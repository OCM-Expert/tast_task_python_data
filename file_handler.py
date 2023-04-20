from zipfile import ZipFile
import os


class FileHandler:
    """
    Класс для управления файлами.
    """
    def extract(self):
        """
        Метод распаковкни zip-файла
        :return: None
        """
        with ZipFile('doc_tasks.zip', 'r') as file:
            file.extractall()

    def remove(self):
        """
        Метод удаления csv-файла
        :return: None
        """
        os.remove('doc_tasks.csv')
