# coding : utf-8
# @Author : DS


from fastapi import Depends , APIRouter
from typing import List , Optional
from dao.schema import Pet_Class_In , Pet_Class_Out
import service
from sqlalchemy.orm import Session
from dao.sql import get_db



router = APIRouter(
                     prefix       = "/pet_classes" ,
                     tags         = [ "店家 _ 寵物：種類" ] ,
                    # dependencies = [ Depends( verify_request_jwt_token ) ] ,  # JWT Token 驗證
                     responses    = { 404 : { "description" : "Not found" }} ,
                  )


# 讀取 _ 所有寵物種類
@router.get( '/' , summary = '所有寵物種類' , description = '讀取 _ 所有寵物種類' , response_model = List[ Pet_Class_Out ] )
def read_all_pet_classes( db : Session = Depends( get_db ) ) :

    return service.read_all_pet_classes( db )


# 讀取 _ 特定店家，所有寵物種類
@router.get( '/account/{account_id}' , summary = '特定店家所有寵物種類' , description = '讀取 _ 特定店家，所有寵物種類' , response_model = List[ Pet_Class_Out ] )
def read_account_all_customers( account_id : str , db: Session = Depends( get_db )  ) :

    return service.read_account_all_pet_classes( account_id , db )



# 讀取 _ 特定寵物種類 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 寵物種類' , description = '以 id，查詢特定寵物種類' , response_model = Pet_Class_Out )
async def read_pet_class_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_pet_class_by_id( id , db )



# 新增 _ 寵物種類
@router.post( '/' , summary = '新增 _ 寵物種類' , description = '新增一筆寵物種類資料' , response_model = Pet_Class_Out )
async def create_pet_class( pet_class : Pet_Class_In , db : Session = Depends( get_db ) ) :

    return service.create_pet_class( pet_class , db )


# 修改 _ 寵物種類
@router.put( '/{id}' , summary = '修改 _ 寵物種類' , description = '根據寵物種類資料表 id，修改 _ 特定寵物種類資料' , response_model = Pet_Class_In  )
async def update_pet_class_by_id( id : int , pet_class : Pet_Class_In , db: Session = Depends( get_db ) ) :

    return service.update_pet_class_by_id( id , pet_class , db )



# 刪除 _ 寵物種類
@router.delete( '/{id}' , summary = '刪除 _ 寵物種類' , description = '根據寵物種類資料表 id，刪除 _ 特定寵物種類資料'  )
async def delete_pet_class_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_pet_class_by_id( id , db )





