# coding : utf-8
# @Author : DS


from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Product_Order_In
from util import pagination
import dao


# 讀取 _ 所有商品項目 : 訂單
def read_all_product_orders( db : Session ) :

    # 讀取所有商品項目
    product_orders = dao.read_all_product_orders( db )

    # 切片分頁
    product_orders = pagination( product_orders , 1  ) ;

    return product_orders


# 讀取 _ 特定商品項目 : 訂單 ( 依主鍵 id )
def read_product_order_by_id( id : int , db : Session ) :

    product_order = dao.read_product_order_by_id( id , db )

    if not product_order :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    return product_order


# 新增 _ 商品項目 : 訂單
def create_product_order( product_order : Product_Order_In , db : Session ) :

    return dao.create_product_order( product_order , db )


# 修改 _ 商品項目 : 訂單
def update_product_order_by_id( id : int , product_order : Product_Order_In , db : Session ) :

    # 先查詢是否有該商品項目
    db_product_order = dao.read_product_order_by_id( id , db )

    if not db_product_order :

        raise HTTPException( detail = "Not Found" , status_code = 404 )

    # 更新資料
    dao.update_product_order_by_id( id , product_order , db )

    # 刷新，取得更新後的資料
    db.refresh( db_product_order )

    # 回傳 _ 更新、刷新後的資料
    return db_product_order


# 刪除 _ 商品項目 : 訂單
def delete_product_order_by_id( id : int , db : Session ) :

    dao.delete_product_order_by_id( id , db )

    return { 'code' : 200 , "message" : '刪除完成' }

