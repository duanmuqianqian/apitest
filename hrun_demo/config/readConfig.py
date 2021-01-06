# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/17 4:56 下午
@Auth ： duanmu
@File ：readConfig.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import os
import codecs
import configparser

class ReadConfig:
    def __init__(self):
        self.cf=configparser.ConfigParser()  #实例化cionfigparser对象
        #获取当前文件夹的父目录绝对路径
        self.path =os.path.dirname(os.path.dirname(__file__))
        #获取config文件夹中的ini文件
        self.file_path=os.path.join(self.path,'config','config.ini')
        #读取ini文件
        self.cf.read(self.file_path,encoding='utf-8')

    def Mysql(self,name):
        value=self.cf.get("Mysql",name)
        return value

    def Database(self,name):
        value=self.cf.get("DATABASE",name)
        return value

