import requests
import time
from colorama import Fore, Style, init

init()  # Initialize colorama

def get_public_ip(url):
    try:
        response = requests.get(url)
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"

def write_ip_to_file_and_print(ipv4, ipv6, last_ipv4, last_ipv6):
    with open("ip_log.txt", "a") as file:
        file.write(f"{time.ctime()} - IPv4: {ipv4}, IPv6: {ipv6}\n")
    
    # Printing IPv4
    if ipv4 != last_ipv4:
        print(Fore.RED + f"IPv4 Changed: {ipv4}")
    else:
        print(Fore.GREEN + f"IPv4: {ipv4}")

    # Printing IPv6
    if ipv6 != last_ipv6:
        print(Fore.RED + f"IPv6 Changed: {ipv6}")
    else:
        print(Fore.CYAN + f"IPv6: {ipv6}")  # Light blue is typically represented as cyan in terminal colors

    print(Style.RESET_ALL)

last_ipv4, last_ipv6 = None, None

while True:
    ipv4 = get_public_ip('https://api.ipify.org')
    ipv6 = get_public_ip('https://api6.ipify.org')

    write_ip_to_file_and_print(ipv4, ipv6, last_ipv4, last_ipv6)

    last_ipv4, last_ipv6 = ipv4, ipv6

    time.sleep(300)  # 300 seconds = 5 minutes
