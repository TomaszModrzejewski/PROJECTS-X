import click
from . import router

@click.group()
def cli():
    """A CLI tool to configure a MikroTik router."""
    pass

@cli.command()
def get_interfaces():
    """Lists all network interfaces."""
    connection = router.get_connection()
    if connection:
        interfaces = router.get_interfaces(connection)
        if interfaces:
            for interface in interfaces:
                print(interface)
        connection.disconnect()

@cli.command()
def get_system_info():
    """Displays system information."""
    connection = router.get_connection()
    if connection:
        info = router.get_system_info(connection)
        if info:
            print(info)
        connection.disconnect()

@cli.command()
@click.option('--primary-server', required=True, help='Primary NTP server IP address.')
@click.option('--secondary-server', required=True, help='Secondary NTP server IP address.')
def set_ntp_client(primary_server, secondary_server):
    """Configures the NTP client."""
    connection = router.get_connection()
    if connection:
        router.set_ntp_client(connection, primary_server, secondary_server)
        connection.disconnect()

if __name__ == '__main__':
    cli()