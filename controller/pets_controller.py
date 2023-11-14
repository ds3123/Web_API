# coding : utf-8
# @Author : DS

from fastapi import Depends , APIRouter
from typing import List , Optional
from dao.schema import Pet_In , Pet_Out , Pet_Page
from sqlalchemy.orm import Session
from dao.sql import get_db
import service



router = APIRouter(
                     prefix       = "/pets" ,
                     tags         = [ "店家 _ 寵物" ] ,
                     # dependencies = [Depends(verify_request_jwt_token)],  # JWT Token 驗證
                     responses    = { 404 : { "description" : "Not found" }} ,
                  )



# 讀取 _ 所有寵物
@router.get( '/' , summary = '所有寵物' , description = '讀取 _ 所有寵物' , response_model = Pet_Page  )
async def read_all_pets( db : Session = Depends( get_db ) ) :

    return service.read_all_pets( db )



# 讀取 _ 特定店家，所有寵物
@router.get( '/account/{account_id}' , summary = '特定店家所有寵物' , description = '讀取 _ 特定店家，所有寵物' , response_model = Pet_Page )
async def read_account_all_pets( account_id : str , page : int = 1 , db: Session = Depends( get_db ) , search : Optional[ str ] = None ) :

    return service.read_account_all_pets( db , account_id , page , search )


# 讀取 _ 特定寵物 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 寵物' , description = '以 id，查詢特定寵物' , response_model = Pet_Out )
async def read_pet_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_pet_by_id( id , db )



# 新增 _ 寵物
@router.post( '/' , summary = '新增 _ 寵物' , description = '新增一筆寵物資料' , response_model = Pet_Out )
async def create_pet( pet : Pet_In , db : Session = Depends( get_db ) ) :

    return service.create_pet( pet , db )



# 修改 _ 寵物
@router.put( '/{id}' , summary = '修改 _ 寵物' , description = '根據寵物資料表 id，修改 _ 特定寵物資料' , response_model = Pet_In )
async def update_pet_by_id( id : int , pet : Pet_In , db: Session = Depends( get_db ) ) :

    return service.update_pet_by_id( id , pet , db )



# 刪除 _ 寵物
@router.delete( '/{id}' , summary = '刪除 _ 寵物' , description = '根據寵物資料表 id，刪除 _ 特定寵物資料'  )
async def delete_pet_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_pet_by_id( id , db )







