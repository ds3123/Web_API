# coding : utf-8
# @Author : DS


from fastapi import Depends , APIRouter
from typing import List
from dao.schema import Product_Image_In , Product_Image_Out
from sqlalchemy.orm import Session
from dao.sql import get_db
import service


router = APIRouter(
                     prefix       = "/product_images" ,
                     tags         = [ "店家 _ 商品項目 : 圖片" ] ,
                   # dependencies = [ Depends( get_token_header ) ] ,
                     responses    = { 404 : { "description" : "Not found" }} ,
                  )



# 讀取 _ 所有商品項目 : 圖片
@router.get( '/' , summary = '所有商品項目 : 圖片' , description = '讀取 _ 所有商品項目 : 圖片' , response_model = List[ Product_Image_Out ] )
async def read_all_product_images( db : Session = Depends( get_db ) ) :

    return service.read_all_product_images( db )


# 讀取 _ 特定商品項目 : 圖片 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 商品項目 : 圖片' , description = '以 id，查詢特定商品項目 : 圖片' , response_model = Product_Image_Out )
async def read_product_image_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_product_image_by_id( id , db )



# 新增 _ 商品項目 : 圖片
@router.post( '/' , summary = '新增 _ 商品項目 : 圖片' , description = '新增一筆商品項目 : 圖片資料' , response_model = Product_Image_Out )
async def create_product_image( product_image : Product_Image_In , db : Session = Depends( get_db ) ) :

    return service.create_product_image( product_image , db )


# 修改 _ 商品項目 : 圖片
@router.put( '/{id}' , summary = '修改 _ 商品項目: 圖片' , description = '根據商品項目資料表 id，修改 _ 特定商品項目: 圖片' , response_model = Product_Image_Out  )
async def update_product_image_by_id( id : int , product_image : Product_Image_In , db : Session = Depends( get_db ) ) :

    return service.update_product_image_by_id( id , product_image , db )


# 刪除 _ 商品項目 : 圖片
@router.delete( '/{id}' , summary = '刪除 _ 商品項目:圖片' , description = '根據商品項目資料表 id，刪除 _ 特定商品項目:圖片'  )
async def delete_product_image_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_product_image_by_id( id , db )
