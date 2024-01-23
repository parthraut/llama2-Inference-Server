
import subprocess
import sys

if __name__ == "__main__":
    path = ""
    process = subprocess.Popen(path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the script to complete and get the output
    stdout, stderr = process.communicate()

    # Handle the outputs
    if process.returncode == 0:
        print("Script output:", stdout.decode())
    else:
        print("An error occurred:", stderr.decode())
        sys.exit(process.returncode)