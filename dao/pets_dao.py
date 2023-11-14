# coding : utf-8
# @Author : DS


from sqlalchemy.orm import Session
from dao.model import Pet_Model
from dao.schema import Pet_In , Pet_Out
from typing import Optional
from sqlalchemy import desc



# 讀取 _ 所有寵物
def read_all_pets( db : Session ) :

    return db.query( Pet_Model ).all()


# 讀取 _ 特定店家，所有寵物
def read_account_all_pets( db : Session , account_id : str , search : Optional[ str ] = None ) :

    # 存放篩選條件
    conditions = []

    conditions.append( Pet_Model.account_id == account_id )                 # 店家帳戶 id

    # 搜尋關鍵字 _ 可查詢欄位
    if search :
        conditions.append(
                           # Customer_Model.name.like( f"%{ search }%" )         | # 姓名
                         )

    return db.query( Pet_Model )\
             .filter( *conditions )\
             .order_by( desc( Pet_Model.id ))\
             .limit( 100 ) \
             .all()


# 讀取 _ 特定寵物 ( 依主鍵 id )
def read_pet_by_id( id : int , db : Session ) :

    return db.query( Pet_Model ).filter( Pet_Model.id == id ).first()


# 新增 _ 寵物
def create_pet( pet : Pet_In , db : Session ) :

    db_pet = Pet_Model( **pet.dict() )

    db.add( db_pet )
    db.commit()

    db.refresh( db_pet )

    return db_pet


# 修改 _ 寵物
def update_pet_by_id( id : int , pet : Pet_In , db : Session ) :

    db.query( Pet_Model ).filter_by( id = id ).update( { **pet.dict() } )
    db.commit()


# 刪除 _ 寵物
def delete_pet_by_id( id : int , db : Session ) :

    db.query( Pet_Model ).filter_by( id = id ).delete()
    db.commit()
