# coding : utf-8
# @Author : DS
from pydantic import BaseModel
from typing import Optional , List
from datetime import date
from .account_schema import Account_In
from .customer_schema import Customer_In
from .product_schema import Product_In

'''

  @ 商品項目 _ 訂單

'''

# 前端 _ 參數
class Product_Order_In( BaseModel ) :

    account_id     : int
    customer_id    : int
    product_id     : int

    order_quantity : int
    payment_amount : int
    payment_method : str
    payment_date   : Optional[ date ] = None



# 後端 _ 資料庫
class Product_Order_Out( Product_Order_In ) :

    id       : int

    # 關聯欄位
    account  : Account_In  # 所屬店家
    customer : Customer_In # 所屬客戶
    product  : Product_In  # 所屬商品



# 後端 _ 資料庫 ( 分頁 )
class Product_Order_Page( BaseModel ) :

    per_page_data  : List[ Product_Order_Out ] = []
    page_btn_num   : int
    total_data_sum : int



