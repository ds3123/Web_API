# coding : utf-8
# @Author : DS


from sqlalchemy.orm import Session
from dao.model import Product_Model
from dao.schema import Product_In



# 讀取 _ 所有商品項目
def read_all_products( db : Session ) :

    return db.query( Product_Model ).all()


# 讀取 _ 特定商品項目 : 價格 ( 依主鍵 id )
def read_product_by_id( id : int , db : Session ) :

    return db.query( Product_Model ).filter( Product_Model.id == id ).first()


# 新增 _ 商品項目
def create_product( product : Product_In , db : Session ) :

    db_product = Product_Model( **product.dict() )

    db.add( db_product )
    db.commit()

    db.refresh( db_product )

    return db_product


# 修改 _ 商品項目
def update_product_by_id( id : int , product : Product_In , db : Session ) :

    db.query( Product_Model ).filter_by( id = id ).update( { **product.dict() } )
    db.commit()


# 刪除 _ 商品項目
def delete_product_by_id( id : int , db : Session ) :

    db.query( Product_Model ).filter_by( id = id ).delete()
    db.commit()


