#import argparse
#import subprocess

# Parse command line arguments
#parser = argparse.ArgumentParser(description='Perform a vulnerability scan using Nikto')
#parser.add_argument('ip_address_or_domain', help='IP address or domain to scan')
#args = parser.parse_args()

# Run the vulnerability scan using Nikto
#subprocess.run(["nikto", "-h", args.ip_address_or_domain])

import nmap
import subprocess

def main():
    ip_address_or_subnet = input("Enter the IP address or subnet to scan: ")
    vuln_scan = input("Perform a vulnerability scan using NSE scripts? (yes/no): ").lower() == 'yes'
    nikto_scan = input("Perform a vulnerability scan using Nikto? (yes/no): ").lower() == 'yes'

    # Initialize nmap scanner
    scanner = nmap.PortScanner()

    # Build the scan command with the specified arguments
    command = f"-sV {ip_address_or_subnet}"
    if vuln_scan:
        command += " --script=vuln"
    if nikto_scan:
        # Run the vulnerability scan using Nikto
        subprocess.run(["nikto", "-h", ip_address_or_subnet])

    # Run the scan
    scan_results = scanner.scan(command)

    # Print the results
    for host in scan_results['scan']:
        print(f"Host: {host}")
        if 'tcp' in scan_results['scan'][host]:
            for port in scan_results['scan'][host]['tcp']:
                print(f"  -> Port: {port}")
                print(f"  State: {scan_results['scan'][host]['tcp'][port]['state']}")
                print(f"  Service: {scan_results['scan'][host]['tcp'][port]['name']}")
                print(f"  Version: {scan_results['scan'][host]['tcp'][port]['product']} {scan_results['scan'][host]['tcp'][port]['version']}")
                if vuln_scan:
                    if 'script' in scan_results['scan'][host]['tcp'][port]:
                        for script in scan_results['scan'][host]['tcp'][port]['script']:
                            print(f"  Vulnerability: {script}")
        if vuln_scan:
            if 'hostscript' in scan_results['scan'][host]:
                for script in scan_results['scan'][host]['hostscript']:
                    print(f"  Vulnerability: {script}")

if __name__ == "__main__":
    main()
