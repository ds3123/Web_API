# coding : utf-8
# @Author : DS

from pydantic import BaseModel
from typing import List , Optional
from datetime import date , datetime
from .account_schema import Account_In

'''

  @ 寵物

'''

class Customer( BaseModel ) :

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



# --------------


# 前端 _ 參數
class Pet_In( BaseModel ) :

    account_id    : int
    customer_id   : int

    name          : str
    serial        : str
    chip          : Optional[ str ]   = None

    pet_class     : str
    pet_species   : Optional[ str ]   = None

    sex           : str
    weight        : Optional[ str ]   = None
    color         : Optional[ str ]   = None
    birthday      : Optional[ date ]  = None

    note          : Optional[ str ]   = None

    is_dead       : Optional[ int ]     = 0
    is_rejected   : Optional[ int ]     = 0
    reject_reason : Optional[ str ]     = None

    created_at    : Optional[ datetime ] = None

# 後端 _ 資料庫
class Pet_Out( Pet_In ) :

    id: int

    # 關聯
    account       : Account_In  # 所屬店家
    customer      : Customer    # 寵物主人
    # service_order : Any  # 相關服務訂單


# 後端 _ 資料庫 ( 分頁 )
class Pet_Page( BaseModel ) :

    per_page_data  : List[ Pet_Out ] = []
    page_btn_num   : int
    total_data_sum : int
