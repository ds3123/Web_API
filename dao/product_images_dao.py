# coding : utf-8
# @Author : DS


from sqlalchemy.orm import Session
from dao.model import Product_Image_Model
from dao.schema import Product_Image_In , Product_Image_Out



# 讀取 _ 所有商品項目 : 圖片
def read_all_product_images( db : Session ) :

    return db.query( Product_Image_Model ).all()


# 讀取 _ 特定商品項目 : 圖片 ( 依主鍵 id )
def read_product_image_by_id( id : int , db : Session ) :

    return db.query( Product_Image_Model ).filter( Product_Image_Model.id == id ).first()


# 新增 _ 商品項目 : 圖片
def create_product_image( product_image : Product_Image_In , db : Session ) :

    db_product_image = Product_Image_Model( **product_image.dict() )

    db.add( db_product_image )
    db.commit()

    db.refresh( db_product_image )

    return db_product_image


# 修改 _ 商品項目 : 圖片
def update_product_image_by_id( id : int , product_image : Product_Image_In , db : Session ) :

    db.query( Product_Image_Model ).filter_by( id = id ).update( { **product_image.dict() } )
    db.commit()


# 刪除 _ 商品項目 : 圖片
def delete_product_image_by_id( id : int , db : Session ) :

    db.query( Product_Image_Model ).filter_by( id = id ).delete()
    db.commit()
