# Connection Service
## Encrypted Wifi Connection Service for Speech4Kids
## Overview
The Connection Service bridges IoT devices with backend services using Wi-Fi, MQTT, and gRPC.

## Features
- Wi-Fi connection management
- MQTT-based communication
- gRPC client for backend interaction

# Directory structure
connection_service/
├── app/
│   ├── __init__.py                # Initialize the service package
│   ├── main.py                    # Entry point for the service
│   ├── routes/                    # API endpoints for the service (if needed for local control)
│   │   ├── __init__.py
│   │   └── iot_connection.py      # Local routes for device control
│   ├── services/                  # Core business logic for device connection
│   │   ├── __init__.py
│   │   ├── wifi_connector.py      # Wi-Fi connection logic
│   │   ├── mqtt_client.py         # MQTT client implementation
│   │   └── grpc_client.py         # gRPC client to communicate with backend
│   ├── utils/                     # Utility functions and helpers
│   │   ├── __init__.py
│   │   ├── logger.py              # Logging configuration
│   │   ├── encryption.py          # Encryption and TLS helpers
│   │   └── device_config.py       # Device-specific configuration
│   └── config/                    # Configuration settings
│       ├── __init__.py
│       └── settings.py            # Environment-based configurations
├── tests/                         # Unit and integration tests
│   ├── __init__.py
│   ├── test_mqtt_client.py        # Test cases for MQTT logic
│   ├── test_wifi_connector.py     # Test cases for Wi-Fi connection
│   └── test_grpc_client.py        # Test cases for gRPC client
├── Dockerfile                     # Dockerfile for containerization
├── requirements.txt               # Python dependencies
├── Makefile                       # Common development commands
└── README.md                      # Documentation for the service


## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the service:
    make run

3. Test the service:
    make test
