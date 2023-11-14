# coding : utf-8
# @Author : DS


from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Service_Order_In
from util import pagination
from typing import Optional
import dao



# 讀取 _ 所有服務項目 : 訂單
def read_all_service_orders( db : Session ) :

    # 讀取所有商品項目訂單
    service_orders = dao.read_all_service_orders( db )

    # 切片分頁
    service_orders = pagination( service_orders , 1 ) ;

    return service_orders


# 讀取 _ 特定店家，所有服務項目 : 訂單
def read_account_all_service_orders( db : Session , account_id : str , page : int , search : Optional[ str ] = None ) :

    # 讀取所有服務訂單
    db_service_orders  = dao.read_account_service_orders( db , account_id , search )

    # 分頁資料
    service_order_dict = pagination( db_service_orders , page )

    return service_order_dict


# 讀取 _ 特定店家，特定 [ 到店日期 ] _ 服務訂單
def read_account_service_orders_by_service_date( db : Session , account_id : str , service_date : str  ) :

    db_date_service_orders = dao.read_account_service_orders_by_service_date( db , account_id , service_date )

    return db_date_service_orders


# 讀取 _ 特定店家，特定 [ 付款日期 ] _ 服務訂單
def read_account_service_orders_by_payment_date( db : Session , account_id : str , payment_date : str  ) :

    db_date_service_orders = dao.read_account_service_orders_by_payment_date( db , account_id , payment_date )

    return db_date_service_orders


# 讀取 _ 特定服務項目 : 訂單 ( 依主鍵 id )
def read_service_order_by_id( id : int , db : Session ) :

    service_order = dao.read_service_order_by_id( id , db )

    if not service_order :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return service_order


# 新增 _ 服務項目 : 訂單
def create_service_order( service_order : Service_Order_In , db : Session ) :

    return dao.create_service_order( service_order , db )


# 修改 _ 服務項目 : 訂單
def update_service_order_by_id( id : int , service_order : Service_Order_In , db : Session ) :

    # 先查詢是否有該服務項目訂單
    db_service_order = dao.read_service_order_by_id( id , db )

    if not db_service_order :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_service_order_by_id( id , service_order , db )

    # 刷新，取得更新後的資料
    db.refresh( db_service_order )

    # 回傳 _ 更新、刷新後的資料
    return db_service_order


# 刪除 _ 服務項目 : 訂單
def delete_service_order_by_id( id : int , db : Session ) :

    dao.delete_service_order_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }



