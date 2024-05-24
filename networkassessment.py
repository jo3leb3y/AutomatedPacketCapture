import subprocess

def capture_packets(interface, duration, output_file, open_in_wireshark=False):
    tshark_path = r'C:\Program Files\Wireshark\tshark.exe'  # Example path
    command = [tshark_path, '-i', interface, '-a', f'duration:{duration}', '-w', output_file]
    subprocess.run(command)

    if open_in_wireshark:
        open_in_wireshark_with_tshark(output_file)

def open_in_wireshark_with_tshark(file_path):
    wireshark_path = r'C:\Program Files\Wireshark\Wireshark.exe'  # Example path
    command = [wireshark_path, '-r', file_path]
    subprocess.Popen(command)

# Example usage
capture_packets('Wi-Fi', 10, 'capture.pcap', open_in_wireshark=True)
