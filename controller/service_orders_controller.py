# coding : utf-8
# @Author : DS

from fastapi import Depends , APIRouter
from typing import List , Optional
from dao.schema import Service_Order_In , Service_Order_Out , Service_Order_Page
from sqlalchemy.orm import Session
from dao.sql import get_db
from util.auth import oauth2_employee
import service


router = APIRouter(
                     prefix       = "/service_orders" ,
                     tags         = [ "店家 _ 服務項目 : 訂單" ] ,
                     # dependencies = [ Depends(verify_request_jwt_token)],  # JWT Token 驗證
                     responses    = { 404 : { "description" : "Not found" }} ,
                  )


# 讀取 _ 所有服務項目 : 訂單
@router.get( '/' , summary = '所有服務項目 : 訂單' , description = '讀取 _ 所有服務項目 : 訂單' , response_model = Service_Order_Page )
#def read_all_service_orders( db : Session = Depends( get_db ) , token : str = Depends( oauth2_employee ) ) :
def read_all_service_orders( db : Session = Depends( get_db )  ) :

    return service.read_all_service_orders( db )



# 讀取 _ 特定店家，所有服務訂單
@router.get( '/account/{account_id}' , summary = '特定店家所有服務訂單' , description = '讀取 _ 特定店家，所有服務訂單' , response_model = Service_Order_Page )
def read_account_all_service_orders( account_id : str , page : int = 1 , db: Session = Depends( get_db ) , search : Optional[ str ] = None ) :

    return service.read_account_all_service_orders( db , account_id , page , search )



# 讀取 _ 特定店家，特定 [ 到店日期 ] _ 服務訂單
@router.get( '/account/{account_id}/service_date/{service_date}' , summary = '特定店家，特定 [ 到店日期 ]，所有服務訂單' , description = '讀取 _ 特定店家，特定 [ 到店日期 ]，所有服務訂單' , response_model = List[ Service_Order_Out ] )
def read_account_service_orders_by_service_date( account_id : str , service_date : str , db : Session = Depends( get_db ) ) :

    return service.read_account_service_orders_by_service_date( db , account_id , service_date )



# 讀取 _ 特定店家，特定 [ 付款日期 ] _ 服務訂單
@router.get( '/account/{account_id}/payment_date/{payment_date}' , summary = '特定店家，特定 [ 付款日期 ]，所有服務訂單' , description = '讀取 _ 特定店家，特定 [ 付款日期 ]，所有服務訂單' , response_model = List[ Service_Order_Out ] )
def read_account_service_orders_by_payment_date( account_id : str , payment_date : str , db : Session = Depends( get_db ) ) :

    return service.read_account_service_orders_by_payment_date( db , account_id , payment_date )


# 讀取 _ 特定服務項目 : 訂單 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 服務項目 : 訂單' , description = '以 id，查詢特定服務項目 : 訂單' , response_model = Service_Order_Out )
def read_service_order_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_service_order_by_id( id , db )


# 新增 _ 服務項目 : 訂單
@router.post( '/' , summary = '新增 _ 服務項目 : 訂單' , description = '新增一筆服務項目 : 訂單 資料' , response_model = Service_Order_Out  )
async def create_service_order( service_order : Service_Order_In , db : Session = Depends( get_db ) ) :

    return service.create_service_order( service_order , db )


# 修改 _ 服務項目 : 訂單
@router.put( '/{id}' , summary = '修改 _ 服務項目 : 訂單' , description = '根據服務項目 : 訂單資料表 id，修改 _ 特定服務項目 : 訂單' , response_model = Service_Order_Out )
def update_service_order_by_id( id : int , service_order : Service_Order_In  , db : Session = Depends( get_db ) ) :

    return service.update_service_order_by_id( id , service_order , db )


# 刪除 _ 服務項目 : 訂單
@router.delete( '/{id}' , summary = '刪除 _ 服務項目 : 訂單' , description = '根據服務項目 : 內容資料表 id，刪除 _ 特定服務項目 : 訂單'  )
async def delete_service_order_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_service_order_by_id( id , db )



