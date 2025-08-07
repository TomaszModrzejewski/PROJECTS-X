from flask import render_template, request, redirect, url_for, session, flash
from app import app
from proxmoxer import ProxmoxAPI
import os
from dotenv import load_dotenv

load_dotenv()

def get_proxmox_api():
    if 'proxmox_host' in session:
        try:
            return ProxmoxAPI(
                session['proxmox_host'],
                user=session['proxmox_user'],
                password=session['proxmox_password'],
                verify_ssl=False
            )
        except Exception as e:
            flash(f"Error connecting to Proxmox: {e}", "danger")
            return None
    return None

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['proxmox_host'] = request.form['host']
        session['proxmox_user'] = request.form['user']
        session['proxmox_password'] = request.form['password']
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    proxmox = get_proxmox_api()
    if not proxmox:
        return redirect(url_for('login'))

    nodes = proxmox.nodes.get()
    vms = []
    for node in nodes:
        for vm in proxmox.nodes(node['node']).qemu.get():
            vms.append(vm)
        for container in proxmox.nodes(node['node']).lxc.get():
            vms.append(container)

    return render_template('dashboard.html', vms=vms)

@app.route('/vm/start/<node>/<vmid>')
def start_vm(node, vmid):
    proxmox = get_proxmox_api()
    if proxmox:
        try:
            proxmox.nodes(node).qemu(vmid).status.start.post()
            flash(f"VM {vmid} started successfully.", "success")
        except Exception as e:
            flash(f"Error starting VM {vmid}: {e}", "danger")
    return redirect(url_for('dashboard'))

@app.route('/vm/stop/<node>/<vmid>')
def stop_vm(node, vmid):
    proxmox = get_proxmox_api()
    if proxmox:
        try:
            proxmox.nodes(node).qemu(vmid).status.stop.post()
            flash(f"VM {vmid} stopped successfully.", "success")
        except Exception as e:
            flash(f"Error stopping VM {vmid}: {e}", "danger")
    return redirect(url_for('dashboard'))

@app.route('/vm/reboot/<node>/<vmid>')
def reboot_vm(node, vmid):
    proxmox = get_proxmox_api()
    if proxmox:
        try:
            proxmox.nodes(node).qemu(vmid).status.reboot.post()
            flash(f"VM {vmid} rebooted successfully.", "success")
        except Exception as e:
            flash(f"Error rebooting VM {vmid}: {e}", "danger")
    return redirect(url_for('dashboard'))