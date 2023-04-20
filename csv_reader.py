import sqlite3 as sq
import os.path

import pandas as pd

from file_handler import FileHandler
from db import Doc


def dataframe_setup(con: sq.Connection):
    """
    Функция, считывающая csv, оставляющая только просроченные таски, и оставляющая в поле "Организация" только города
    :param con: sq.Connection - соединение с БД
    :return: None
    """
    df = pd.read_csv('doc_tasks.csv')
    df.drop('Unnamed: 0', axis=1, inplace=True)
    df = df[~df['Просрочена, ч'].isnull()]
    df['Организация'] = df['Организация'].map(lambda item: item.replace('Филиал в городе ', ''))
    df.to_sql('doc', con=con, if_exists='append', index=False)


Doc.create_table()
con = sq.connect('test_task.db')

if os.path.exists('doc_tasks.csv'):
    print('Started instertion')
    dataframe_setup(con)
    FileHandler().remove()
    print('Insertion completed')
else:
    FileHandler().extract()
    print('Started instertion')
    dataframe_setup(con)
    FileHandler().remove()
    print('Insertion completed')

