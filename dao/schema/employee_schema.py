# coding : utf-8
# @Author : DS

from pydantic import BaseModel
from typing import Optional , List
from datetime import date , datetime
from .account_schema import Account_In



'''

  @ 員工

'''

# 前端 _ 參數
class Employee_In( BaseModel ) :

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

    created_at      : Optional[datetime] = None


# 後端 _ 資料庫
class Employee_Out( Employee_In ) :

    id : int

    # 關聯
    shop_account: Optional[ Account_In ] = None  # 所屬店家帳號


# 後端 _ 資料庫 ( 分頁 )
class Employee_Page( BaseModel ) :

    per_page_data  : List[ Employee_Out ] = []
    page_btn_num   : int
    total_data_sum : int

# 後端 _ 登入授權
class Employee_Authorization( BaseModel ) :

    account  : str
    password : str






