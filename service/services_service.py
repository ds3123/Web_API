# coding : utf-8
# @Author : DS


from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Service_In
from util import pagination
import dao



# 讀取 _ 所有服務項目
def read_all_services( db : Session ) :

    # 讀取所有商品項目
    services = dao.read_all_services( db )

    # 切片分頁
    services = pagination( services , 1 ) ;

    return services


# 讀取 _ 特定店家，所有服務項目
def read_account_all_services( account_id : str , db : Session ) :

    db_services = dao.read_account_all_services( account_id , db )

    return db_services


# 讀取 _ 特定服務 ( 依主鍵 id )
def read_service_by_id( id : int , db : Session ) :

    service = dao.read_service_by_id( id , db )

    if not service :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return service



# 新增 _ 服務項目
def create_service( service : Service_In , db : Session ) :

    return dao.create_service( service , db )



# 修改 _ 服務項目
def update_service_by_id( id : int , service : Service_In, db : Session ) :

    # 先查詢是否有該服務項目
    db_service = dao.read_service_by_id( id , db )

    if not db_service :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_service_by_id( id , service , db )

    # 刷新，取得更新後的資料
    db.refresh( db_service )

    # 回傳 _ 更新、刷新後的資料
    return db_service


# 刪除 _ 服務項目
def delete_service_by_id( id : int , db : Session ) :

    dao.delete_service_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }