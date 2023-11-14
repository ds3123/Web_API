# coding : utf-8
# @Author : DS

from fastapi import Depends , APIRouter
from typing import List
from dao.schema import Product_In , Product_Out , Product_Page
from sqlalchemy.orm import Session
from dao.sql import get_db
import service

router = APIRouter(
                     prefix       = "/products" ,
                     tags         = [ "店家 _ 商品項目" ] ,
                   # dependencies = [ Depends( get_token_header ) ] ,
                     responses    = { 404 : { "description" : "Not found" }} ,
                  )


# 讀取 _ 所有商品項目
@router.get( '/' , summary = '所有商品項目' , description = '讀取 _ 所有商品項目' , response_model = Product_Page )
async def read_all_products( db : Session = Depends( get_db ) ) :

    return service.read_all_products( db )


# 讀取 _ 特定商品項目 : 價格 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 商品項目' , description = '以 id，查詢特定商品項目' , response_model = Product_Out )
async def read_product_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_product_by_id( id , db )


# 新增 _ 商品項目
@router.post( '/' , summary = '新增 _ 商品項目' , description = '新增一筆商品項目資料' , response_model = Product_Out )
async def create_product( product : Product_In , db : Session = Depends( get_db ) ) :

    return service.create_product( product , db )


# 修改 _ 商品項目
@router.put( '/{id}' , summary = '修改 _ 商品項目' , description = '根據商品項目資料表 id，修改 _ 特定商品項目' , response_model = Product_Out  )
async def update_product_by_id( id : int , product : Product_In , db : Session = Depends( get_db ) ) :

    return service.update_product_by_id( id , product , db )


# 刪除 _ 商品項目
@router.delete( '/{id}' , summary = '刪除 _ 商品項目' , description = '根據商品項目資料表 id，刪除 _ 特定商品項目' )
async def delete_product_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_product_by_id( id , db )








