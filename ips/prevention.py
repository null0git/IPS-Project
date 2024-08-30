import subprocess

def block_ip(ip_address):
    try:
        subprocess.run(["iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"], check=True)
        print(f"IP address {ip_address} has been blocked.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to block IP address {ip_address}: {e}")
