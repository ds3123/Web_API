# coding : utf-8
# @Author : DS


from sqlalchemy.orm import Session
from dao.model import Service_Price_Model
from dao.schema import Service_Price_In
from typing import Optional



# 讀取 _ 所有服務項目 : 價格
def read_all_service_prices( db : Session ) :

    return db.query( Service_Price_Model ).all()


# 讀取 _ 特定服務項目 : 價格 ( 依主鍵 id )
def read_service_price_by_id( id : int , db : Session ) :

    return db.query( Service_Price_Model ).filter( Service_Price_Model.id == id ).first()


# 讀取 _ 特定條件 ( 第 1,2 層級分類 id  ) 服務項目 : 價格
def read_service_price_by_class_id( db : Session , first_id : int , second_id : Optional[ int ] = None ) :

    return db.query( Service_Price_Model )\
           .filter( Service_Price_Model.service_id == first_id , Service_Price_Model.service_content_id == second_id )\
           .first()


# 新增 _ 服務項目 : 價格
def create_service_price( service_price : Service_Price_In , db : Session ) :

    db_service_price = Service_Price_Model( **service_price.dict() )

    db.add( db_service_price )
    db.commit()

    db.refresh( db_service_price )

    return db_service_price


# 修改 _ 服務項目 : 價格
def update_service_price_by_id( id : int , service_price : Service_Price_In  , db : Session ) :

    db.query( Service_Price_Model ).filter_by( id = id ).update( { **service_price.dict() } )
    db.commit()


# 刪除 _ 服務項目 : 價格
def delete_service_price_by_id( id : int , db : Session ) :

    db.query( Service_Price_Model ).filter_by( id = id ).delete()
    db.commit()

