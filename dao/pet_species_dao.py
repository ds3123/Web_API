# coding : utf-8
# @Author : DS


from sqlalchemy.orm import Session
from dao.model import Pet_Species_Model
from dao.schema import Pet_Species_In



# 讀取 _ 所有寵物品種
def read_all_pet_species( db : Session ) :

    return db.query( Pet_Species_Model ).all()


# 讀取 _ 特定寵物品種 ( 依主鍵 id )
def read_pet_species_by_id( id : int , db : Session ) :

    return db.query( Pet_Species_Model ).filter( Pet_Species_Model.id == id ).first()


# 新增 _ 寵物品種
def create_pet_species( pet_species : Pet_Species_In , db : Session ) :

    db_pet_species = Pet_Species_Model( **pet_species.dict() )

    db.add( db_pet_species )
    db.commit()

    db.refresh( db_pet_species )

    return db_pet_species


# 修改 _ 寵物品種
def update_pet_species_by_id( id : int , pet_species : Pet_Species_In , db : Session ) :

    db.query( Pet_Species_Model ).filter_by( id = id ).update( { **pet_species.dict() } )
    db.commit()


# 刪除 _ 寵物品種
def delete_pet_species_by_id( id : int , db : Session ) :

    db.query( Pet_Species_Model ).filter_by( id = id ).delete()
    db.commit()
