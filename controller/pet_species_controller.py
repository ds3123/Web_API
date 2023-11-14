
# coding : utf-8
# @Author : DS

from fastapi import Depends , APIRouter
from typing import List , Optional
from dao.schema import Pet_Species_In , Pet_Species_Out
from sqlalchemy.orm import Session
from dao.sql import get_db
import service


router = APIRouter(
                     prefix       = "/pet_species" ,
                     tags         = [ "店家 _ 寵物：品種" ] ,
                   # dependencies = [ Depends( get_token_header ) ] ,
                     responses    = { 404 : { "description" : "Not found" }} ,
                  )


# 讀取 _ 所有寵物品種
@router.get( '/' , summary = '所有寵物品種' , description = '讀取 _ 所有寵物品種' , response_model = List[ Pet_Species_Out ] )
async def read_all_pet_species( db : Session = Depends( get_db ) ) :

    return service.read_all_pet_species( db )



# 讀取 _ 特定寵物品種 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 寵物品種' , description = '以 id，查詢特定寵物品種' , response_model = Pet_Species_Out )
async def read_pet_species_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_pet_species_by_id( id , db )


# 新增 _ 寵物品種
@router.post( '/' , summary = '新增 _ 寵物品種' , description = '新增一筆寵物品種資料' , response_model = Pet_Species_Out )
async def create_pet_species( pet_species : Pet_Species_In , db : Session = Depends( get_db ) ) :

    return service.create_pet_species( pet_species , db )


# 修改 _ 寵物品種
@router.put( '/{id}' , summary = '修改 _ 寵物品種' , description = '根據寵物品種資料表 id，修改 _ 特定寵物品種資料' , response_model = Pet_Species_Out  )
async def update_pet_species_by_id( id : int , pet_species : Pet_Species_In , db: Session = Depends( get_db ) ) :

    return service.update_pet_species_by_id( id , pet_species , db )


# 刪除 _ 寵物品種
@router.delete( '/{id}' , summary = '刪除 _ 寵物品種' , description = '根據寵物品種資料表 id，刪除 _ 特定寵物種類資料'  )
async def delete_pet_species_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_pet_species_by_id( id , db )

