# coding : utf-8
# @Author : DS

import pymysql
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from dotenv import load_dotenv


# 下載環境變數
load_dotenv()


# 使用 pymysql 作為 MySQLdb
pymysql.install_as_MySQLdb()

username = os.getenv( 'DB_USERNAME' )
password = os.getenv( 'DB_PASSWORD' )
host     = os.getenv( 'DB_HOST' )
database = os.getenv( 'DB_DATABASE' )


# 建立 _ 資料庫引擎 ( 指定所要連結的 MySQL 資料庫 : gogopark_ts  )
engine = create_engine( f"mysql://{ username }:{ password }@{ host }/{ database }" )




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
