# Basic Network Sniffer

This project is a Python-based network sniffer developed as part of the CodeAlpha Cybersecurity Internship program. The purpose of this tool is to capture and analyze network traffic packets to understand network data flow and the basics of communication protocols.

---

### Features

- Captures network packets in real-time.
- Analyzes captured packets to understand their structure and content.
- Displays key information for each packet, including:
    - Source IP and Destination IP
    - Protocol (e.g., TCP, UDP)
    - Payload (optional, if you added this feature)
- Utilizes the `scapy` library for robust packet manipulation.

---

### Technologies Used

- **Language:** Python
- **Libraries:** Scapy

---

### How to Run the Program

#### Prerequisites

Before running the program, ensure you have the following installed:

1.  **Python:** [You can add a link to the official Python download page here, e.g., `https://www.python.org/downloads/`]
2.  **Scapy:** Install using pip.
    ```bash
    pip install scapy
    ```
3.  **Npcap (for Windows users):** Download and install Npcap from the official website ([You can add a link to the Npcap download page here, e.g., `https://nmap.org/npcap/`]). Make sure to check the "Install Npcap in WinPcap API-compatible Mode" option during installation.

#### Usage

1.  Clone the repository:
    ```bash
    git clone [https://github.com/cyberknight2024/BasicNetworkSniffer.git](https://github.com/cyberknight2024/BasicNetworkSniffer.git)
    cd BasicNetworkSniffer
    ```
2.  Run the Python script from your terminal:
    ```bash
    python sniffer.py
    ```
3.  The program will start sniffing for network packets and display the details in the console. You can modify the `sniff()` function in the script to change the number of packets captured or specify a network interface.
