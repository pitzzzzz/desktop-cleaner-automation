from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil

class MyHandler(FileSystemEventHandler):
    fed on_modified(self, event): #when files are added to desktop
        for filename in os.listedir(folder_to_track):
            i = 1
            if filename != 'sort':
                try:
                    extention = str(os.path.splittext(folder_to_track + '/' + filename)[1])
                    new_name = filename
                    file_exists = os.path.isfile(extentions_folders[extension] + '/' + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splittext(folder_to_track + '/' new_name)[0] + str(i) + os.path.splittext
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination + "/" + new_name)
                src = folder_to_track + "/" + filename
                new_name = folder_destination + "/" + new_name
                os.rename(src, new_name)
        except Exception:
            print(filename)

extentions_folders = {
    # Audio Files
    '.aif' : "/Users/Joshua/Desktop/sort/media/audio",
    '.cda' : "/Users/Joshua/Desktop/sort/media/audio",
    '.mid' : "/Users/Joshua/Desktop/sort/media/audio",
    '.midi' : "/Users/Joshua/Desktop/sort/media/audio",
    '.mp3' : "/Users/Joshua/Desktop/sort/media/audio",
    '.mpa' : "/Users/Joshua/Desktop/sort/media/audio",
    '.ogg' : "/Users/Joshua/Desktop/sort/media/audio",
    '.wav' : "/Users/Joshua/Desktop/sort/media/audio",
    '.wma' : "/Users/Joshua/Desktop/sort/media/audio",
    '.wpl' : "/Users/Joshua/Desktop/sort/media/audio",
# Text Files
    '.txt' : "/Users/Joshua/Desktop/sort/text/textfiles",
    '.dox' : "/Users/Joshua/Desktop/sort/text/microsoft/word",
    '.docx' : "/Users/Joshua/Desktop/sort/text/microsoft/word",
    '.odt' : "/Users/Joshua/Desktop/sort/text/textfiles",
    '.pdf' : "/Users/Joshua/Desktop/sort/text/pdf",
    '.rtf' : "/Users/Joshua/Desktop/sort/text/textfiles",
    '.tex' : "/Users/Joshua/Desktop/sort/text/textfiles",
    '.wks' : "/Users/Joshua/Desktop/sort/text/textfiles",
    '.wps' : "/Users/Joshua/Desktop/sort/text/textfiles",
    '.wpd' : "/Users/Joshua/Desktop/sort/text/textfiles",
# Spreadsheet Files
    '.xlsx' : "/Users/Joshua/Desktop/sort/text/microsoft/excel",
    '.xls' : "/Users/Joshua/Desktop/sort/text/microsoft/excel",
# Video Files
    '.mov' : "/Users/Joshua/Desktop/sort/media/video",
    '.mp4' : "/Users/Joshua/Desktop/sort/media/video",
# Image Files
    '.ai' : "/Users/Joshua/Desktop/sort/media/image",
    '.jpg' : "/Users/Joshua/Desktop/sort/media/image",
    '.jpeg' : "/Users/Joshua/Desktop/sort/media/image",
    '.png' : "/Users/Joshua/Desktop/sort/media/image",
    '.gif' : "/Users/Joshua/Desktop/sort/media/image",
# Data files
    '.csv' : "/Users/Joshua/Desktop/sort/media/image",
# Executable files

    
    
    
    
}
                

folder_to_track = '/Users/Joshua/Desktop'
folder_destination = '/Users/Joshua/Desktop/sort/'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()



