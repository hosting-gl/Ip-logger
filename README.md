Ip-logger

Overview

Ip-logger is a straightforward, yet powerful Python script designed to monitor changes in your public IP address. With the capability to track both IPv4 and IPv6 addresses, this tool logs your IP to a text file and displays it in the terminal. It's particularly useful if you need to verify whether your Internet Service Provider (ISP) is providing you with a stable, static IP address.

Key Features

Dual IP Version Support: The script checks and logs both IPv4 and IPv6 addresses.
Change Detection: If your IP changes since the last check, the new IP is highlighted in red in the terminal for easy identification.
Color-Coded Display: Consistent IPs are shown in green (IPv4) and blue (IPv6), making it easy to read and understand the output at a glance.
Hourly Updates: Automatically checks your IP every hour, ensuring up-to-date information.
Motivation

I developed Ip-logger out of a personal need to hold my ISP accountable for their promise of a static IP. Despite their assurances, I noticed random changes in my IP address, which led me to create this tool. It serves as a simple, yet effective way to gather proof of these changes.

How to Use

Install Python: Ensure Python is installed on your system.
Install Dependencies: This script requires the requests and colorama libraries. Install them using:
Copy code
pip install requests colorama
Run the Script: Execute the script in your Python environment. The script will automatically start monitoring and logging your IP address.
View Logs: Check the ip_log.txt file for a historical record of your IP addresses and timestamps.
Output Format

The script writes the current time, IPv4, and IPv6 addresses to ip_log.txt.
In the terminal, IPv4 addresses are displayed in green, IPv6 in blue, and any changes since the last log are shown in red.
Limitations & Disclaimer

The accuracy of IP detection is subject to the reliability of external IP checking services.
Ensure to use this tool responsibly, considering privacy and security implications, as IP addresses are sensitive information.
Contributing

Feel free to fork this repository, submit pull requests, or suggest features. Any contributions to enhance Ip-logger are warmly welcomed.

License

This project is open-sourced under the MIT License. See the LICENSE file for more details.r
