# coding : utf-8
# @Author : DS

from pydantic import BaseModel
from typing import Union , Any , Optional , List
from datetime import date


# 客戶 _ 基礎 Model
class Customer_Base( BaseModel ) :

    account_id   : int
    name         : str
    sex          : str
    serial_id    : str
    mobile_phone : str
    tel_phone    : Optional[str]
    address      : Optional[str]

    birthday     : Optional[date]
    email        : Optional[str]
    line         : Optional[str]
    note         : Optional[str]

    created_at   : Any


# 檢驗 _ 前端 : 傳送參數
class Customer_In( Customer_Base ) :

    ...


# 檢驗 _ 後端 : 回傳資料
class Customer_Out( Customer_Base ) :

    id : int





