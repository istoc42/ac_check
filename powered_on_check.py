import subprocess
from datetime import datetime

# Get datetime stamp at beginning of search. Print to console
start = datetime.now()
# Convert to readable date and time
dt_string = start.strftime("%d/%m/%Y %H:%M:%S")
print("Time started: ", dt_string)

with open('ip_list.txt', 'r') as ip_file:
    # Open the output file for writing
    with open("output.txt", "w") as output_file:

        for line in ip_file:
            ip_address = line.strip()

            # Run the ping command to check if the PC is reachable
            print(f"Running ping command for {ip_address}...")
            ping_output = subprocess.run(["ping", "-n", "1", "-w", "1000", ip_address], capture_output=True)

            # Check if the PC is reachable
            if ping_output.returncode == 0:
                # The PC is reachable, so run the "systeminfo" command to get the last boot time
                print(f"Running systeminfo command for {ip_address}...")
                systeminfo_output = subprocess.run(["systeminfo", f"/s", ip_address, f"/u", "shaun.hudson.a", f"/p", "hexbladewarlock"], capture_output=True) #TODO: Asking for a password at this stage in CMD

                # Search for the "System Boot Time" line in the output
                print(f'Searching for the System Boot Time for {ip_address}')
                for line in systeminfo_output.stdout.decode().splitlines():
                    if line.startswith("System Boot Time:"):
                        # Extract the date and time from the line
                        boot_time_str = line.split(":")[1].strip()

                        # Print the boot time
                        print(f"The last time {ip_address} was powered on: {boot_time_str}")

                        # Write the output to the file
                        output_file.write(f"The last time {ip_address} was powered on: {boot_time_str}\n")
                        break
            else:
                # The PC is not reachable
                print(f"{ip_address} is not reachable.")
                # Write the output to the file
                output_file.write(f"{ip_address} is not reachable.\n")

print("Script finished.")

# Get datetime stamp at end of search. Print to console.
finish = datetime.now()
# Convert to readable date and time
dt_string_end = finish.strftime("%d/%m/%Y %H:%M:%S")
print("Time finished: ", dt_string_end)

# Calculate time taken to run script.
time_taken = finish - start
# Convert to readable date and time
hours, minutes, seconds = time_taken.seconds // 3600, time_taken.seconds // 60 % 60, time_taken.seconds
print(f"Time taken: {minutes} minutes and {seconds} seconds.")
