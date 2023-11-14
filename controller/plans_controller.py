# coding : utf-8
# @Author : DS


from fastapi import Depends , APIRouter
from typing import List , Optional
from dao.schema import Plan_In , Plan_Out , Plan_Page
from sqlalchemy.orm import Session
from dao.sql import get_db
import service



router = APIRouter(
                     prefix       = "/plans" ,
                     tags         = [ "自訂方案" ] ,
                     # dependencies = [ Depends(verify_request_jwt_token) ],  # JWT Token 驗證
                     responses    = { 404 : { "description" : "Not found" } } ,
                  )



# 讀取 _ 所有自訂方案
@router.get( '/' , summary = '所有自訂方案' , description = '讀取 _ 所有自訂方案' , response_model = Plan_Page )
async def read_all_plans( db : Session = Depends( get_db ) ) :

    return service.read_all_plans( db )



# 讀取 _ 特定店家，所有自訂方案
@router.get( '/account/{account_id}' , summary = '特定店家所有自訂方案' , description = '讀取 _ 特定店家，所有自訂方案' , response_model = List[ Plan_Out ] )
async def read_account_all_plans( account_id : str , db : Session = Depends( get_db ) ) :

    return service.read_account_all_plans( account_id , db )


# 讀取 _ 特定自訂方案 ( 依主鍵 id )
@router.get( '/{id}' , summary = '讀取 _ 特定條件 ( id ) 自訂方案' , description = '以 id，查詢特定自訂方案' , response_model = Plan_Out )
async def read_plan_by_id( id : int , db : Session = Depends( get_db ) ) :

    return service.read_plan_by_id( id , db )


# 新增 _ 自訂方案
@router.post( '/' , summary = '新增 _ 自訂方案' , description = '新增一筆自訂方案資料' , response_model = Plan_Out )
async def create_plan( plan_in : Plan_In , db : Session = Depends( get_db ) ) :

    return service.create_plan( plan_in , db )


# 修改 _ 自訂方案
@router.put( '/{id}' , summary = '修改 _ 自訂方案' , description = '根據自訂方案資料表 id，修改 _ 特定自訂方案' , response_model = Plan_Out )
async def update_plan_by_id( id : int , plan_in : Plan_In , db : Session = Depends( get_db ) ) :

    return service.update_plan_by_id( id , plan_in , db )



# 刪除 _ 自訂方案
@router.delete( '/{id}' , summary = '刪除 _ 自訂方案' , description = '根據自訂方案資料表 id，刪除 _ 特定自訂方案' )
async def delete_plan_by_id( id : int , db: Session = Depends( get_db ) ) :

    return service.delete_plan_by_id( id , db )





