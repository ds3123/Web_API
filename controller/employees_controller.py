# coding : utf-8
# @Author : DS


from fastapi import Depends , APIRouter
from typing import List
from dao.schema import Employee_In , Employee_Out , Employee_Page
from sqlalchemy.orm import Session
from dao.sql import get_db
import service



router = APIRouter(
                     prefix       = "/employees" ,
                     tags         = [ "店家 _ 員工" ] ,
                     # dependencies = [ Depends( verify_request_jwt_token ) ] ,  # JWT Token 驗證
                     responses    = { 404 : { "description": "Not found" }} ,
                  )


# 讀取 _ 所有員工
@router.get( '/' , summary = '所有員工' , description = '讀取 _ 所有員工' , response_model = Employee_Page )
def read_all_employees( db : Session = Depends( get_db ) ) :

    return service.read_all_employees( db )


# 讀取 _ 特定員工 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 員工' , description = '以 id，查詢特定員工' , response_model = Employee_Out )
def read_employee_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.read_employee_by_id( id , db )

# 讀取 _ 特定員工 ( 依登入所輸入 ：帳號、密碼 )
@router.get( '/{account}/{password}' , summary = '讀取 _  特定員工 ( 依登入所輸入 ：帳號、密碼 )' , description = '以 帳號、密碼，查詢特定員工' , response_model = Employee_Out )
def read_employee_by_login( account : str , password : str , db: Session = Depends( get_db ) ) :

    return service.read_employee_by_login( account , password , db )


# 讀取 _ 特定店家，所有員工
@router.get( '/account/{account_id}' , summary = '特定店家，所有員工' , description = '讀取 _ 特定店家，所有員工' , response_model = List[ Employee_Out ] )
async def read_account_all_employees( account_id : str , db: Session = Depends( get_db ) ) :

    return service.read_account_all_employees( db , account_id )


# 新增 _ 員工
@router.post( '/' , summary = '新增 _ 員工' , description = '新增一筆員工資料' , response_model = Employee_In )
async def create_employee( employee : Employee_In , db: Session = Depends( get_db ) ) :

    return service.create_employee( employee , db )


# 修改 _ 員工
@router.put( '/{id}' , summary = '修改 _ 員工' , description = '根據員工資料表id，修改 _ 特定客戶資料' , response_model = Employee_In  )
async def update_employee_by_id( id : int , employee : Employee_In , db: Session = Depends( get_db ) ) :

    return service.update_employee_by_id( id , employee , db )


# 刪除 _ 員工
@router.delete( '/{id}' , summary = '刪除 _ 員工' , description = '根據員工資料表id，刪除 _ 特定客戶資料'  )
async def delete_employee_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_employee_by_id( id , db )
