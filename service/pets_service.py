# coding : utf-8
# @Author : DS


from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Pet_In
from typing import Optional
from util import pagination
import dao



# 讀取 _ 所有寵物
def read_all_pets( db : Session ) :

    # 讀取所有寵物
    pets = dao.read_all_pets( db )

    # 切片分頁
    pets = pagination( pets , 1  ) ;

    return pets


# 讀取 _ 特定店家，所有寵物
def read_account_all_pets( db : Session , account_id : str , page : int , search : Optional[ str ] = None ) :

    # 讀取所有寵物
    db_pets   = dao.read_account_all_pets( db , account_id , search ) ;

    # 分頁資料
    pets_dict = pagination( db_pets , page ) ;

    return pets_dict


# 讀取 _ 特定寵物 ( 依主鍵 id )
def read_pet_by_id( id : int , db : Session  ) :

    pet = dao.read_pet_by_id( id , db )

    if not pet:
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return pet


# 新增 _ 寵物
def create_pet( pet : Pet_In , db : Session ) :

    return dao.create_pet( pet , db )


# 修改 _ 寵物
def update_pet_by_id( id : int , pet : Pet_In , db : Session ) :

    # 先查詢是否有該寵物
    db_pet = dao.read_pet_by_id( id , db )

    if not db_pet :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_pet_by_id( id , pet , db )

    # 刷新，取得更新後的資料
    db.refresh( db_pet )

    # 回傳 _ 更新、刷新後的資料
    return db_pet


# 刪除 _ 寵物
def delete_pet_by_id( id : int , db : Session ) :

    dao.delete_pet_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }