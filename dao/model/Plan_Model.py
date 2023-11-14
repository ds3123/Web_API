# coding : utf-8
# @Author : DS


from sqlalchemy import Column , String , Integer , Text  , Date , inspect , TIMESTAMP , ForeignKey , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 自訂方案

'''

class Plan_Model( Base_Model ) :

    __tablename__  = "plans"                   # 指定資料表名稱
    __table_args__ = { "comment" : "自訂方案" } # 資料表備註

    id             = Column( Integer , primary_key = True , autoincrement = True ) # 主鍵
    account_id     = Column( Integer , ForeignKey( "accounts.id" ) , nullable = False , comment = "所屬店家 id" )  # 所屬店家 id

    name           = Column( String( 50 ) , unique = True , nullable = False , comment = "方案 _ 名稱" )  # 方案 _ 名稱

    count          = Column( Integer , nullable = False , comment = "方案 _可使用次數" )   # 方案 _可使用次數
    period         = Column( Integer , nullable = True , comment = "方案 _可使用期限" )    # 方案 _可使用期限
    note           = Column( String( 150 ) , nullable = True , comment = "方案 _備註"  )  # 方案 _備註

    created_at     = Column( TIMESTAMP , nullable = False, server_default = func.now() )  # 建立時間
    updated_at     = Column( TIMESTAMP , nullable = False, server_default = func.current_timestamp() , onupdate = func.current_timestamp() )  # 修改時間

    # [ 關聯 ]
    account        = relationship( "Account_Model"  , back_populates = "plan" ) # 店家帳號

    plan_content   = relationship( "Plan_Content_Model" , back_populates = "plan" , cascade = "all,delete-orphan" ) # 方案內容 ( 項目 )
    plan_price     = relationship( "Plan_Price_Model" ,   back_populates = "plan" , cascade = "all,delete-orphan" ) # 方案價格
    plan_order     = relationship( "Plan_Order_Model" ,   back_populates = "plan" , cascade = "all,delete-orphan" ) # 方案購買訂單

