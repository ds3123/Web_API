# coding : utf-8
# @Author : DS


from sqlalchemy import Column, String, Integer, Text, Date, inspect, TIMESTAMP, ForeignKey , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model

'''

   @ 自訂方案 : 內容 ( 選項 )

'''


class Plan_Content_Model( Base_Model ) :

    __tablename__  = "plan_contents"                          # 指定資料表名稱
    __table_args__ = { "comment" : "自訂方案 : 內容 ( 選項 )" }  # 資料表備註


    id            = Column( Integer , primary_key = True , autoincrement = True )  # 主鍵
    plan_id       = Column( Integer , ForeignKey( "plans.id" ) , nullable = False , comment = "所屬自訂方案 id" )  # 所屬自訂方案 id

    content       = Column( String( 50 ) , nullable = False , comment = "方案項目 ( 項目 ) 名稱" )  # 方案項目 ( 項目 ) 名稱

    # [ 關聯 ]
    plan          = relationship( "Plan_Model" , back_populates = "plan_content" ) # 服務項目


