# coding : utf-8
# @Author : DS

from sqlalchemy import Column , String , Integer , TIMESTAMP , inspect , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model

'''

    @ 店家 _ 帳號

'''

class Account_Model( Base_Model ) :

    __tablename__  = "accounts"                    # 指定資料表名稱
    __table_args__ = { "comment" : "店家 / 帳號" }  # 資料表備註

    id         = Column( Integer , primary_key = True  , autoincrement = True )      # 主鍵

    county     = Column( String( 20 ) , nullable = False , comment = "所屬縣市" )     # 縣市
    district   = Column( String( 20 ) , nullable = False , comment = "所屬行政區" )    # 行政區
    zipcode    = Column( String( 20 ) , nullable = False , comment = "所屬郵遞區號" )  # 郵遞區號

    serial     = Column( String( 20 ) , nullable = False , comment = "區域店別編號" )  # 店別編號

    shop_brand = Column( String( 30 ) , nullable = False , comment = "店家品牌" )     # 店家品牌
    shop_name  = Column( String( 50 ) , nullable = False , comment = "店家名稱" )     # 店家名稱
    shop_owner = Column( String( 20 ) , nullable = False , comment = "店家負責人" )    # 店家負責人

    auth_level = Column( String( 15 ) , nullable = False , comment = "權限等級" )     # 權限等級

    created_at = Column( TIMESTAMP , nullable = False , server_default = func.now() ) # 建立時間
    updated_at = Column( TIMESTAMP , nullable = False , server_default = func.current_timestamp() , onupdate = func.current_timestamp() ) # 修改時間

    # 關聯
    employee      = relationship( "Employee_Model" , back_populates = "shop_account"  ) # 所屬店家員工
    customer      = relationship( "Customer_Model" , back_populates = "account" )       # 所屬店家客人

    pet           = relationship( "Pet_Model"       , back_populates = "account" )      # 所有店家寵物
    pet_class     = relationship( "Pet_Class_Model" , back_populates = "account" )      # 所有店家寵物 : 種類

    service       = relationship( "Service_Model"       , back_populates = "account" )  # 服務項目
    service_order = relationship( "Service_Order_Model" , back_populates = "account" )  # 服務項目 : 訂單

    plan          = relationship( "Plan_Model"       , back_populates = "account" )     # 自訂方案
    plan_order    = relationship( "Plan_Order_Model" , back_populates = "account" )     # 自訂方案 _ 購買

    product       = relationship( "Product_Model"       , back_populates = "account")   # 商品項目
    product_order = relationship( "Product_Order_Model" , back_populates = "account")   # 商品項目 : 訂單


    # 回傳 _ Model : 所有屬性
    def as_dict( self ) :
        return { c.key : getattr( self , c.key ) for c in inspect( self ).mapper.column_attrs }
