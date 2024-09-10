# Polygon Validator Monitoring Tool

This repository contains a containerized application that monitors a Polygon validator node and sends alerts via Telegram when certain conditions are met.

## Project Structure
polygon-validator-monitor/
│
├── src/
│ ├── main.py # Main entry point of the application; orchestrates monitoring and alerting.
│ ├── monitor.py # Contains core monitoring functionality; checks validator status and sync progress.
│ ├── alerts.py # Handles alerting functionality; sends alerts via Telegram.
│ └── config.py # Loads configuration settings from the config.yaml file.
│
├── config.yaml # Configuration file for the application; contains settings for validator and alerts.
│
├── Dockerfile # Dockerfile to build a container image for the application.
│
└── requirements.txt # Lists Python dependencies required for the application.
