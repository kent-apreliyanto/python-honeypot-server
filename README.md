# Low-Interaction Network Honeypot

A low-interaction cybersecurity honeypot designed to deploy fake vulnerable network services, attract unauthorized connections, and log attacker payloads for forensic analysis.

## Features
- **Custom Port Binding:** Deploys a deceptive server on any specified port using socket programming.
- **Deceptive Banners:** Feeds attackers fake system information (e.g., Ubuntu SSH) to encourage payload execution.
- **Automated Logging:** Silently records attacker IP addresses, source ports, and raw injected payloads into a persistent `intrusion.log` file.
- **Connection Dropping:** Immediately terminates connections after data capture to protect the host machine from sustained interaction.

## Technology Stack
- Python 3
- `socket` (Network listening and connection handling)
- `logging` (Forensic data recording)
- `argparse` (CLI port configuration)

## How to Run
1. Clone this repository.
2. Deploy the honeypot on a specific port (e.g., 8080):
   ```bash
   python honeypot.py -p 8080

## Security Notice
This tool is designed for educational purposes, defensive cybersecurity research, and authorized network monitoring only.