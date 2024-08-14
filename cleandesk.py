from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil

folder_to_track = '\\Users\\Joshua\\Desktop'
folder_destination = '\\Users\\Joshua\\Desktop\\home'

extentions_folders = {
# No name
    'noname' : "\\Users\\Joshua\\Desktop\\home\\text\\other\\uncategorized",
# Main Desktop Format
    'main-desktop' : "\\Users\\Joshua\\Desktop\\home",
# Audio Files
    '.aif' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\audio",
    '.cda' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\audio",
    '.mid' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\audio",
    '.midi' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\audio",
    '.mp3' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\audio",
    '.mpa' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\audio",
    '.ogg' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\audio",
    '.wav' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\audio",
    '.wma' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\audio",
    '.wpl' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\audio",
# Text Files
    '.txt' : r"C:\\Users\\Joshua\\Desktop\\home\\other\\executables",
    '.dox' : r"C:\\Users\\Joshua\\Desktop\\home\\text\\microsoft\\word",
    '.docx' : r"C:\\Users\\Joshua\\Desktop\\home\\text\\microsoft\\word",
    '.odt' : r"C:\\Users\\Joshua\\Desktop\\home\\other\\executables",
    '.pdf' : r"C:\\Users\\Joshua\\Desktop\\home\\text\\pdf",
    '.rtf' : r"C:\\Users\\Joshua\\Desktop\\home\\other\\executables",
    '.tex' : r"C:\\Users\\Joshua\\Desktop\\home\\other\\executables",
    '.wks' : r"C:\\Users\\Joshua\\Desktop\\home\\other\\executables",
    '.wps' : r"C:\\Users\\Joshua\\Desktop\\home\\other\\executables",
    '.wpd' : r"C:\\Users\\Joshua\\Desktop\\home\\other\\executables",
# Presentation Files
    '.key' : r"C:\\Users\\Joshua\\Desktop\\home\\text\\presentations",
    '.pps' : r"C:\\Users\\Joshua\\Desktop\\home\\text\\presentations",
    '.ppt' : r"C:\\Users\\Joshua\\Desktop\\home\\text\\presentations",
    '.pptx' : r"C:\\Users\\Joshua\\Desktop\\home\\text\\presentations",
    '.odp' : r"C:\\Users\\Joshua\\Desktop\\home\\text\\presentations",
# Spreadsheet Files
    '.xlsx' : r"C:\\Users\\Joshua\\Desktop\\home\\text\\microsoft\\excel",
    '.xls' : r"C:\\Users\\Joshua\\Desktop\\home\\text\\microsoft\\excel",
# Video Files
    '.mov' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\video",
    '.mp4' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\video",
# Image Files
    '.ai' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\image",
    '.jpg' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\image",
    '.jpeg' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\image",
    '.png' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\image",
    '.gif' : r"C:\\Users\\Joshua\\Desktop\\home\\media\\image",
# Data files
    '.csv' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\database",
    '.dat' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\database",
    '.db' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\database",
    '.dbf' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\database",
    '.log' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\database",
    '.sql' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\database",
    '.tar' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\database",
    '.json' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\database",
    '.xml' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\database",
    '.mdb' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\database",
    '.sav' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\database",
# Executable files
    '.exe' : r"C:\\Users\\Joshua\\Desktop\\home\\other\\executables",
    '.com' : r"C:\\Users\\Joshua\\Desktop\\home\\other\\executables",
    '.bat' : r"C:\\Users\\Joshua\\Desktop\\home\\other\\executables",
    '.jar' : r"C:\\Users\\Joshua\\Desktop\\home\\other\\executables",
    '.wsf' : r"C:\\Users\\Joshua\\Desktop\\home\\other\\executables",
# Program Files
    '.c' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\c&c++",
    '.class' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\java",
    '.java' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\java",
    '.dart' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\dart",
    '.py' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\python",
    '.sh' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\shell",
    '.swift' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\swift",
    '.html' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\html",
    '.rs' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\rust",
    '.PHP' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\php",
    '.c' : r"C:\\Users\\Joshua\\Desktop\\home\\programming\\c&c++",
}

for path in extentions_folders.values():
    if not os.path.exists(path):
        print(f"Destination folder does not exist: {path}")

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Detected modification: {event.src_path}")
        # Itterate over the files in the folder to track (desktop)
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'home':
                try:
                    extention = os.path.splitext(filename)[1]
                    new_name = filename
                    # Determine the destination path
                    path = extentions_folders.get(extention, extentions_folders['noname'])
                    if not os.path.exists(path):
                        print(f"Destination folder does not exist: {path}")
                        continue
                    
                    file_exists = os.path.isfile(os.path.join(path, new_name))
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(filename)[0] + str(i) + os.path.splitext(filename)[1]
                        file_exists = os.path.isfile(os.path.join(path, new_name))
                    
                    # Source and destination paths
                    src = os.path.join(folder_to_track, filename)
                    new_name = os.path.join(path, new_name)
                    # Log the file movement
                    print(f"Moving file from {src} to {new_name}")
                    # Proceed to move the file
                    shutil.move(src, new_name)
                except Exception as e:
                    # Log any errors that may occur
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