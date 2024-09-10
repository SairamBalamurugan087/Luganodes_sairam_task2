# Polygon Validator Monitoring Tool

This repository contains a containerized application that monitors a Polygon validator node and sends alerts via Telegram when certain conditions are met.

## Project Structure
```plaintext
polygon-validator-monitor/
│
├── src/
│   ├── main.py          # Main entry point of the application; orchestrates monitoring and alerting.
│   ├── monitor.py       # Contains core monitoring functionality; checks validator status and sync progress.
│   ├── alerts.py        # Handles alerting functionality; sends alerts via Telegram.
│   └── config.py        # Loads configuration settings from the config.yaml file.
│
├── config.yaml           # Configuration file for the application; contains settings for validator and alerts.
│
├── Dockerfile            # Dockerfile to build a container image for the application.
│
└── requirements.txt      # Lists Python dependencies required for the application.```




## File Descriptions

- **`main.py`**: 
  - The main entry point of the application. It orchestrates the monitoring process by calling functions from other modules and handles alerting logic based on the validator's status.

- **`monitor.py`**: 
  - Contains the core monitoring functionality that checks the status of the Polygon validator and determines if it is synced with the blockchain.

- **`alerts.py`**: 
  - Manages the alerting process by sending messages to a specified Telegram chat whenever issues are detected with the validator.

- **`config.py`**: 
  - Responsible for loading the configuration settings from the `config.yaml` file, making it easy to manage application settings.

- **`config.yaml`**: 
  - A YAML configuration file that stores essential settings such as the validator address, RPC endpoint, Telegram bot token, and thresholds for alerts.

- **`Dockerfile`**: 
  - A file used to create a Docker image for the application, allowing for easy deployment and scalability in various environments.

- **`requirements.txt`**: 
  - A text file that lists the Python packages required for the application to run, ensuring that all dependencies are installed.

## License

This project is licensed under the MIT License.
