# coding : utf-8
# @Author : DS

from sqlalchemy.orm import Session , relationship
from dao.model import Account_Model
from dao.schema import Account_In , Account_Out
from sqlalchemy import desc


# 讀取 _ 所有店家帳戶
def read_all_accounts( db : Session ) :

    return db.query( Account_Model ).order_by( desc( Account_Model.id ) ).all()



# 讀取 _ 特定帳戶 ( 依主鍵 id )
def read_account_by_id( id : int , db : Session ) :

    return db.query( Account_Model ).filter( Account_Model.id == id ).first()


# 讀取 _ 特定條件 : 郵遞區號 店家帳戶
def read_accounts_by_zipcode( zipcode : str , db : Session ) :

    return db.query( Account_Model ).filter( Account_Model.zipcode == zipcode ).all()



# 新增 _ 店家帳戶
def create_account( account : Account_In , db : Session ) :

    db_account = Account_Model( **account.dict() )

    db.add( db_account )
    db.commit()

    db.refresh( db_account )

    return db_account


# 修改 _ 店家帳戶
def update_account_by_id( id : int , account : Account_In , db : Session ) :

    db.query( Account_Model ).filter_by( id = id ).update( { **account.dict() } )
    db.commit()



# 刪除 _ 店家帳戶
def delete_account_by_id( id : int , db : Session ) :

    db.query( Account_Model ).filter_by( id = id ).delete()
    db.commit()

