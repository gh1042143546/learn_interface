import pymysql
from Utils.config import Config

config_read = Config()
db_host = config_read.get('DBconfig')['host']
db_port = config_read.get('DBconfig')['port']
db_username = config_read.get('DBconfig')['username']
db_password = config_read.get('DBconfig')['password']
db_datebase = config_read.get('DBconfig')['database']
class DBManager:

    def __init__(self,host,port,username,password,db):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db = db
        self.conection = None
        self.cursor = None
        self.config = {
        'host': self.host,
        'port': self.port,
        'user': self.username,
        'passwd': self.password,
        'db': self.db,
    }
    #负责数据库连接，返回需要被管理的资源
    def __enter__(self):  #上下文管理器必须包括方法”__enter__()”和__exit__方法“
        self.conection = pymysql.connect(**self.config)
        self.cursor = self.conection.cursor()
        print("Connect DB successfully!")
        return self  #返回DBManager对象

    def excute_sql(self,sql,query_num='1'):
        res_num = self.cursor.execute(sql)
        if query_num == '1':
            res_one = self.cursor.fetchone()
            return (res_num,res_one)
        elif query_num == 'all':
            res_all = self.cursor.fetchall()
            return (res_num,res_all)

    #负责关闭数据库的连接，释放资源
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conection.close()
        print("db closed")

if __name__== "__main__":
    with DBManager(db_host,db_port,db_username,db_password,db_datebase) as db_client:
        a = db_client.excute_sql("select * from `purse_account` a where a.`mid`='9'")
        print(a[1])