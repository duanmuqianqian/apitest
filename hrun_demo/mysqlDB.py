# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/17 5:36 下午
@Auth ： duanmu
@File ：mysqlDB.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import pymysql
from hrun_demo.config.readConfig import ReadConfig

mysql=ReadConfig()
class MysqlDb:
    def __init__(self):
        self.host=mysql.Database("host")
        self.user=mysql.Database("user")
        self.passwd=mysql.Database("passwd")
        self.database=mysql.Database("database")
        self.db=pymysql.connect(self.host,self.user,self.passwd,self.database,charset="utf8")

    def execute(self,sql,data):
        connect=self.db
        cursor=connect.cursor()
        cursor.execute(sql%data)
        connect.commit()


    def execute_read(self,sql,data):
        connect=self.db
        cursor=connect.cursor()
        cursor.execute(sql%data)
        for row in cursor.fetchall():
            return row

    def last_content(self):
        sql=mysql.Mysql("last_content")
        data=self.execute_read(sql,())
        return data



