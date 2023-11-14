# coding : utf-8
# @Author : DS



from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Plan_Content_In
import dao


# 讀取 _ 所有自訂方案 : 內容
def read_all_plan_contents( db : Session ) :

    db_plan_contents = dao.read_all_plan_contents( db )

    return db_plan_contents


# 讀取 _ 特定自訂方案 : 內容 ( 依主鍵 id )
def read_plan_content_by_id( id : int , db : Session ) :

    plan_content = dao.read_plan_content_by_id( id , db )

    if not plan_content :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return plan_content


# 新增 _ 自訂方案 : 內容
def create_plan_content( plan_content : Plan_Content_In , db : Session ) :

    return dao.create_plan_content( plan_content , db )


# 修改 _ 自訂方案 : 內容
def update_plan_content_by_id( id : int , plan_content : Plan_Content_In , db : Session ) :

    # 先查詢是否有該自訂方案
    db_plan_content = dao.read_plan_content_by_id( id , db )

    if not db_plan_content :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_plan_content_by_id( id , plan_content , db )

    # 刷新，取得更新後的資料
    db.refresh( db_plan_content )

    # 回傳 _ 更新、刷新後的資料
    return db_plan_content


# 刪除 _ 自訂方案 : 內容
def delete_plan_content_by_id( id : int , db : Session ) :

    dao.delete_plan_content_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }

