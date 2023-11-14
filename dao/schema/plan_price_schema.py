# coding : utf-8
# @Author : DS

from pydantic import BaseModel
from typing import Optional
from .plan_schema import Plan_In

'''

  @ 方案項目 _ 價格

'''


# 前端 _ 參數
class Plan_Price_In( BaseModel ) :

    plan_id         : int
    plan_content_id : Optional[ int ] = None

    price           : int


# 後端 _ 資料庫
class Plan_Price_Out( Plan_Price_In ) :

    id   : int

    # 關聯欄位
    plan : Plan_In  # 方案