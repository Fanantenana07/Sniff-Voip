from PyQt5.QtSql import QSqlDatabase
import os

def connection():
    directory = str(os.getcwd()).replace('\\','/')+"/Database/database.db"
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(directory)
    return db