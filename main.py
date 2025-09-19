from alive_progress import alive_bar
import time

with alive_bar(3) as bar:
    for _ in range(3):
        time.sleep(1)
        bar()
