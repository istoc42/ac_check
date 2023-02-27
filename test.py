import subprocess
from datetime import datetime

ip_address = 'NBT23276'

print(f"Running ping command for {ip_address}...")
ping_output = subprocess.run(["ping", "-n", "1", "-w", "1000", ip_address], capture_output=True)

if ping_output.returncode == 0:
    print(f"Running systeminfo command for {ip_address}...")
    systeminfo_output = subprocess.run(["systeminfo", f"/s", ip_address, f"/u", "shaun.hudson.a", f"/p", "hexbladewarlock"], capture_output=True)

    print(f'Searching for the System Boot Time for {ip_address}')
    sysinfo_output = systeminfo_output.stdout.decode().splitlines()
    for line in systeminfo_output.stdout.decode().splitlines():
        if line.startswith("System Boot Time:"):
            # Extract the date and time from the line
            boot_time_str = line
            print(boot_time_str)
            # boot_time = datetime.strptime(boot_time_str, "%m/%d/%Y, %I:%M:%S %p")
    