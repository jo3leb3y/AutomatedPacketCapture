Automated Network Packet Capture and Analysis
Description:
This project aims to automate the process of capturing network packets using Wireshark's command-line tool (tshark.exe) and provides an option to open the captured packet file in Wireshark for analysis. It eliminates the need for manual packet capture using Wireshark's graphical interface, thereby saving time and effort in network troubleshooting and analysis workflows.

Features:
Automated Packet Capture: Captures network packets from a specified interface (e.g., Wi-Fi) for a defined duration and saves them to a pcap file.
Optional Analysis in Wireshark: Provides an option to automatically open the captured packet file in Wireshark after the capture process, facilitating immediate analysis and visualization of network traffic.
Technologies:
Python
Subprocess module
Wireshark (tshark.exe)
Usage:
Clone the repository to your local machine.
Run the Python script capture_packets.py.
Provide the desired interface, capture duration, and output file name.
Optionally, set open_in_wireshark=True to open the captured file in Wireshark after the capture process.
