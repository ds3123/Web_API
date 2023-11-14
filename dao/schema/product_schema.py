# coding : utf-8
# @Author : DS

from pydantic import BaseModel
from typing import List , Optional
from datetime import date
from .product_image_schema import Product_Image_In

'''

  @ 商品項目

'''

# 商品訂單
class Product_Order( BaseModel ) :

    account_id     : int
    customer_id    : int
    product_id     : int

    order_quantity : int
    payment_amount : int
    payment_method : str
    payment_date   : Optional[ date ] = None


# 前端 _ 參數
class Product_In( BaseModel ) :

    account_id : int
    name       : str
    type       : str
    stock      : int
    unit_price : int


# 後端 _ 資料庫
class Product_Out( Product_In ) :

    id             : int

    # 關聯欄位
    product_images : List[ Product_Image_In ] # 商品圖片
    product_order  : List[ Product_Order ]    # 商品訂單


# 後端 _ 資料庫 ( 分頁 )
class Product_Page( BaseModel ) :

    per_page_data  : List[ Product_Out ] = []
    page_btn_num   : int
    total_data_sum : int



