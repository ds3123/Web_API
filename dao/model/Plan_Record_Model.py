# coding : utf-8
# @Author : DS


from sqlalchemy import Column , String , Integer , Text  , Date , inspect , TIMESTAMP , ForeignKey , Boolean , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 自訂方案 _ 使用紀錄

'''


class Plan_Record_Model( Base_Model ) :

    __tablename__  = "plan_records"                     # 指定資料表名稱
    __table_args__ = { "comment" : "自訂方案 _ 使用紀錄" } # 資料表備註

    id               = Column( Integer , primary_key = True , autoincrement = True )  # 主鍵

    plan_order_id    = Column( Integer , ForeignKey( "plan_orders.id" ) ,    nullable = False , comment = "所購買方案 id" )  # 所購買方案 id
    service_order_id = Column( Integer , ForeignKey( "service_orders.id" ) , nullable = False , comment = "所購買服務 id" )  # 所購買服務 id

    customer_id      = Column( Integer , ForeignKey( "customers.id" ) ,    nullable = False , comment = "使用客戶 id" )  # 使用客戶 id
    pet_id           = Column( Integer , ForeignKey( "pets.id" ) ,         nullable = False , comment = "使用寵物 id" )  # 使用寵物 id

    record_note      = Column( String( 150 ) , comment = "方案使用備註" )  # 方案使用備註

    is_delete        = Column( Boolean , default = False , comment = "是否銷單 _ 0 : 否 , 1 : 是" )  # 是否銷單
    delete_reason    = Column( String( 50 ) , comment = "銷單理由"   )  # 銷單理由
    delete_submitter = Column( String( 20 ) , comment = "銷單提交者" )  # 銷單提交者

    created_at       = Column( TIMESTAMP , nullable = False , server_default = func.now() )  # 建立時間
    updated_at       = Column( TIMESTAMP , nullable = False , server_default = func.current_timestamp() , onupdate = func.current_timestamp() ) # 修改時間

    # [ 關聯 ]
    plan_order       = relationship( "Plan_Order_Model"    , back_populates = "plan_record" )  # 所屬方案
    service_order    = relationship( "Service_Order_Model" , back_populates = "plan_record" )  # 所屬服務項目
    customer         = relationship( "Customer_Model"      , back_populates = "plan_record" )  # 使用客戶
    pet              = relationship( "Pet_Model"           , back_populates = "plan_record" )  # 使用寵物