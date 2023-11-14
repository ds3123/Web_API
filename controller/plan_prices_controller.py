# coding : utf-8
# @Author : DS


from fastapi import Depends , APIRouter
from typing import List , Optional
from dao.schema import Plan_Price_In , Plan_Price_Out
from sqlalchemy.orm import Session
from dao.sql import get_db
import service


router = APIRouter(
                     prefix       = "/plan_prices" ,
                     tags         = [ "店家 _ 方案 : 價格" ] ,
                     # dependencies = [Depends(verify_request_jwt_token)],  # JWT Token 驗證
                     responses    = { 404 : { "description" : "Not found" }} ,
                  )



# 讀取 _ 所有方案項目 : 價格
@router.get( '/' , summary = '所有方案項目 : 價格' , description = '讀取 _ 所有方案項目 : 價格' , response_model = List[ Plan_Price_Out ] )
async def read_all_plan_prices( db : Session = Depends( get_db ) ) :

    return service.read_all_plan_prices( db )


# 讀取 _ 特定自訂方案 : 價格 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 方案項目 : 價格' , description = '以 id，查詢特定方案項目 : 價格' , response_model = Plan_Price_Out )
async def read_plan_price_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_plan_price_by_id( id , db )



# 讀取 _ 特定條件 ( 第 1,2 層級分類 id  ) 方案項目 : 價格
@router.get( '/first_class_id/{first_id}/second_class_id/{second_id}' , summary = '讀取 _ 特定條件 ( 第 1,2 層級分類 id) 方案項目 : 價格' , description = '以第 1,2 層級分類 id，查詢特定方案項目 : 價格'  )
async def read_plan_price_by_class_id( first_id : int , second_id : Optional[ int ] = None , db : Session = Depends( get_db ) ) :

    return service.read_plan_price_by_class_id( db , first_id , second_id )



# 新增 _ 方案項目 : 價格
@router.post( '/' , summary = '新增 _ 方案項目 : 價格' , description = '新增一筆方案項目 : 價格資料' , response_model = Plan_Price_Out )
async def create_plan_price( plan_price : Plan_Price_In , db : Session = Depends( get_db ) ) :

    return service.create_plan_price( plan_price , db )


# 修改 _ 方案項目 : 價格
@router.put( '/{id}' , summary = '修改 _ 方案項目 : 價格' , description = '根據方案項目 : 價格資料表 id，修改 _ 特定方案項目 : 價格' , response_model = Plan_Price_Out )
async def update_plan_price_by_id( id : int , plan_price : Plan_Price_In  , db : Session = Depends( get_db ) ) :

    return service.update_plan_price_by_id( id , plan_price , db )


# 刪除 _ 方案項目 : 價格
@router.delete( '/{id}' , summary = '刪除 _ 方案項目 : 價格' , description = '根據方案項目 : 內容 資料表 id，刪除 _ 特定方案項目 : 價格'  )
async def delete_plan_price_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_plan_price_by_id( id , db )





