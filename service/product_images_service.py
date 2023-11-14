# coding : utf-8
# @Author : DS

from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Product_Image_In
import dao


# 讀取 _ 所有商品項目 : 圖片
def read_all_product_images( db : Session ) :

    db_product_images = dao.read_all_product_images( db )

    return db_product_images


# 讀取 _  特定商品項目 : 圖片 ( 依主鍵 id )
def read_product_image_by_id( id : int , db : Session ) :

    product_image = dao.read_product_image_by_id( id , db )

    if not product_image :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return product_image


# 新增 _ 商品項目 : 圖片
def create_product_image( product_image : Product_Image_In , db : Session ) :

    return dao.create_product_image( product_image , db )


# 修改 _ 商品項目 : 圖片
def update_product_image_by_id( id : int , product_image : Product_Image_In , db : Session ) :

    # 先查詢是否有該商品項目
    db_product_image = dao.read_product_image_by_id( id , db )

    if not db_product_image :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_product_image_by_id( id , product_image , db )

    # 刷新，取得更新後的資料
    db.refresh( db_product_image )

    # 回傳 _ 更新、刷新後的資料
    return db_product_image


# 刪除 _ 商品項目 : 圖片
def delete_product_image_by_id( id : int , db : Session ) :

    dao.delete_product_image_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }


