# coding : utf-8
# @Author : DS


from fastapi import Depends , APIRouter
from typing import List
from dao.schema import Plan_Content_In , Plan_Content_Out
from sqlalchemy.orm import Session
from dao.sql import get_db
import service


router = APIRouter(
                     prefix       = "/plan_contents" ,
                     tags         = [ "店家 _ 自訂方案 : 內容" ] ,
                     #dependencies = [ Depends( verify_request_jwt_token ) ] ,  # JWT Token 驗證
                     responses    = { 404 : { "description" : "Not found" }} ,
                  )


# 讀取 _ 所有自訂方案 : 內容
@router.get( '/' , summary = '所有自訂方案 : 內容 ' , description = '讀取 _ 所有自訂方案 : 內容 ' , response_model = List[ Plan_Content_Out ]  )
async def read_all_plan_contents( db : Session = Depends( get_db ) ) :

    return service.read_all_plan_contents( db )



# 讀取 _ 特定自訂方案 : 內容 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 自訂方案 : 內容 ' , description = '以 id，查詢特定自訂方案 : 內容 ' , response_model = Plan_Content_Out )
async def read_plan_content_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_plan_content_by_id( id , db )



# 新增 _ 自訂方案 : 內容
@router.post( '/' , summary = '新增 _ 自訂方案 : 內容 ' , description = '新增一筆自訂方案 : 內容 資料' , response_model = Plan_Content_Out )
async def create_plan_content( plan_content : Plan_Content_In , db : Session = Depends( get_db ) ) :

    return service.create_plan_content( plan_content , db )


# 修改 _ 自訂方案 : 內容
@router.put( '/{id}' , summary = '修改 _ 自訂方案 : 內容 ' , description = '根據自訂方案 : 內容 資料表 id，修改 _ 特定自訂方案 : 內容 ' , response_model = Plan_Content_Out  )
async def update_plan_content_by_id( id : int , plan_content : Plan_Content_In , db : Session = Depends( get_db ) ) :

    return service.update_plan_content_by_id( id , plan_content , db )


# 刪除 _ 自訂方案 : 內容
@router.delete( '/{id}' , summary = '刪除 _ 自訂方案 : 內容 ' , description = '根據自訂方案 : 內容 資料表 id，刪除 _ 特定自訂方案 : 內容 '  )
async def delete_plan_content_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_plan_content_by_id( id , db )




