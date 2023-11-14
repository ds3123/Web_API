# coding : utf-8
# @Author : DS

from fastapi import Depends , APIRouter
from typing import List , Optional
from dao.schema import Customer_In , Customer_Out , Customer_Page
import service
from sqlalchemy.orm import Session
from dao.sql import get_db



router = APIRouter(
                     prefix       = "/customers" ,
                     tags         = [ "店家 _ 客戶" ] ,
                     # dependencies = [ Depends( verify_request_jwt_token ) ] ,  # JWT Token 驗證
                     responses    = { 404 : { "description": "Not found" } } ,
                  )


# 讀取 _ 特定店家，所有客戶
@router.get( '/' , summary = '所有客戶' , description = '讀取 _ 所有客戶' , response_model = Customer_Page )
def read_all_customers( page : int = 1 , db : Session = Depends( get_db ) ) :

    return service.read_all_customers( db , page )


# 讀取 _ 特定店家，所有客戶
@router.get( '/account/{account_id}' , summary = '特定店家所有客戶' , description = '讀取 _ 特定店家，所有客戶' , response_model = Customer_Page )
async def read_account_all_customers( account_id : str , page : int = 1 , db : Session = Depends( get_db ) , search : Optional[ str ] = None ) :

    return service.read_account_all_customers( db , account_id , page , search )


# 讀取 _ 特定客戶 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 客戶' , description = '以 id，查詢特定客戶' , response_model = Customer_Out )
async def read_customer_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_customer_by_id( id , db )


# 讀取 _ 特定店家，特定手機號碼客戶
@router.get( '/account/{account_id}/mobile/{mobile}' , summary = '特定店家，特定手機號碼客戶' , description = '讀取 _ 特定店家，特定手機號碼客戶' , response_model = List[ Customer_Out ] )
async def read_account_customer_by_mobile( account_id : str , mobile : str , db : Session = Depends( get_db ) ) :

    return service.read_account_customer_by_mobile( db , account_id , mobile )


# 新增 _ 客戶
@router.post( '/' , summary = '新增 _ 客戶' , description = '新增一筆客戶資料' , response_model = Customer_In )
async def create_customer( customer : Customer_In , db: Session = Depends( get_db ) ) :

    return service.create_customer( customer , db )


# 修改 _ 客戶
@router.put( '/{id}' , summary = '修改 _ 客戶' , description = '根據客戶資料表id，修改 _ 特定客戶資料' , response_model = Customer_In  )
async def update_customer_by_id( id : int , customer : Customer_In , db: Session = Depends( get_db ) ) :

    return service.update_customer_by_id( id , customer , db )



# 刪除 _ 客戶
@router.delete( '/{id}' , summary = '刪除 _ 客戶' , description = '根據客戶資料表id，刪除 _ 特定客戶資料'  )
async def delete_customer_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_customer_by_id( id , db )
