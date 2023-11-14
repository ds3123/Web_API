# coding : utf-8
# @Author : DS



from fastapi import Depends , APIRouter
from typing import List , Optional
from dao.schema import Service_Price_In , Service_Price_Out
from sqlalchemy.orm import Session
from dao.sql import get_db
import service


router = APIRouter(
                     prefix       = "/service_prices" ,
                     tags         = [ "店家 _ 服務項目 : 價格" ] ,
                   # dependencies = [ Depends( get_token_header ) ] ,
                     responses    = { 404 : { "description" : "Not found" }} ,
                  )


# 讀取 _ 所有服務項目 : 價格
@router.get( '/' , summary = '所有服務項目 : 價格' , description = '讀取 _ 所有服務項目 : 價格' , response_model = List[ Service_Price_Out ] )
async def read_all_service_prices( db : Session = Depends( get_db ) ) :

    return service.read_all_service_prices( db )


# 讀取 _ 特定服務項目 : 價格 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 服務項目 : 價格' , description = '以 id，查詢特定服務項目 : 價格' , response_model = Service_Price_Out )
async def read_service_price_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_service_price_by_id( id , db )


# 讀取 _ 特定條件 ( 第 1,2 層級分類 id  ) 服務項目 : 價格
@router.get( '/first_class_id/{first_id}/second_class_id/{second_id}' , summary = '讀取 _ 特定條件 ( 第 1,2 層級分類 id) 服務項目 : 價格' , description = '以第 1,2 層級分類 id，查詢特定服務項目 : 價格' , response_model = Service_Price_Out )
async def read_service_price_by_class_id( first_id : int , second_id : Optional[ int ] = None , db : Session = Depends( get_db ) ) :

    return service.read_service_price_by_class_id( db , first_id , second_id )


# 新增 _ 服務項目 : 價格
@router.post( '/' , summary = '新增 _ 服務項目 : 價格' , description = '新增一筆服務項目 : 價格資料' , response_model = Service_Price_Out )
async def create_service_price( service_price : Service_Price_In , db : Session = Depends( get_db ) ) :

    return service.create_service_price( service_price , db )


# 修改 _ 服務項目 : 價格
@router.put( '/{id}' , summary = '修改 _ 服務項目 : 價格' , description = '根據服務項目 : 價格資料表 id，修改 _ 特定服務項目 : 價格' , response_model = Service_Price_Out )
async def update_service_price_by_id( id : int , service_price : Service_Price_In  , db : Session = Depends( get_db ) ) :

    return service.update_service_price_by_id( id , service_price , db )


# 刪除 _ 服務項目 : 價格
@router.delete( '/{id}' , summary = '刪除 _ 服務項目 : 價格' , description = '根據服務項目 : 內容 資料表 id，刪除 _ 特定服務項目 : 價格'  )
async def delete_service_price_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_service_price_by_id( id , db )
