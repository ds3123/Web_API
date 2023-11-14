# coding : utf-8
# @Author : DS


from pydantic import BaseModel
from typing import List , Optional
from datetime import date
from .account_schema import Account_In
from .customer_schema import Customer_In
from .pet_schema import Pet_In
from .service_schema import Service_In


'''

  @ 前後端檢驗 : 服務項目 _ 訂單

'''


# 前端 _ 參數
class Service_Order_In( BaseModel ) :

    account_id     : int
    customer_id    : int
    pet_id         : int
    service_id     : int

    service_type   : str
    service_date   : date
    arrival_time   : Optional[ str ] = None

    service_price  : int

    adjust_amount  : Optional[ int ] = None
    adjust_reason  : Optional[ str ] = None

    amount_paid    : int

    payment_method : str
    payment_date   : date

    service_note   : Optional[ str ] = None

    shop_status    : str


# 後端 _ 資料庫
class Service_Order_Out( Service_Order_In ) :

    id       : int

    # 關聯欄位
    account  : Account_In  # 所屬店家
    customer : Customer_In # 所屬店家客人
    pet      : Pet_In      # 所屬店家寵物
    service  : Service_In  # 所屬店家服務


# 後端 _ 資料庫 ( 分頁 )
class Service_Order_Page( BaseModel ) :

    per_page_data  : List[ Service_Order_Out ] = []
    page_btn_num   : int
    total_data_sum : int

