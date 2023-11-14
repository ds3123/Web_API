# coding : utf-8
# @Author : DS


from fastapi import Depends , APIRouter
from typing import List
from dao.schema import Product_Order_In , Product_Order_Out , Product_Order_Page
from sqlalchemy.orm import Session
from dao.sql import get_db
import service


router = APIRouter(
                     prefix       = "/product_orders" ,
                     tags         = [ "店家 _ 商品項目 : 訂單" ] ,
                   # dependencies = [ Depends( get_token_header ) ] ,
                     responses    = { 404 : { "description" : "Not found" }} ,
                  )


# 讀取 _ 所有商品項目 : 訂單
@router.get( '/' , summary = '所有商品項目 : 訂單' , description = '讀取 _ 所有商品項目 : 訂單' , response_model = Product_Order_Page )
async def read_all_product_orders( db : Session = Depends( get_db ) ) :

    return service.read_all_product_orders( db )


# 讀取 _ 特定條件 ( id ) 商品項目 : 訂單
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 商品項目 : 訂單' , description = '以 id，查詢特定商品項目 : 訂單' , response_model = Product_Order_Out )
async def read_product_order_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_product_order_by_id( id , db )


# 新增 _ 商品項目 : 訂單
@router.post( '/' , summary = '新增 _ 商品項目 : 訂單' , description = '新增一筆商品項目 : 訂單資料' , response_model = Product_Order_Out )
async def create_product_order( product_order : Product_Order_In , db : Session = Depends( get_db ) ) :

    return service.create_product_order( product_order , db )


# 修改 _ 商品項目 : 訂單
@router.put( '/{id}' , summary = '修改 _ 商品項目 : 訂單' , description = '根據商品項目訂單資料表 id，修改 _ 特定商品項目 : 訂單' , response_model = Product_Order_Out  )
async def update_product_order_by_id( id : int , product_order : Product_Order_In , db : Session = Depends( get_db ) ) :

    return service.update_product_order_by_id( id , product_order , db )


# 刪除 _ 商品項目 : 訂單
@router.delete( '/{id}' , summary = '刪除 _ 商品項目 : 訂單' , description = '根據商品項目訂單資料表 id，刪除 _ 特定商品項目 : 訂單' )
async def delete_product_order_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_product_order_by_id( id , db )
