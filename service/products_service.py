# coding : utf-8
# @Author : DS


from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Product_In
from util import pagination
import dao


# 讀取 _ 所有商品項目
def read_all_products( db : Session ) :

    # 讀取所有商品項目
    products = dao.read_all_products( db )

    # 切片分頁
    products = pagination( products , 1 ) ;

    return products


# 讀取 _ 特定商品項目 : 價格 ( 依主鍵 id )
def read_product_by_id( id : int , db : Session ) :

    product = dao.read_product_by_id( id , db )

    if not product :
        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return product


# 新增 _ 商品項目
def create_product( product : Product_In , db : Session ) :

    return dao.create_product( product , db )


# 修改 _ 商品項目
def update_product_by_id( id : int , product : Product_In , db : Session ) :

    # 先查詢是否有該商品項目
    db_product = dao.read_product_by_id( id , db )

    if not db_product :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_product_by_id( id , product , db )

    # 刷新，取得更新後的資料
    db.refresh( db_product )

    # 回傳 _ 更新、刷新後的資料
    return db_product


# 刪除 _ 商品項目
def delete_product_by_id( id : int , db : Session ) :

    dao.delete_product_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }





