
import glob
import logging
import os
import pathlib
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


def on_created(event):
    path1 = str(pathlib.Path(__file__).parent.resolve()) + '\watchfolder'
    os.chdir(path=path1)
    list_of_files = glob.glob("*.*")
    list_of_files.sort(key=os.path.getmtime)
    last_file = list_of_files[len(list_of_files)-1]
    print('last_file: ' + last_file)
    #print(last_file)
    print("created")
        
def on_deleted(event):
    # print("deleted")
    pass
        
def on_modified(event):
    # print("modified")
    pass
        
def on_moved(event):
    # print("moved")
    pass


if __name__ == "__main__":
    event_handler = FileSystemEventHandler()
    # calling functions
    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved

    # caminho que será observado
    path = str(pathlib.Path(__file__).parent.resolve()) + '\watchfolder'
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        print("Monitorando")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("terminado")
    observer.join()
    


# caminho = str(pathlib.Path(__file__).parent.resolve()) + '\watchfolder'
# print(caminho)











