# coding : utf-8
# @Author : DS

import pymysql

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session



# 使用 pymysql 作為 MySQLdb
pymysql.install_as_MySQLdb()




# 建立 _ 資料庫引擎 ( 指定所要連結的 MySQL 資料庫 : gogopark_ts  )
#engine = create_engine( "mysql://root:root@localhost:8889/e_web" )


engine = create_engine( "mysql://dannyshih:Ds31230125@db-web-api.mysql.database.azure.com/e_web" )

#cnx = mysql.connector.connect(user="dannyshih", password="Ds31230125", host="db-web-api.mysql.database.azure.com", port=3306, database="e_web", ssl_ca="{ca-cert filename}", ssl_disabled=False)



# 建立 _ Session 類別
SessionLocal = sessionmaker( bind = engine )


# 依賴函式
async def get_db() :

    # 實體化 _ Session 類別，取得 _ 資料庫物件 ( 進行各種 CRUD )
    db : Session = SessionLocal()

    try :
        yield db

    finally :
        db.close()
