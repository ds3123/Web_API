# coding : utf-8
# @Author : DS

from pydantic import BaseModel
from typing import Optional , List , Any
from datetime import date , datetime
from .account_schema import Account_In
from .pet_schema import Pet_Out


'''

  @ 客戶

'''


# 前端 _ 參數
class Customer_In( BaseModel ) :

    account_id   : int
    name         : str
    sex          : str
    serial_id    : str
    mobile_phone : str

    tel_phone    : Optional[str]  = None
    address      : Optional[str]  = None
    birthday     : Optional[date] = None
    email        : Optional[str]  = None
    line         : Optional[str]  = None
    note         : Optional[str]  = None

    created_at   : Optional[ datetime ]   = None





# 後端 _ 資料庫
class Customer_Out( Customer_In ) :

    id : int

    # 關聯
    account : Optional[ Account_In ] = None  # 所屬店家帳號
    pet     : List[ Pet_Out ]         = []    # 所有寵物



# 後端 _ 資料庫 ( 分頁 )
class Customer_Page( BaseModel ) :

    per_page_data  : List[ Customer_Out ] = []
    page_btn_num   : int
    total_data_sum : int






