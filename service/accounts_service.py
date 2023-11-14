# coding : utf-8
# @Author : DS


from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Account_In
from util import pagination
import dao


# 讀取 _ 所有店家帳戶
def read_all_accounts( db : Session , page : int = 1 ) :

    # 讀取所有店家
    db_accounts   = dao.read_all_accounts( db )

    # 分頁資料
    accounts_dict = pagination( db_accounts , page )

    return accounts_dict



# 讀取 _ 特定帳戶 ( 依主鍵 id )
def read_account_by_id( id : int , db : Session ) :

    account = dao.read_account_by_id( id , db )

    if not account :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return account


# 讀取 _ 特定條件 : 郵遞區號 店家帳戶
def read_accounts_by_zipcode( zipcode : str , db : Session ) :

    accounts = dao.read_accounts_by_zipcode( zipcode , db )

    if not accounts :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return accounts


# 新增 _ 店家帳戶
def create_account( account : Account_In , db : Session ) :

    return dao.create_account( account , db )


# 修改 _ 店家帳戶
def update_account_by_id( id : int , account : Account_In , db : Session ) :

    # 先查詢是否有該店家帳戶
    db_account = dao.read_account_by_id( id , db )

    if not db_account :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_account_by_id( id , account , db)

    # 刷新，取得更新後的資料
    db.refresh( db_account )

    # 回傳 _ 更新、刷新後的資料
    return db_account


# 刪除 _ 店家
def delete_account_by_id( id : int , db : Session ) :

    dao.delete_account_by_id( id , db )

    return {'code': 200, "message": '刪除完成'}
