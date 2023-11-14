# coding : utf-8
# @Author : DS

from sqlalchemy import Column , String , Integer , ForeignKey , Date , DateTime  , Text , TIMESTAMP , inspect , Boolean , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model

'''

    @ 店家 _ 客戶

'''

class Customer_Model( Base_Model ) :

    __tablename__  = "customers"  # 資料表
    __table_args__ = { "comment" : "客戶資料表" }   # 資料表備註

    id            = Column( Integer , primary_key = True, index = True , autoincrement = True  ) # 主鍵
    account_id    = Column( Integer , ForeignKey( "accounts.id" ) , nullable = False , comment = "所屬店家 id" ) # 所屬店家 id

    name          = Column( String( 60 ) , nullable = False , comment = "姓名" ) # 姓名
    sex           = Column( String( 15 ) , nullable = False , comment = "性別" ) # 性別
    serial_id     = Column( String( 30 ) , unique = True , nullable = False , comment = "身分證字號" ) # 身分證字號
    mobile_phone  = Column( String( 20 ) , unique = True , nullable = False , comment = "手機號碼" )   # 手機號碼
    tel_phone     = Column( String( 20 ) , comment = "家用電話" )                    # 家用電話

    address       = Column( String( 120 ) , comment = "通訊地址" ) # 通訊地址
    birthday      = Column( Date , comment = "生日" )             # 生日

    email         = Column( String( 100 ) , comment = "Email" )  # Email
    line          = Column( String( 50 )  , comment = "Line"  )  # Line

    note          = Column( Text , comment = "客戶備註" )  # 客戶備註

    is_rejected   = Column( Boolean , default = False , comment = "是否被拒接 _ 0 : 否 , 1 : 是" )  # 是否被拒接
    reject_reason = Column( String( 150 ) , comment = "拒接理由" )   # 拒接理由

    created_at    = Column( TIMESTAMP, nullable = False, server_default = func.now())  # 建立時間
    updated_at    = Column( TIMESTAMP, nullable = False, server_default = func.current_timestamp() , onupdate = func.current_timestamp() )  # 修改時間


    # [ 關聯 ]
    account       = relationship( "Account_Model", back_populates = "customer" ) # 所屬店家帳號
    pet           = relationship( "Pet_Model", back_populates = "customer" , cascade = "all,delete-orphan" ) # 所有寵物

    service_order = relationship( "Service_Order_Model" , back_populates = "customer" , cascade = "all,delete-orphan" ) # 購買 _ 服務項目 : 訂單
    product_order = relationship( "Product_Order_Model" , back_populates = "customer" , cascade = "all,delete-orphan" ) # 購買 _ 商品項目 : 訂單

    plan_order    = relationship( "Plan_Order_Model"    , back_populates = "customer" , cascade = "all,delete-orphan" ) # 購買 _ 自訂方案 : 訂單
    plan_record   = relationship( "Plan_Record_Model"   , back_populates = "customer" , cascade = "all,delete-orphan" ) # 使用方案紀錄


    # 回傳 _ Model : 所有屬性
    def as_dict( self ) :
        return { c.key : getattr( self , c.key ) for c in inspect( self ).mapper.column_attrs }






