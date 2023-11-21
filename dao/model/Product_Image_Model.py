# coding : utf-8
# @Author : DS



from sqlalchemy import Column , String , Integer , Text  , inspect , TIMESTAMP , ForeignKey , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model

'''

   @ 商品項目 : 圖片

'''


class Product_Image_Model( Base_Model ) :

    __tablename__  = "product_images"                # 指定資料表名稱
    __table_args__ = { "comment": "商品項目 : 圖片" }  # 資料表備註

    id         = Column( Integer , primary_key = True , autoincrement = True ) # 主鍵
    product_id = Column( Integer , ForeignKey( "products.id" , ondelete = "CASCADE" ) , nullable = False , comment = "所屬商品項目 id" ) # 所屬商品項目 id

    url        = Column( String( 150 ) , unique = True , nullable = False , comment = "所屬商品項目 id" )  # 商品 _ 圖片 url

    created_at = Column( TIMESTAMP , nullable = False , server_default = func.now())  # 建立時間
    updated_at = Column( TIMESTAMP , nullable = False , server_default = func.current_timestamp() , onupdate = func.current_timestamp())  # 修改時間

    # [ 關聯 ]
    product    = relationship( "Product_Model" , back_populates = "product_images"  ) # 所屬商品
