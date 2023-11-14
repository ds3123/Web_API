# coding : utf-8
# @Author : DS


from sqlalchemy import Column , String , Integer , Text  , Date , inspect , TIMESTAMP , ForeignKey
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 服務項目 : 價格 

'''

class Service_Price_Model( Base_Model ) :

    __tablename__      = "service_prices"                 # 指定資料表名稱
    __table_args__     = { "comment" : "服務項目 : 價格" }  # 資料表備註

    id                 = Column( Integer , primary_key = True , autoincrement = True ) # 主鍵

    service_id         = Column( Integer , ForeignKey( "services.id" ) , nullable = False , comment = "所屬服務 _ 項目 id" )  # 所屬服務 _ 項目 id
    service_content_id = Column( Integer , comment = "所屬服務 _ 項目 : 內容 id" ) # 所屬服務 _ 項目 : 內容 id


    price              = Column( Integer , nullable = False , comment = "服務 _ 價格" )  # 服務價格

    # [ 關聯 ]
    service            = relationship( "Service_Model" , back_populates = "service_price" )          # 服務 _ 項目


    # 回傳 _ Model : 所有屬性
    def as_dict( self ) :
        return { c.key : getattr( self, c.key ) for c in inspect( self ).mapper.column_attrs }

