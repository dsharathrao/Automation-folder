from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler


import os
import json
import time

class Myhandler(FileSystemEventHandler):
	i = 1
	def on_modified(self, event):
		for filename in os.listdir(folder_to_track):
			src = folder_to_track + "/" + filename
			new_destination = folder_destination + "/" + filename
			os.rename(src, new_destination)


folder_to_track = "C:/Users/bujji/Desktop/123"
folder_destination = "C:/Users/bujji/Desktop/abc"

event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	observer.stop()
observer.join()
