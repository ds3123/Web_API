# coding : utf-8
# @Author : DS



from sqlalchemy import Column , String , Integer , Text  , Date , inspect , TIMESTAMP , ForeignKey , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model

'''

   @ 商品項目 : 訂單

'''


class Product_Order_Model( Base_Model ) :

    __tablename__  = "product_orders" # 指定資料表名稱
    __table_args__ = { "comment": "商品項目 : 訂單" }  # 資料表備註

    id             = Column( Integer , primary_key = True , autoincrement = True ) # 主鍵

    account_id     = Column( Integer , ForeignKey( "accounts.id" ) ,  nullable = False , comment = "所屬店家 id" )    # 所屬店家 id
    customer_id    = Column( Integer , ForeignKey( "customers.id" ) , nullable = False , comment = "所屬客人 id" )    # 所屬客人 id
    product_id     = Column( Integer , ForeignKey( "products.id" ) ,  nullable = False , comment = "所屬商品項目 id" ) # 所屬商品項目 id

    order_quantity = Column( Integer , nullable = False , default = 1 , comment = "訂購數量" )      # 訂購數量

    payment_amount = Column( Integer      , nullable = False , comment = "付款金額" )  # 付款金額
    payment_method = Column( String( 30 ) , nullable = False , comment = "付款方法" )  # 付款方法
    payment_date   = Column( Date         , nullable = False , comment = "付款日期" )  # 付款日期

    created_at     = Column( TIMESTAMP , nullable = False , server_default = func.now())  # 建立時間
    updated_at     = Column( TIMESTAMP , nullable = False , server_default = func.current_timestamp() , onupdate = func.current_timestamp())  # 修改時間


    # [ 關聯 ]
    account        = relationship( "Account_Model"  , back_populates = "product_order"  ) # 店家帳號
    customer       = relationship( "Customer_Model" , back_populates = "product_order"  ) # 店家客戶

    product        = relationship( "Product_Model"  , back_populates = "product_order"  ) # 店家商品
