# coding : utf-8
# @Author : DS



from sqlalchemy import Column , String , Integer , Text  , inspect , TIMESTAMP , ForeignKey , Boolean , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 商品項目

'''

class Product_Model( Base_Model ) :

    __tablename__  = "products"                     # 指定資料表名稱
    __table_args__ = { "comment": "店家商品資料表" }  # 資料表備註

    id          = Column( Integer , primary_key = True , index = True , autoincrement = True ) # 主鍵

    account_id  = Column( Integer , ForeignKey( "accounts.id" ) , nullable = False , comment = "所屬店家 id" )  # 所屬店家 id

    name        = Column( String( 80 ) , nullable = False , comment = "商品名稱" )       # 商品名稱
    type        = Column( String( 20 ) , nullable = False , comment = "商品 _ 主類型"  ) # 商品 _ 主類型
    sub_type    = Column( String( 20 ) , comment = "商品 _ 次類型" )   # 商品 _ 次類型

    stock       = Column( Integer , default = 1 , comment = "庫存數量" )            # 庫存數量

    feature     = Column( String( 100 )  , comment = "商品特色" )  # 商品特色
    description = Column( Text  , comment = "商品描述" )           # 商品描述

    unit_price  = Column( Integer , nullable = False , comment = "商品單價" )       # 商品單價
    sale_price  = Column( Integer , nullable = False  , comment = "商品賣價" )       # 商品賣價

    is_on       = Column( Boolean , default = False , comment = "是否上架 _ 0 : 否 , 1 : 是" )  # 是否上架

    created_at  = Column( TIMESTAMP , nullable = False , server_default = func.now())  # 建立時間
    updated_at  = Column( TIMESTAMP , nullable = False , server_default = func.current_timestamp() , onupdate = func.current_timestamp())  # 修改時間

    # [ 關聯 ]
    account        = relationship( "Account_Model" ,       back_populates  = "product" ) # 店家帳號

    product_images = relationship( "Product_Image_Model" , back_populates = "product" , cascade = "all,delete-orphan" ) # 商品圖片
    product_order  = relationship( "Product_Order_Model" , back_populates = "product" , cascade = "all,delete-orphan" ) # 商品訂單

