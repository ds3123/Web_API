# coding : utf-8
# @Author : DS

from fastapi import HTTPException , Response
from sqlalchemy.orm import Session
from dao.schema import Employee_In
from util import pagination
from util.helper import Hash
from util.auth import oauth2
import dao



# 讀取 _ 所有員工
def read_all_employees( db : Session ) :

    # 讀取所有員工
    employees = dao.read_all_employees( db )

    # 切片分頁
    employees = pagination( employees , 1 ) ;

    return employees


# 讀取 _ 特定員工 ( 依主鍵 id )
def read_employee_by_id( id : int , db : Session  ) :

    db_employee = dao.read_employee_by_id( id , db )

    if not db_employee :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return db_employee


# 讀取 _ 特定員工 ( 依登入所輸入 ：帳號、密碼 )
def read_employee_by_login( account : str , password : str , db : Session ) :

    # 先用 < 帳號 >，查詢資料庫
    db_employee = dao.read_employee_by_account( account , db )

    # 檢查 _ 是否有該筆資料
    if not db_employee:
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 檢查 _ < 密碼 > 是否正確
    if not Hash.verify( db_employee.password , password ) :
        raise HTTPException( detail = "Password Error" , status_code = 401 )

    # 建立 token
    access_token = oauth2.create_access_token( data = { 'sub' : db_employee.account } )


    return {
              'access_token'  : access_token ,
              'token_type'    : 'bearer' ,     # 普遍、標準 token 類型
              'employee_info' : db_employee
            }


# 讀取 _ 特定店家，所有員工
def read_account_all_employees( db : Session , account_id : str ) :

    # 讀取所有員工
    db_employees = dao.read_account_all_employees( db , account_id ) ;

    if not db_employees:
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return db_employees


# 刪除 _ 員工
def delete_employee_by_id( id : int , db : Session ) :

    dao.delete_employee_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }



# 新增 _ 員工
def create_employee( employee : Employee_In , db : Session ) :

    return dao.create_employee( employee , db )


# 修改 _ 員工
def update_employee_by_id( id : int , employee : Employee_In , db : Session ) :

    # 先查詢是否有該店家帳戶
    db_employee = dao.read_employee_by_id( id , db )

    if not db_employee :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_employee_by_id( id , employee , db )

    # 刷新，取得更新後的資料
    db.refresh( db_employee )

    # 回傳 _ 更新、刷新後的資料
    return db_employee


# 刪除 _ 員工
def delete_employee_by_id( id : int , db : Session ) :

    dao.delete_employee_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }

