# coding : utf-8
# @Author : DS


from sqlalchemy import Column , String , Integer , Text  , Date , inspect , TIMESTAMP , ForeignKey
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 自訂方案 : 價格

'''

class Plan_Price_Model( Base_Model ) :

    __tablename__   = "plan_prices"                    # 指定資料表名稱
    __table_args__  = { "comment" : "自訂方案 : 價格" }  # 資料表備註

    id              = Column( Integer , primary_key = True , autoincrement = True ) # 主鍵

    plan_id         = Column( Integer , ForeignKey( "plans.id" , ondelete = "CASCADE" ) , nullable = False , comment = "所屬方案 id" )  # 所屬方案 id
    plan_content_id = Column( Integer , nullable = True , comment = "所屬方案內容 id" )  # 所屬方案內容 id

    price           = Column( Integer , nullable = False , comment = "方案 _ 價格" )  # 方案 _ 價格


    # [ 關聯 ]
    plan            = relationship( "Plan_Model" , back_populates = "plan_price" ) # 所屬方案








