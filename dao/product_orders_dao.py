# coding : utf-8
# @Author : DS

from sqlalchemy.orm import Session
from dao.model import Product_Order_Model
from dao.schema import Product_Order_In


# 讀取 _ 所有商品項目 : 訂單
def read_all_product_orders( db : Session ) :

    return db.query( Product_Order_Model ).all()


# 讀取 _ 特定商品項目 : 訂單 ( 依主鍵 id )
def read_product_order_by_id( id : int , db : Session ) :

    return db.query( Product_Order_Model ).filter( Product_Order_Model.id == id ).first()


# 新增 _ 商品項目 : 訂單
def create_product_order( product_order : Product_Order_In , db : Session ) :

    db_product_order = Product_Order_Model( **product_order.dict() )

    db.add( db_product_order )
    db.commit()

    db.refresh( db_product_order )

    return db_product_order


# 修改 _ 商品項目 : 訂單
def update_product_order_by_id( id : int , product_order : Product_Order_In , db : Session ) :

    db.query( Product_Order_Model ).filter_by( id = id ).update( { **product_order.dict() } )
    db.commit()


# 刪除 _ 商品項目 : 訂單
def delete_product_order_by_id( id : int , db : Session ) :

    db.query( Product_Order_Model ).filter_by( id = id ).delete()
    db.commit()




