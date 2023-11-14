# coding : utf-8
# @Author : DS


from pydantic import BaseModel
from typing import Optional
from datetime import date
from .service_schema import Service_In


'''

  @ 服務項目 _ 價格

'''


# 前端 _ 參數
class Service_Price_In( BaseModel ) :

    service_id         : int
    service_content_id : Optional[ int ] = None

    price              : int


# 後端 _ 資料庫
class Service_Price_Out( Service_Price_In ) :

    id      : int

    # 關聯欄位
    service : Service_In  # 服務 _ 項目




