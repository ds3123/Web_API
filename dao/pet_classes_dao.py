# coding : utf-8
# @Author : DS


from sqlalchemy.orm import Session
from dao.model import Pet_Class_Model
from dao.schema import Pet_Class_In , Pet_Class_Out



# 讀取 _ 所有寵物種類
def read_all_pet_classes( db : Session ) :

    return db.query( Pet_Class_Model ).all()


# 讀取 _ 特定店家，所有寵物種類
def read_account_all_pet_classes( account_id : str , db : Session ) :

    return db.query( Pet_Class_Model ).filter( Pet_Class_Model.account_id == account_id ).all()


# 讀取 _ 特定寵物種類 ( 依主鍵 id )
def read_pet_class_by_id( id : int , db : Session ) :

    return db.query( Pet_Class_Model ).filter( Pet_Class_Model.id == id ).first()



# 新增 _ 寵物種類
def create_pet_class( pet_class : Pet_Class_In , db : Session ) :

    db_pet_class = Pet_Class_Model( **pet_class.dict() )

    db.add( db_pet_class )
    db.commit()

    db.refresh( db_pet_class )

    return db_pet_class



# 修改 _ 寵物種類
def update_pet_class_by_id( id : int , pet_class : Pet_Class_In , db : Session ) :

    db.query( Pet_Class_Model ).filter_by( id = id ).update( { **pet_class.dict() } )
    db.commit()



# 刪除 _ 寵物種類
def delete_pet_class_by_id( id : int , db : Session ) :

    db.query( Pet_Class_Model ).filter_by( id = id ).delete()
    db.commit()