# coding : utf-8
# @Author : DS

from pydantic import BaseModel
from typing import List
from .account_schema import Account_In



'''

  @ 服務項目

'''


# 前端 _ 參數
class Service_In( BaseModel ) :

    account_id : int
    name       : str


# 後端 _ 資料庫
class Service_Out( Service_In ) :

    id: int


    # 關聯欄位
    account : Account_In  # 所屬店家

    # service_content: Any  # 服務 _ 內容 ( 項目 )
    # service_order: Any  # 服務 _ 訂單
    # service_price: Any  # 服務 _ 價格


# 後端 _ 資料庫 ( 分頁 )
class Service_Page( BaseModel ) :

    per_page_data  : List[ Service_Out ] = []
    page_btn_num   : int
    total_data_sum : int

