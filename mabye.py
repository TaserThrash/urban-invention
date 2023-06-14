
import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Taser/Documents/byjus coding/python-1/project 103 perhaps"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_modified(self, event):
        print(f"Oops! Someone modified {event.src_path}!")
        name, extention = os.path.splitext(event.src_path)
        time.sleep(1)

    def on_moved(self, event):
        print(f"{event.src_path} moved")
        name, extention = os.path.splitext(event.src_path)
        time.sleep(1)

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive = True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
