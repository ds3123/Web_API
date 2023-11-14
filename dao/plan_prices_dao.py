# coding : utf-8
# @Author : DS

from sqlalchemy.orm import Session
from dao.model import Plan_Price_Model
from dao.schema import Plan_Price_In , Plan_Price_Out
from typing import Optional



# 讀取 _ 所有方案項目 : 價格
def read_all_plan_prices( db : Session ) :

    return db.query( Plan_Price_Model ).all()


# 讀取 _ 特定自訂方案 : 價格 ( 依主鍵 id )
def read_plan_price_by_id( id : int , db : Session ) :

    return db.query( Plan_Price_Model ).filter( Plan_Price_Model.id == id ).first()


# 讀取 _ 特定條件 ( 第 1,2 層級分類 id  ) 方案項目 : 價格
def read_plan_price_by_class_id( db : Session , first_id : int ,  second_id : Optional[ int ] = None ) :

    return db.query( Plan_Price_Model )\
           .filter( Plan_Price_Model.plan_id == first_id , Plan_Price_Model.plan_content_id == second_id )\
           .first()


# 新增 _ 方案項目 : 價格
def create_plan_price( plan_price : Plan_Price_In , db : Session ) :

    db_plan_price = Plan_Price_Model( **plan_price.dict() )

    db.add( db_plan_price )
    db.commit()

    db.refresh( db_plan_price )

    return db_plan_price


# 修改 _ 方案項目 : 價格
def update_plan_price_by_id( id : int , plan_price : Plan_Price_In  , db : Session ) :

    db.query( Plan_Price_Model ).filter_by( id = id ).update( { **plan_price.dict() } )
    db.commit()


# 刪除 _ 方案項目 : 價格
def delete_plan_price_by_id( id : int , db : Session ) :

    db.query( Plan_Price_Model ).filter_by( id = id ).delete()
    db.commit()


