# coding : utf-8
# @Author : DS

from pydantic import BaseModel
from typing import Optional , List
from .account_schema import Account_In

'''

  @ 方案項目

'''


# 方案項目：內容
class Plan_Content( BaseModel ) :

    plan_id : int
    content : str


# 前端 _ 參數
class Plan_In( BaseModel ) :

    account_id : int

    name       : str
    count      : int
    period     : int
    note       : Optional[ str ] = None


# 後端 _ 資料庫
class Plan_Out( Plan_In ) :

    id: int

    # 關聯欄位
    account      : Account_In            # 所屬店家
    plan_content : List[ Plan_Content ]  # 方案 _ 內容 ( 項目 )

# 後端 _ 資料庫 ( 分頁 )
class Plan_Page( BaseModel ) :

    per_page_data  : List[ Plan_Out ] = []
    page_btn_num   : int
    total_data_sum : int



