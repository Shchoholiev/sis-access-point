# sis-access-point
A Python-based access control system integrating PIR motion sensors and camera operations to detect motion, capture images, and interact with a backend for smart inventory management.

## Table of Contents
- [Features](#features)
- [Stack](#stack)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [Configuration](#configuration)

## Features
- Monitors PIR motion sensors for detection of motion.
- Captures images automatically via a connected camera when motion is detected.
- Sends captured images to a backend API for identifying items.
- Provides logging with rotating log files for detailed operational insights.
- Supports device and application configuration through JSON files.
- Designed for Raspberry Pi hardware integration (GPIO and camera).

## Stack
- Python 3.9+
- [gpiozero](https://gpiozero.readthedocs.io) for motion sensor interfacing.
- [Pillow](https://python-pillow.org/) for image handling.
- Requests for HTTP communication.
- libcamera tools (libcamera-still) for camera image capture.
- Logging with Python `logging` and `RotatingFileHandler`.
- Packaging and environment management with setuptools and devcontainers.

## Installation

### Prerequisites
- Raspberry Pi running a compatible OS (e.g., Raspberry Pi OS).
- Python 3.9 or above installed.
- Camera module compatible with `libcamera-still`.
- PIR motion sensor connected to an appropriate GPIO pin.
- Install `libcamera` tools on your system.
- Internet connection for backend API access.

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/Shchoholiev/sis-access-point.git
   cd sis-access-point
   ```

2. Create and activate a Python virtual environment (optional, but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) If using the devcontainer, open the folder with VSCode and launch the devcontainer for a consistent dev environment.

5. Run the application with:
   ```bash
   accesspoint
   ```
   Or alternatively:
   ```bash
   python -m access_point.app.app
   ```

## Configuration
Configuration files are located in the `access_point/app` directory:

- `appconfig.json` — Contains backend API URLs and Azure IoT Hub hostname.
- `deviceconfig.json` — Stores device-specific identifiers and access keys.

Example `appconfig.json` content:
```json
{
    "apiUrl": "https://smart-inventory-system.azurewebsites.net",
    "azureIoTHub": {
        "hostName": "smart-inventory-system.azure-devices.net"
    }
}
```

Example `deviceconfig.json` content:
```json
{
    "deviceId": "your-device-id",
    "accessKey": "your-access-key"
}
```

Modify these JSON files to match your environment and credentials before running the application.
