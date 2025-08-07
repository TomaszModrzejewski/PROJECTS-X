# MikroTik Configuration Tool

This is a command-line tool to connect to a MikroTik router and perform configuration tasks.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd mikrotik-config-tool
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    -   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Create a `.env` file:**
    Copy the `.env.example` file to `.env` and fill in your router's credentials.
    ```bash
    copy .env.example .env
    ```

## Usage

Run the tool from the command line:

```bash
python mikrotik_cli/cli.py <command> [options]
```

### Available Commands

-   `get-interfaces`: Lists all network interfaces.
-   `get-system-info`: Displays system information (uptime, version, etc.).
-   `set-ntp-client --primary-server <ip> --secondary-server <ip>`: Configures the NTP client.
