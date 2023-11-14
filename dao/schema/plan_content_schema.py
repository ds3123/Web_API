# coding : utf-8
# @Author : DS

from pydantic import BaseModel
from .plan_schema import Plan_In


'''

  @ 方案項目 _ 內容 ( 選項 )

'''


# 前端 _ 參數
class Plan_Content_In( BaseModel ) :

    plan_id : int
    content : str


# 後端 _ 資料庫
class Plan_Content_Out( Plan_Content_In ) :

    id   : int

    # 關聯欄位
    plan : Plan_In  # 所屬 _ 方案項目




