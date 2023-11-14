# coding : utf-8
# @Author : DS

from sqlalchemy import Column , String , Integer , Text  , Date , inspect , TIMESTAMP , ForeignKey , Boolean
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 服務項目 : 訂單 _ 處理

'''


class Service_Order_Process_Model( Base_Model ) :

    __tablename__  = "service_order_processes"              # 指定資料表名稱
    __table_args__ = { "comment" : "服務項目 : 訂單 _ 處理" }  # 資料表備註

    id = Column( Integer , primary_key = True , autoincrement = True )  # 主鍵

    service_order_id = Column( Integer , ForeignKey( "service_orders.id" ) , nullable = False , comment = "所屬服務訂單 id" )  # 所屬服務訂單 id

    shop_status      = Column( String( 25 ) , nullable = False , comment = "到店處理 Ex. 尚未到店 / 到店等候中 / 美容中 ..." )    # 到店處理狀況

    customer_note    = Column( String( 150 ) , comment = "客人交代" )    # 客人交代
    customer_item    = Column( String( 150 ) , comment = "客人自備物品" ) # 客人自備物品

    is_error         = Column( Boolean , default = False , comment = "是否異常 _ 0 : 否 , 1 : 是" ) # 是否異常
    error_reason     = Column( String( 50 ) , comment = "異常理由" )   # 異常理由
    error_submitter  = Column( String( 20 ) , comment = "異常提交者" ) # 異常提交者

    is_delete        = Column( Boolean , default = False , comment = "是否銷單 _ 0 : 否 , 1 : 是" )  # 是否銷單
    delete_reason    = Column( String( 50 ) , comment = "銷單理由" )   # 銷單理由
    delete_submitter = Column( String( 20 ) , comment = "銷單提交者" ) # 銷單提交者

    admin_note       = Column( String( 80 ) , comment = "經手備註" )         # 經手備註
    admin_user       = Column( String( 30 ) , comment = "櫃檯人員 / 經手人" ) # 櫃檯人員 / 經手人

    # [ 關聯 ]
    service_order    = relationship( "Service_Order_Model" , back_populates = "service_order_process" )  # 服務訂單





