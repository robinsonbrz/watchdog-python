
import glob
import logging
import os
import pathlib
import sys
import time
from cmath import e

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import ocr

PATH1 = str(pathlib.Path(__file__).parent.resolve()) + '\watchfolder'

def lista_arquivos_da_pasta_monitorada():
    '''Lista arquivos na pasta monitorada'''
    # path1 = str(pathlib.Path(__file__).parent.resolve()) + '\watchfolder'
    os.chdir(path=PATH1)
    return glob.glob("*.*")




def print_file(file_name):
    print(file_name)
    return


def on_created(event):
    time.sleep(0.5)
    # print(image_list.file_names)

    try:
        list_files = lista_arquivos_da_pasta_monitorada()
        last_file = image_list.new_image(list_files)
        image_full_file_name = PATH1 + "\\" + last_file
        img1 = ocr.Image(image_full_file_name)
        img1.ocr()
        # list_of_files.sort(key=os.path.getmtime)
        # last_file = list_of_files[len(list_of_files)-1]
    except Exception as e:
        print(e.__class__, "occurred.")
        return 

    return
        

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

    # objeto acumula a lista de arquivos inseridos na pasta
    image_list = ocr.Image_list()


    list_files = lista_arquivos_da_pasta_monitorada()

    # Casa exista arquivos no diretório já inicializa com a lista desses arquivos
    image_list.apend_list_image( list_files.sort(key=os.path.getmtime))
    event_handler = FileSystemEventHandler()

    # calling functions
    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_modified = on_modified
    event_handler.on_moved = on_moved

    # caminho que será monitorado
    path = str(pathlib.Path(__file__).parent.resolve()) + '\watchfolder'
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        print("\n##################### Iniciado #####################\nMonitorando a pasta: ", PATH1)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("terminado")
    observer.join()
    


# caminho = str(pathlib.Path(__file__).parent.resolve()) + '\watchfolder'
# print(caminho)











