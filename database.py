# from To_do_list_app import main as ad
import os
import pymysql as pyms
from dotenv import load_dotenv
load_dotenv()

dbPass = os.getenv("DB_PASS")

my_con = pyms.connect(host = '127.0.0.1', user = 'root', password = dbPass)
# print("Connection Successful")

my_cursor = my_con.cursor()