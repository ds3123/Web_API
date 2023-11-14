# coding : utf-8
# @Author : DS


from fastapi import Depends , APIRouter
from typing import List , Optional
from dao.schema import Service_Content_In , Service_Content_Out
from sqlalchemy.orm import Session
from dao.sql import get_db
import service


router = APIRouter(
                     prefix       = "/service_contents" ,
                     tags         = [ "店家 _ 服務項目 : 內容" ] ,
                     # dependencies = [ Depends( verify_request_jwt_token ) ] ,  # JWT Token 驗證
                     responses    = { 404 : { "description" : "Not found" }} ,
                  )


# 讀取 _ 所有服務項目 : 內容
@router.get( '/' , summary = '所有服務項目 : 內容 ' , description = '讀取 _ 所有服務項目 : 內容 ' , response_model = List[ Service_Content_Out ]  )
async def read_all_service_contents( db : Session = Depends( get_db ) ) :

    return service.read_all_service_contents( db )


# 讀取 _ 特定服務項目 : 內容 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 服務項目 : 內容 ' , description = '以 id，查詢特定服務項目 : 內容 ' , response_model = Service_Content_Out )
async def read_service_content_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_service_content_by_id( id , db )


# 新增 _ 服務項目 : 內容
@router.post( '/' , summary = '新增 _ 服務項目 : 內容 ' , description = '新增一筆服務項目 : 內容 資料' , response_model = Service_Content_Out )
async def create_service_content( service_content : Service_Content_In , db : Session = Depends( get_db ) ) :

    return service.create_service_content( service_content , db )



# 修改 _ 服務項目 : 內容
@router.put( '/{id}' , summary = '修改 _ 服務項目 : 內容 ' , description = '根據服務項目 : 內容 資料表 id，修改 _ 特定服務項目 : 內容 ' , response_model = Service_Content_Out  )
async def update_service_content_by_id( id : int , service_content : Service_Content_In , db : Session = Depends( get_db ) ) :

    return service.update_service_content_by_id( id , service_content , db )


# 刪除 _ 服務項目 : 內容
@router.delete( '/{id}' , summary = '刪除 _ 服務項目 : 內容 ' , description = '根據服務項目 : 內容 資料表 id，刪除 _ 特定服務項目 : 內容 '  )
async def delete_service_content_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_service_content_by_id( id , db )

