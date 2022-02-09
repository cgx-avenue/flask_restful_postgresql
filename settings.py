'''
Author: your name
Date: 2021-11-17 14:12:57
LastEditTime: 2021-11-23 10:07:57
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \flask_restful_postgresql\settings.py
'''
from dotenv import load_dotenv
import os
load_dotenv(verbose=True,override=True)

DEBUG=True
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))  # python-dotenv不能自动转换类型，需添加转换
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

P_DB_URI=os.getenv("P_DB_URI")
