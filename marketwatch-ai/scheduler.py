import subprocess
import time

while True:

    subprocess.run(
        ["python", "main.py"]
    )

    print(
        "New prices collected"
    )

    time.sleep(60)