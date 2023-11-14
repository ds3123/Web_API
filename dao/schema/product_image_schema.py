# coding : utf-8
# @Author : DS


from pydantic import BaseModel

'''

  @ 商品項目 _ 圖片

'''


# 前端 _ 參數
class Product_Image_In( BaseModel ) :

    product_id : int
    url        : str


# 後端 _ 資料庫
class Product_Image_Out( Product_Image_In ) :

    id : int


