from peewee import *

db = SqliteDatabase('test_task.db')


class Doc(Model):
    """
    Класс для описания модели таблицы
    """
    doc_type = CharField(null=True, column_name='Вид документа')
    doc_object = CharField(null=True, column_name='Объект')
    author = CharField(column_name='Автор')
    organization = CharField(column_name='Организация')
    performer = CharField(column_name='Исполнитель')
    task = CharField(null=True, column_name='Задача')
    date_issue = DateTimeField(null=True, column_name='Дата выдачи')
    date_completion_plan = DateTimeField(null=True, column_name='Дата выполнения (план)')
    date_completion_real = DateTimeField(null=True, column_name='Дата выполнения (факт)')
    overdue = FloatField(column_name='Просрочена, ч')
    resolution = CharField(null=True, column_name='Резолюция')
    auto_complete = CharField(null=True, column_name='Выполнена автоматически')
    schema = CharField(null=True, column_name='Договор по шаблону')
    state = CharField(null=True, column_name='Состояние')
    date = DateTimeField(null=True, column_name='Дата')
    date_completion = DateTimeField(null=True, column_name='Дата завершения')
    completed = BooleanField(null=True, column_name='Завершен')

    class Meta:
        database = db
