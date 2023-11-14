# coding : utf-8
# @Author : DS

from sqlalchemy import desc
from sqlalchemy.orm import Session
from dao.model import Customer_Model
from dao.schema import Customer_In
from typing import Optional



# 讀取 _ 所有客戶
def read_all_customers( db : Session ) :

    return db.query( Customer_Model ).order_by( desc( Customer_Model.id ) ).all()


# 讀取 _ 特定店家，所有客戶
def read_account_all_customers( db : Session , account_id : str , search : Optional[ str ] = None ) :

    # 存放篩選條件
    conditions = []

    conditions.append( Customer_Model.account_id == account_id )                 # 店家帳戶 id

    # 搜尋關鍵字 _ 可查詢欄位
    if search :
        conditions.append(
                           Customer_Model.name.like( f"%{ search }%" )         | # 姓名
                           Customer_Model.serial_id.like( f"%{ search }%" )    | # 身分證字號
                           Customer_Model.mobile_phone.like( f"%{ search }%" ) | # 手機號碼
                           Customer_Model.address.like( f"%{ search }%" )        # 通訊地址
                         )

    return db.query( Customer_Model )\
             .filter( *conditions )\
             .order_by( desc( Customer_Model.id ))\
             .limit( 100 ) \
             .all()


# 讀取 _ 特定客戶 ( 依主鍵 id )
def read_customer_by_id( id : int , db : Session ) :

    return db.query( Customer_Model ).filter( Customer_Model.id == id ).first()



# 讀取 _ 特定店家，特定手機號碼客戶
def read_account_customer_by_mobile( db : Session , account_id : str , mobile : str ) :

    return db.query( Customer_Model ) \
             .filter( Customer_Model.account_id == account_id , Customer_Model.mobile_phone.like( f"%{ mobile }%" ) ) \
             .order_by( desc( Customer_Model.id )) \
             .limit( 4 ) \
             .all()



# 新增 _ 客戶
def create_customer( customer : Customer_In , db : Session ) :

    db_customer = Customer_Model( **customer.dict() )

    db.add( db_customer )
    db.commit()

    db.refresh( db_customer )

    return db_customer



# 修改 _ 客戶
def update_customer_by_id( id : int , customer : Customer_In , db : Session ) :

    db.query( Customer_Model ).filter_by( id = id ).update( { **customer.dict() } )
    db.commit()


# 刪除 _ 客戶
def delete_customer_by_id( id : int , db : Session ) :

    db.query( Customer_Model ).filter_by( id = id ).delete()
    db.commit()


