import subprocess
import sys
import os
from status import Status

status = Status()

def fan(action):
    if action == "status":
        print(subprocess.run("sudo uhubctl -l 1-1 | grep 'Port 2' | awk '{print $4}'", shell=True, stdout=subprocess.PIPE).stdout.decode("utf-8"))
    else:
        subprocess.run(f"sudo uhubctl -l 1-1 -p 2 -a {action}", shell=True, stdout=subprocess.DEVNULL)
        status.fan_on = action == "on"


if __name__ == "__main__":

    if os.geteuid() != 0:
        sys.exit("This script needs to be run as root")

    if len(sys.argv) != 2:
        sys.exit("Please provide an action(on/off)")

    action = sys.argv[1]

    fan(action)
