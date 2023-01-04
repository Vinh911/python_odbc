import pyodbc

def getConn ():
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          "Server=xxx.xx.x.xx;"
                          "Database=xxx;"
                          "uid=xxx;pwd=xxx")
    return cnxn
