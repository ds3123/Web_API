# coding : utf-8
# @Author : DS

from pydantic import BaseModel
from typing import Optional
from datetime import date
from .service_schema import Service_In


'''

  @ 服務項目 _ 內容 ( 選項 )

'''


# 前端 _ 參數
class Service_Content_In( BaseModel ) :

    service_id : int
    content    : str


# 後端 _ 資料庫
class Service_Content_Out( Service_Content_In ) :

    id : int

    # 關聯欄位
    service : Service_In  # 所屬 _ 服務項目
