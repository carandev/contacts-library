import pymysql.cursors

def connect():
    return pymysql.connect(host='localhost',
                             user='root',
                             password='admin',
                             database='contacts_db',
                             cursorclass=pymysql.cursors.DictCursor)