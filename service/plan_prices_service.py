# coding : utf-8
# @Author : DS


from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Plan_Price_In
from typing import Optional
import dao


# 讀取 _ 所有方案項目 : 價格
def read_all_plan_prices( db : Session ) :

    db_plan_prices = dao.read_all_plan_prices( db )

    return db_plan_prices


# 讀取 _ 特定自訂方案 : 價格 ( 依主鍵 id )
def read_plan_price_by_id( id : int , db : Session ) :

    db_plan_price = dao.read_plan_price_by_id( id , db )

    if not db_plan_price :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return db_plan_price


# 讀取 _ 特定條件 ( 第 1,2 層級分類 id  ) 方案項目 : 價格
def read_plan_price_by_class_id( db : Session , first_id : int , second_id : Optional[ int] = None  ) :

    return dao.read_plan_price_by_class_id( first_id , second_id , db )


# 新增 _ 方案項目 : 價格
def create_plan_price( plan_price : Plan_Price_In , db : Session ) :

    return dao.create_plan_price( plan_price , db )


# 修改 _ 方案項目 : 價格
def update_plan_price_by_id( id : int , plan_price : Plan_Price_In , db : Session ) :

    # 先查詢是否有該服務價格
    db_plan_price = dao.read_plan_price_by_id( id , db )

    if not db_plan_price :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_plan_price_by_id( id , plan_price , db )

    # 刷新，取得更新後的資料
    db.refresh( db_plan_price )

    # 回傳 _ 更新、刷新後的資料
    return db_plan_price


# 刪除 _ 方案項目 : 價格
def delete_plan_price_by_id( id : int , db : Session ) :

    dao.delete_plan_price_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }
