# coding : utf-8
# @Author : DS

from typing import Union
from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Customer_In
from util import pagination
import dao


# 讀取 _ 所有客戶
def read_all_customers( db : Session , page : int = 1 ) :

    # 讀取 _ 所有客戶
    db_customers = dao.read_all_customers( db )

    # 分頁資料
    customers_dict = pagination( db_customers , page )

    return customers_dict


# 讀取 _ 特定店家，所有客戶
def read_account_all_customers( db : Session , account_id : str , page : int , search : Union[ str , None] = None   ) :

    # 讀取所有客戶
    db_customers   = dao.read_account_all_customers( db , account_id , search )

    # 分頁資料
    customers_dict = pagination( db_customers , page )

    return customers_dict


# 讀取 _ 特定客戶 ( 依主鍵 id )
def read_customer_by_id( id : int , db : Session ) :

    customer = dao.read_customer_by_id( id , db )

    if not customer:
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return customer



# 讀取 _ 特定店家，特定手機號碼客戶
def read_account_customer_by_mobile( db : Session , account_id : str , mobile : str  ) :

    db_customers = dao.read_account_customer_by_mobile( db , account_id , mobile )

    return db_customers


# 新增 _ 客戶
def create_customer( customer : Customer_In , db : Session ) :

    return dao.create_customer( customer , db )


# 修改 _ 客戶
def update_customer_by_id( id : int , customer : Customer_In , db : Session ) :

    # 先查詢是否有該店家帳戶
    db_customer = dao.read_customer_by_id( id , db )

    if not db_customer :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_customer_by_id( id , customer , db )

    # 刷新，取得更新後的資料
    db.refresh( db_customer )

    # 回傳 _ 更新、刷新後的資料
    return db_customer


# 刪除 _ 客戶
def delete_customer_by_id( id : int , db : Session ) :

    dao.delete_customer_by_id( id , db )

    return { 'code' : 200, "message" : '刪除完成' }

