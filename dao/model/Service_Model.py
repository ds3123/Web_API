# coding : utf-8
# @Author : DS


from sqlalchemy import Column , String , Integer , Text  , Date , inspect , TIMESTAMP , ForeignKey , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 服務項目 

'''


class Service_Model( Base_Model ) :

    __tablename__  = "services"                # 指定資料表名稱
    __table_args__ = { "comment" : "服務項目" }  # 資料表備註

    id             = Column( Integer , primary_key = True , autoincrement = True ) # 主鍵
    account_id     = Column( Integer , ForeignKey( "accounts.id" ) , nullable = False , comment = "所屬店家 id" )  # 所屬店家 id

    name           = Column( String( 50 ) , unique = True , nullable = False , comment = "服務名稱"  )  # 服務名稱

    created_at     = Column( TIMESTAMP , nullable = False , server_default = func.now() )  # 建立時間
    updated_at     = Column( TIMESTAMP , nullable = False , server_default = func.current_timestamp() , onupdate = func.current_timestamp() )  # 修改時間

    # [ 關聯 ]
    account         = relationship( "Account_Model"         , back_populates = "service" )  # 店家帳號

    service_content = relationship( "Service_Content_Model" , back_populates = "service" , cascade = "all,delete-orphan" )  # 服務內容 ( 項目 )
    service_order   = relationship( "Service_Order_Model"   , back_populates = "service" , cascade = "all,delete-orphan" )  # 服務項目 : 訂單
    service_price   = relationship( "Service_Price_Model"   , back_populates = "service" , cascade = "all,delete-orphan" )  # 服務項目 : 價格


    # 回傳 _ Model : 所有屬性
    def as_dict( self ) :
        return { c.key : getattr( self, c.key ) for c in inspect( self ).mapper.column_attrs }




