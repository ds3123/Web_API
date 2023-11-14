# coding : utf-8
# @Author : DS


from fastapi import Depends , APIRouter
from typing import List , Optional
from dao.schema import Account_In , Account_Out , Account_Page
from sqlalchemy.orm import Session
from dao.sql import get_db
import service


router = APIRouter(
                     prefix       = "/accounts" ,
                     tags         = [ "店家 _ 帳號" ] ,
                     # dependencies = [ Depends( verify_request_jwt_token ) ] ,
                     responses    = { 404 : { "description" : "Not found" } } ,
                  )


# 讀取 _ 所有店家帳號
@router.get( '/' , summary = '所有店家帳號' , description = '讀取 _ 所有店家帳號' , response_model = Account_Page )
def read_all_accounts( page : int = 1 , db: Session = Depends( get_db ) ) :

    return service.read_all_accounts( db , page )


# 讀取 _ 特定帳戶 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 店家帳戶' , description = '以 id，查詢特定店家帳戶' , response_model = Account_Out )
async def read_account_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.read_account_by_id( id , db )



# 讀取 _ 特定條件 : 郵遞區號 店家帳號
@router.get( '/zipcode/{zipcode}' , summary = '讀取 _ 特定條件 : 郵遞區號 店家帳號' , description = '以 zipcode，查詢店家帳戶' , response_model = List[ Account_Out ] )
async def read_accounts_by_zipcode( zipcode : str , db: Session = Depends( get_db ) ) :

    return service.read_accounts_by_zipcode( zipcode , db )



# 新增 _ 店家帳號
@router.post( '/' , summary = '新增 _ 店家帳號' , description = '新增一筆店家帳號資料' , response_model = Account_In )
async def create_account( account : Account_In , db: Session = Depends( get_db ) ) :

    return service.create_account( account , db )


# 修改 _ 店家帳號
@router.put( '/{id}' , summary = '修改 _ 店家帳號' , description = '根據店家帳號資料表id，修改 _ 特定店家帳號' , response_model = Account_In  )
async def update_account_by_id( id : int , account : Account_In , db: Session = Depends( get_db ) ) :

    return service.update_account_by_id( id , account , db )


# 刪除 _ 店家帳號
@router.delete( '/{id}' , summary = '刪除 _ 店家帳號' , description = '根據店家帳號資料表id，刪除 _ 特定店家帳號'  )
async def delete_account_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_account_by_id( id , db )