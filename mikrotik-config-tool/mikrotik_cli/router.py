import os
import routeros_api
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """Establishes a connection to the MikroTik router."""
    try:
        connection = routeros_api.RouterOsApiPool(
            os.getenv('ROUTER_IP'),
            username=os.getenv('ROUTER_USER'),
            password=os.getenv('ROUTER_PASSWORD'),
            plaintext_login=True
        )
        return connection
    except Exception as e:
        print(f"Error connecting to router: {e}")
        return None

def get_interfaces(connection):
    """Retrieves the list of interfaces."""
    try:
        api = connection.get_api()
        interfaces = api.get_resource('/interface')
        return interfaces.get()
    except Exception as e:
        print(f"Error getting interfaces: {e}")
        return None

def get_system_info(connection):
    """Retrieves system information."""
    try:
        api = connection.get_api()
        system_info = api.get_resource('/system/resource')
        return system_info.get()
    except Exception as e:
        print(f"Error getting system info: {e}")
        return None

def set_ntp_client(connection, primary_server, secondary_server):
    """Configures the NTP client."""
    try:
        api = connection.get_api()
        ntp_client = api.get_resource('/system/ntp/client')
        ntp_client.set(
            enabled='yes',
            primary_ntp=primary_server,
            secondary_ntp=secondary_server
        )
        print("NTP client configured successfully.")
    except Exception as e:
        print(f"Error setting NTP client: {e}")