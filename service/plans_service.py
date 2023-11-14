# coding : utf-8
# @Author : DS


from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Plan_In
from util import pagination
import dao


# 讀取 _ 所有自訂方案
def read_all_plans( db : Session ) :

    # 讀取所有商品項目
    plans = dao.read_all_plans( db )

    # 切片分頁
    plans = pagination( plans , 1 ) ;

    return plans


# 讀取 _ 特定店家，所有自訂方案
def read_account_all_plans( account_id : str , db : Session ) :

    db_plans = dao.read_account_all_plans( account_id , db )

    return db_plans


# 讀取 _ 特定自訂方案 ( 依主鍵 id )
def read_plan_by_id( id : int , db : Session ) :

    plan = dao.read_plan_by_id( id , db )

    if not plan :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return plan


# 新增 _ 自訂方案
def create_plan( plan : Plan_In , db : Session ) :

    return dao.create_plan( plan , db )


# 修改 _ 自訂方案
def update_plan_by_id( id : int , plan : Plan_In, db : Session ) :

    # 先查詢是否有該自訂方案
    db_plan = dao.read_plan_by_id( id , db )

    if not db_plan :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_plan_by_id( id , plan , db )

    # 刷新，取得更新後的資料
    db.refresh( db_plan )

    # 回傳 _ 更新、刷新後的資料
    return db_plan


# 刪除 _ 自訂方案
def delete_plan_by_id( id : int , db : Session ) :

    dao.delete_plan_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }
