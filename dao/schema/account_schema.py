# coding : utf-8
# @Author : DS

from pydantic import BaseModel
from typing import Optional , List
from datetime import date , datetime


'''

  @ 帳號
  
  NOTE :
       以下的客戶( Customer )與 員工( Employee ) 模型，不直接從 customer_schema.py , employee_schema.py 匯入
       因其各自也有匯入 Account_In ，為避免 循環匯入 ( circular import ) 問題，在此檔案另行定義

'''


# 員工
class Employee( BaseModel ) :

    id              : Optional[int] = None

    account_id      : int

    account         : str
    password        : str

    name            : str
    sex             : str
    serial_id       : str
    mobile_phone    : str

    tel_phone       : Optional[str]  = None
    nickname        : Optional[str]  = None
    birthday        : Optional[date] = None

    line            : Optional[str]  = None
    email           : Optional[str]  = None
    address         : Optional[str]  = None

    salary_type     : Optional[str]  = None
    position_type   : Optional[str]  = None
    position_status : Optional[str]  = None

    created_at      : Optional[datetime]   = None

# 客戶
class Customer( BaseModel ) :

    id           : Optional[int] = None

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


# ------------

# 前端 _ 參數
class Account_In( BaseModel ) :

    county     : str
    district   : str
    zipcode    : str

    serial     : str

    shop_brand : str
    shop_name  : str
    shop_owner : str

    auth_level : Optional[ str ]      = None

    created_at : Optional[ datetime ] = None



# 後端 _ 資料庫
class Account_Out( Account_In ) :

    id       : int

    # 關聯
    employee : Optional[ List[ Employee ] ] = None  # 所有員工
    customer : Optional[ List[ Customer ] ] = None  # 所有客戶


# 後端 _ 資料庫 ( 分頁 )
class Account_Page( BaseModel ) :

    per_page_data  : List[ Account_Out ] = []
    page_btn_num   : int
    total_data_sum : int

