# coding : utf-8
# @Author : DS


from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Service_Content_In
from util import pagination
import dao



# 讀取 _ 所有服務項目 : 內容
def read_all_service_contents( db : Session ) :

    db_service_contents = dao.read_all_service_contents( db )

    return db_service_contents


# 讀取 _ 特定服務項目 : 內容 ( 依主鍵 id )
def read_service_content_by_id( id : int , db : Session ) :

    service_content = dao.read_service_content_by_id( id , db )

    if not service_content :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return service_content


# 新增 _ 服務項目 : 內容
def create_service_content( service_content : Service_Content_In , db : Session ) :

    return dao.create_service_content( service_content , db )


# 修改 _ 服務項目 : 內容
def update_service_content_by_id( id : int , service_content : Service_Content_In , db : Session ) :

    # 先查詢是否有該服務項目
    db_service_content = dao.read_service_content_by_id( id , db )

    if not db_service_content :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_service_content_by_id( id , service_content , db )

    # 刷新，取得更新後的資料
    db.refresh( db_service_content )

    # 回傳 _ 更新、刷新後的資料
    return db_service_content


# 刪除 _ 服務項目 : 內容
def delete_service_content_by_id( id : int , db : Session ) :

    dao.delete_service_content_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }
