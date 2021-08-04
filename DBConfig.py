
import pymysql

class DatabaseUtil:

    conn = None

    @staticmethod
    def get_mysql_connection():
        if DatabaseUtil.conn==None:
            conn = pymysql.connect("localhost","root","root","persist")#ack -- handshaking
        return conn

