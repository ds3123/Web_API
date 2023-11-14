# coding : utf-8
# @Author : DS

from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Pet_Class_In
import dao


# 讀取 _ 所有寵物種類
def read_all_pet_classes( db : Session ) :

    db_pet_classes = dao.read_all_pet_classes( db )

    return db_pet_classes



# 讀取 _ 特定店家，所有寵物種類
def read_account_all_pet_classes( account_id : str , db : Session ) :

    db_pet_classes = dao.read_account_all_pet_classes( account_id , db )

    return db_pet_classes


# 讀取 _ 特定寵物種類 ( 依主鍵 id )
def read_pet_class_by_id( id : int , db : Session  ) :

    pet_class = dao.read_pet_class_by_id( id , db )

    if not pet_class :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return pet_class



# 新增 _ 寵物種類
def create_pet_class( pet_class : Pet_Class_In , db : Session ) :

    return dao.create_pet_class( pet_class , db )


# 修改 _ 寵物種類
def update_pet_class_by_id( id : int , pet_class : Pet_Class_In , db : Session ) :

    # 先查詢是否有該寵物種類
    db_pet_class = dao.read_pet_class_by_id( id , db )

    if not db_pet_class :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_pet_class_by_id( id , pet_class , db )

    # 刷新，取得更新後的資料
    db.refresh( db_pet_class )

    # 回傳 _ 更新、刷新後的資料
    return db_pet_class


# 刪除 _ 寵物種類
def delete_pet_class_by_id( id : int , db : Session ) :

    dao.delete_pet_class_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }
