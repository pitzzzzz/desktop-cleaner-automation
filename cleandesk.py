from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil

folder_to_track = '/Users/Joshua/Desktop'
folder_destination = '/Users/Joshua/Desktop/sort/'

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
# Presentation Files
    '.key' : "/Users/Joshua/Desktop/sort/text/presentations",
    '.pps' : "/Users/Joshua/Desktop/sort/text/presentations",
    '.ppt' : "/Users/Joshua/Desktop/sort/text/presentations",
    '.pptx' : "/Users/Joshua/Desktop/sort/text/presentations",
    '.odp' : "/Users/Joshua/Desktop/sort/text/presentations",
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
    '.csv' : "/Users/Joshua/Desktop/sort/programming/database",
    '.dat' : "/Users/Joshua/Desktop/sort/programming/database",
    '.db' : "/Users/Joshua/Desktop/sort/programming/database",
    '.dbf' : "/Users/Joshua/Desktop/sort/programming/database",
    '.log' : "/Users/Joshua/Desktop/sort/programming/database",
    '.sql' : "/Users/Joshua/Desktop/sort/programming/database",
    '.tar' : "/Users/Joshua/Desktop/sort/programming/database",
    '.json' : "/Users/Joshua/Desktop/sort/programming/database",
    '.xml' : "/Users/Joshua/Desktop/sort/programming/database",
    '.mdb' : "/Users/Joshua/Desktop/sort/programming/database",
    '.sav' : "/Users/Joshua/Desktop/sort/programming/database",
# Executable files
    '.exe' : "/Users/Joshua/Desktop/sort/other/executables",
    '.com' : "/Users/Joshua/Desktop/sort/other/executables",
    '.bat' : "/Users/Joshua/Desktop/sort/other/executables",
    '.jar' : "/Users/Joshua/Desktop/sort/other/executables",
    '.wsf' : "/Users/Joshua/Desktop/sort/other/executables",
# Program Files
    '.c' : "/Users/Joshua/Desktop/sort/programming/c&c++",
    '.class' : "/Users/Joshua/Desktop/sort/programming/java",
    '.java' : "/Users/Joshua/Desktop/sort/programming/java",
    '.dart' : "/Users/Joshua/Desktop/sort/programming/dart",
    '.py' : "/Users/Joshua/Desktop/sort/programming/python",
    '.sh' : "/Users/Joshua/Desktop/sort/programming/shell",
    '.swift' : "/Users/Joshua/Desktop/sort/programming/swift",
    '.html' : "/Users/Joshua/Desktop/sort/programming/html",
    '.rs' : "/Users/Joshua/Desktop/sort/programming/rust",
    '.PHP' : "/Users/Joshua/Desktop/sort/programming/php",
    '.c' : "/Users/Joshua/Desktop/sort/programming/c&c++",
}

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'sort':
                try:
                    extention = os.path.splitext(filename)[1]
                    new_name = filename
                    file_exists = os.path.isfile(extentions_folders[extention] + '/' + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(filename)[0] + str(i) + os.path.splitext(filename)[1]
                        file_exists = os.path.isfile(extentions_folders[extention] + "/" + new_name)
                    src = folder_to_track + "/" + filename
                    new_name = extentions_folders[extention] + "/" + new_name
                    shutil.move(src, new_name)
                except Exception as e:
                    print(f"Error moving file {filename}: {e}")

if __name__ == "__main__":
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