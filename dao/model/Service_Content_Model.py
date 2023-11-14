# coding : utf-8
# @Author : DS



from sqlalchemy import Column , String , Integer , Text  , Date , inspect , TIMESTAMP , ForeignKey , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 服務項目 : 內容 ( 選項 ) 

'''


class Service_Content_Model( Base_Model ) :

    __tablename__  = "service_contents"                       # 指定資料表名稱
    __table_args__ = { "comment": "服務項目 : 內容 ( 選項 ) " }  # 資料表備註

    id             = Column( Integer , primary_key = True , autoincrement = True ) # 主鍵
    service_id     = Column( Integer , ForeignKey( "services.id" ) , nullable = False , comment = "所屬服務項目 id" )  # 所屬服務項目 id

    content        = Column( String( 50 ) , nullable = False , comment = "服務項目 ( 項目 ) 名稱"  )  # 服務項目 ( 項目 ) 名稱

    created_at     = Column( TIMESTAMP , nullable = False, server_default = func.now() )  # 建立時間
    updated_at     = Column( TIMESTAMP , nullable = False, server_default = func.current_timestamp() , onupdate = func.current_timestamp() )  # 修改時間

    # [ 關聯 ]
    service        = relationship( "Service_Model" , back_populates = "service_content" ) # 服務項目


    # 回傳 _ Model : 所有屬性
    def as_dict( self ) :
        return { c.key : getattr( self, c.key ) for c in inspect( self ).mapper.column_attrs }

