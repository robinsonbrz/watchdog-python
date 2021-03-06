
import glob
import os
import pathlib
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import ocr

PATH1 = str(pathlib.Path(__file__).parent.resolve()) + r'\watchedfolder'


def lista_arquivos_da_pasta_monitorada():
    '''Lista arquivos na pasta monitorada'''
    os.chdir(path=PATH1)
    return glob.glob("*.*")


def on_created(event):
    time.sleep(0.5)
    try:
        list_files = lista_arquivos_da_pasta_monitorada()
        last_file = image_list.new_image(list_files)
        image_full_file_name = PATH1 + "\\" + last_file
        img1 = ocr.Image(image_full_file_name)
        img1.ocr()

    except Exception as e:
        print("occurred. ", e.__class__)
        return

    return


if __name__ == "__main__":

    # objeto acumula a lista de arquivos inseridos na pasta
    image_list = ocr.Image_list()

    list_files = lista_arquivos_da_pasta_monitorada()

    # Casa exista arquivos no diretório já inicializa com a lista desses arquivos no objeto
    image_list.apend_list_image(list_files.sort(key=os.path.getmtime))
    event_handler = FileSystemEventHandler()

    # calling functions for events
    event_handler.on_created = on_created
    # event_handler.on_deleted =on_deleted
    # event_handler.on_modified = on_modified
    # event_handler.on_moved = on_moved

    # caminho que será monitorado
    observer = Observer()
    observer.schedule(event_handler, PATH1, recursive=False)
    observer.start()
    try:
        print("\n##################### Iniciado #####################\nMonitorando a pasta: \n", PATH1, "\n")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("terminado")
    observer.join()
