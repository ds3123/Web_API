# coding : utf-8
# @Author : DS


from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Service_Price_In
from typing import Optional
import dao



# 讀取 _ 所有服務項目 : 價格
def read_all_service_prices( db : Session ) :

    db_service_prices = dao.read_all_service_prices( db )

    return db_service_prices


# 讀取 _ 特定服務項目 : 價格 ( 依主鍵 id )
def read_service_price_by_id( id : int , db : Session ) :

    db_service_price = dao.read_service_price_by_id( id , db )

    if not db_service_price :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return db_service_price


# 讀取 _ 特定條件 ( 第 1,2 層級分類 id  ) 服務項目 : 價格
def read_service_price_by_class_id( db : Session  , first_id : int , second_id : Optional[ int]  ) :

    return dao.read_service_price_by_class_id( db , first_id , second_id )


# 新增 _ 服務項目 : 價格
def create_service_price( service_price : Service_Price_In , db : Session ) :

    return dao.create_service_price( service_price , db )


# 修改 _ 服務項目 : 價格
def update_service_price_by_id( id : int , service_price : Service_Price_In , db : Session ) :

    # 先查詢是否有該服務價格
    db_service_price = dao.read_service_price_by_id( id , db )

    if not db_service_price :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_service_price_by_id( id , service_price , db )

    # 刷新，取得更新後的資料
    db.refresh( db_service_price )

    # 回傳 _ 更新、刷新後的資料
    return db_service_price


# 刪除 _ 服務項目 : 價格
def delete_service_price_by_id( id : int , db : Session ) :

    dao.delete_service_price_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }
