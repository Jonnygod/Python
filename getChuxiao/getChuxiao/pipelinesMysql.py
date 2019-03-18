import time
import pymysql

class MysqlPipeline2(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        Gname = item['Gname']
        discount = item['cost']
        price = item['price']
        grade = item['grade']
        Data = today

        conn = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = '1234',
            db = 'Discount',
            charset = 'utf8')
        cur = conn.cursor()
        mysqlCmd = "insert into table1(Gname,discount,price,grade,timedate) values('%s','%s','%s','%s','%s');" %(Gname,discount,price,grade,Data)
        cur.execute(mysqlCmd)
        cur.close()
        conn.commit()
        conn.close()

        return item