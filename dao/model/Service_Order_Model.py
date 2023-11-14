# coding : utf-8
# @Author : DS


from sqlalchemy import Column , String , Integer , Text  , Date , inspect , TIMESTAMP , ForeignKey , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 服務項目 : 訂單

'''

class Service_Order_Model( Base_Model ) :

    __tablename__  = "service_orders"                 # 指定資料表名稱
    __table_args__ = { "comment" : "服務項目 : 訂單" }  # 資料表備註

    id             = Column( Integer , primary_key = True , autoincrement = True ) # 主鍵

    account_id     = Column( Integer , ForeignKey( "accounts.id" )  , nullable = False , comment = "所屬店家 id" )     # 所屬店家 id
    customer_id    = Column( Integer , ForeignKey( "customers.id" ) , nullable = False , comment = "所屬客人 id" )     # 所屬客人 id
    pet_id         = Column( Integer , ForeignKey( "pets.id" )      , nullable = False , comment = "所屬寵物 id" )     # 所屬寵物 id
    service_id     = Column( Integer , ForeignKey( "services.id" )  , nullable = False , comment = "所屬服務項目 id" )  # 所屬服務項目 id

    service_code   = Column( String( 10 ) , nullable = False , comment = "服務當日處理碼" )                # 當日處理碼
    service_type   = Column( String( 30 ) , nullable = False , comment = "服務 _ 類型 ( 服務第一層分類 )" ) # 服務 _ 類型 ( 服務第一層分類 )

    service_date   = Column( Date , nullable = False , comment = "到店日期" ) # 到店日期
    arrival_time   = Column( String( 30 ) , comment = "到店時間" )            # 到店時間

    service_price  = Column( Integer , nullable = False , comment = "服務訂單 _ 價格" ) # 服務訂單 _ 價格
    adjust_amount  = Column( Integer , comment = "服務訂單 _ 調整價格" )                 # 服務訂單 _ 調整價格
    adjust_reason  = Column( String( 50 ) , comment = "服務訂單 _ 調整價格理由" )        # 服務訂單 _ 調整價格理由

    amount_paid    = Column( Integer , nullable = False , comment = "實付金額" )       # 實付金額

    payment_method = Column( String( 15 ) , nullable = False , comment = "付款方式" )  # 付款方式
    payment_date   = Column( Date         , nullable = False , comment = "付款日期" )  # 付款日期

    service_note   = Column( String( 100 ) , comment = "服務訂單備註" )                 # 服務備註

    created_at     = Column( TIMESTAMP , nullable = False, server_default = func.now())  # 建立時間
    updated_at     = Column( TIMESTAMP , nullable = False, server_default = func.current_timestamp() , onupdate = func.current_timestamp() )  # 修改時間

    # [ 關聯 ]
    account               = relationship( "Account_Model"  , back_populates = "service_order" ) # 店家帳號
    customer              = relationship( "Customer_Model" , back_populates = "service_order" ) # 店家客戶
    pet                   = relationship( "Pet_Model"      , back_populates = "service_order" ) # 店家寵物

    service               = relationship( "Service_Model"              , back_populates = "service_order" ) # 服務項目
    service_order_process = relationship( "Service_Order_Process_Model", back_populates = "service_order" ) # 服務訂單 _ 處理狀況

    plan_record           = relationship( "Plan_Record_Model" , back_populates = "service_order" )  # 該服務相對應使用紀錄



    # 回傳 _ Model : 所有屬性
    def as_dict( self ) :
        return { c.key : getattr( self, c.key ) for c in inspect( self ).mapper.column_attrs }