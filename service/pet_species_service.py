# coding : utf-8
# @Author : DS

from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Pet_Species_In
import dao



# 讀取 _ 所有寵物品種
def read_all_pet_species( db : Session ) :

    db_pet_species = dao.read_all_pet_species( db )

    return db_pet_species


# 讀取 _ 特定寵物品種 ( 依主鍵 id )
def read_pet_species_by_id( id : int , db : Session  ) :

    pet_species = dao.read_pet_species_by_id( id , db )

    if not pet_species :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return pet_species


# 新增 _ 寵物品種
def create_pet_species( pet_species : Pet_Species_In , db : Session ) :

    return dao.create_pet_species( pet_species , db )


# 修改 _ 寵物品種
def update_pet_species_by_id( id : int , pet_species : Pet_Species_In  , db : Session ) :

    # 先查詢是否有該寵物品種
    db_pet_species = dao.read_pet_species_by_id( id , db )

    if not db_pet_species :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_pet_species_by_id( id , pet_species , db )

    # 刷新，取得更新後的資料
    db.refresh( db_pet_species )

    # 回傳 _ 更新、刷新後的資料
    return db_pet_species


# 刪除 _ 寵物品種
def delete_pet_species_by_id( id : int , db : Session ) :

    dao.delete_pet_species_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }
