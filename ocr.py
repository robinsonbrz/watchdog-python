import pathlib

import cv2
import pytesseract

# corrigir instalação windows:
# https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i

# instalar outra língua: https://github.com/tesseract-ocr/tessdata
# baixar o arquivo por,**** e colar na pasta do tesseract

# pegar linguas: print(pytesseract.get_languages())

# windows instalar tesseract https://github.com/UB-Mannheim/tesseract/wiki


class Image_list():
    '''Classe armazena lista dos arquivos da pasta'''
    def __init__(self):
        self.file_names = []

    def new_image(self, image_full_file_name):
        # descobrir novo arquivo
        # subtrai as duas listas e retorna apenas arquivo novo
        new_file = (set(image_full_file_name) - set(self.file_names)).pop()

        # append novo arquivo
        self.file_names.append(new_file)

        # retorna o novo arquivo
        return new_file

    def apend_list_image(self, image_full_file_name):
        # append lista
        self.file_names.append(image_full_file_name)
        return


class Image():
    def __init__(self, image_full_file_name):
        self.image_name = image_full_file_name
        self.text = ""

    def ocr(self):
        imagem = cv2.imread(self.image_name)
        TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR"
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH + r'\tesseract.exe'
        self.text = pytesseract.image_to_string(imagem, lang="por")
        # retorno da leitura do arquivo
        f = open("..\\OCR_text.txt", "a")
        f.write("#################\n")
        f.write(self.image_name)
        f.write("\n")
        f.write("\n")
        f.write(self.text)
        f.write("\n")
        f.close()
        print("Arquivo reconhecido: ", self.image_name)
        print(self.text)
        return


if __name__ == "__main__":
    path1 = str(pathlib.Path(__file__).parent.resolve()) + r'\watchfolder'
    arquivo = '\\nome_arquivo_teste.jpg'
    full_file_name = path1 + arquivo
    img1 = Image(full_file_name)
    img1.ocr()
