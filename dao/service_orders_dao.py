# coding : utf-8
# @Author : DS


from sqlalchemy.orm import Session
from dao.model import Service_Order_Model
from dao.schema import Service_Order_In
from typing import Optional
from sqlalchemy import desc



# 讀取 _ 所有服務項目 : 訂單
def read_all_service_orders( db : Session ) :

    return db.query( Service_Order_Model ).all()


# 讀取 _ 特定店家，所有服務項目 : 訂單
def read_account_service_orders( db : Session , account_id : str , search : Optional[ str ] = None ) :

    # 存放篩選條件
    conditions = []

    conditions.append( Service_Order_Model.account_id == account_id )                 # 店家帳戶 id

    # 搜尋關鍵字 _ 可查詢欄位
    if search :
        conditions.append(
                           # Service_Order_Model.name.like( f"%{ search }%" )         | # 姓名

                         )

    return db.query( Service_Order_Model )\
             .filter( *conditions )\
             .order_by( desc( Service_Order_Model.id ))\
             .limit( 100 ) \
             .all()


# 讀取 _ 特定服務項目 : 訂單 ( 依主鍵 id )
def read_service_order_by_id( id : int , db : Session ) :

    return db.query( Service_Order_Model ).filter( Service_Order_Model.id == id ).first()


# 讀取 _ 特定店家，特定 [ 到店日期 ] _ 服務訂單
def read_account_service_orders_by_service_date( db : Session , account_id : str , service_date : str ) :

    return db.query( Service_Order_Model ) \
             .filter( Service_Order_Model.account_id == account_id ,    # 特定店家
                      Service_Order_Model.service_date == service_date  # 到店日期
                    ) \
             .order_by( desc( Service_Order_Model.id ) ) \
             .all()


# 讀取 _ 特定店家，特定 [ 付款日期 ] _ 服務訂單
def read_account_service_orders_by_payment_date( db : Session , account_id : str , payment_date : str ) :

    return db.query( Service_Order_Model ) \
             .filter( Service_Order_Model.account_id == account_id ,    # 特定店家
                      Service_Order_Model.payment_date == payment_date  # 付款日期
                    ) \
             .order_by( desc( Service_Order_Model.id ) ) \
             .all()


# 新增 _ 服務項目 : 訂單
def create_service_order( service_order : Service_Order_In , db : Session ) :

    db_service_order = Service_Order_Model( **service_order.dict() )

    db.add( db_service_order )
    db.commit()

    db.refresh( db_service_order )

    return db_service_order


# 修改 _ 服務項目 : 訂單
def update_service_order_by_id( id : int , service_order : Service_Order_In , db : Session ) :

    db.query( Service_Order_Model ).filter_by( id = id ).update( { **service_order.dict() } )
    db.commit()


# 刪除 _ 服務項目 : 訂單
def delete_service_order_by_id( id : int , db : Session ) :

    db.query( Service_Order_Model ).filter_by( id = id ).delete()
    db.commit()

