# coding : utf-8
# @Author : DS

from sqlalchemy import Column , String , Integer , Text  , Date , inspect , TIMESTAMP , ForeignKey , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 自訂方案 _ 購買訂單

'''


class Plan_Order_Model( Base_Model ) :

    __tablename__  = "plan_orders"                      # 指定資料表名稱
    __table_args__ = { "comment" : "自訂方案 _ 購買訂單" } # 資料表備註

    id             = Column( Integer , primary_key = True, autoincrement = True )  # 主鍵

    plan_id        = Column( Integer , ForeignKey( "plans.id"     , ondelete = "CASCADE" ) , nullable = False, comment="所屬方案 id")  # 所屬方案 id
    account_id     = Column( Integer , ForeignKey( "accounts.id"  , ondelete = "CASCADE" ) , nullable = False , comment = "所屬店家 id" ) # 所屬店家 id
    customer_id    = Column( Integer , ForeignKey( "customers.id" , ondelete = "CASCADE" ) , nullable = False , comment = "所屬客戶 id" ) # 所屬客戶 id
    pet_id         = Column( Integer , ForeignKey( "pets.id"      , ondelete = "CASCADE" ) , nullable = False , comment = "所屬寵物 id" ) # 所屬寵物 id

    plan_price     = Column( Integer , nullable = False , comment = "方案 _ 基本價格" ) # 方案 _ 基本價格
    adjust_amount  = Column( Integer , comment = "方案 _ 調整金額" )                    # 方案 _ 調整金額
    adjust_reason  = Column( String( 50 ) , comment = "方案 _ 調整價格理由" )            # 方案 _ 調整價格理由

    amount_paid    = Column( Integer , nullable = False , comment = "實付金額" )       # 實付金額

    payment_method = Column( String( 15 ) , nullable = False , comment = "付款方式" )  # 付款方式
    payment_date   = Column( Date         , nullable = False , comment = "付款日期" )  # 付款日期

    plan_note      = Column( String( 100 ) , comment = "方案訂單備註" )                 # 方案訂單備註

    created_at     = Column( TIMESTAMP , nullable = False , server_default = func.now() )  # 建立時間
    updated_at     = Column( TIMESTAMP , nullable = False , server_default = func.current_timestamp() , onupdate = func.current_timestamp() ) # 修改時間


    # [ 關聯 ]
    account        = relationship( "Account_Model"     , back_populates = "plan_order" ) # 店家帳號
    plan           = relationship( "Plan_Model"        , back_populates = "plan_order" ) # 所屬方案

    customer       = relationship( "Customer_Model"    , back_populates = "plan_order" ) # 購買客人
    pet            = relationship( "Pet_Model"         , back_populates = "plan_order" ) # 所屬寵物

    plan_record    = relationship( "Plan_Record_Model" , back_populates = "plan_order" ) # 該方案使用紀錄




