# coding : utf-8
# @Author : DS



from sqlalchemy import Column , String , Integer , inspect , ForeignKey , Date , Text , TIMESTAMP , func , Boolean
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 寵物

'''

class Pet_Model( Base_Model ) :

    __tablename__  = "pets" # 指定資料表名稱
    __table_args__ = { "comment": "寵物資料表" }  # 資料表備註

    id          = Column( Integer , primary_key = True , autoincrement = True ) # 主鍵

    account_id  = Column( Integer , ForeignKey( "accounts.id" ) ,  nullable = False , comment = "所屬店家 id" )  # 所屬店家 id
    customer_id = Column( Integer , ForeignKey( "customers.id" ) , nullable = False , comment = "所屬主人 id" ) # 所屬主人 id

    name        = Column( String( 50 ) , nullable = False , comment = "寵物名字" )  # 名字
    serial      = Column( String( 80 ) , nullable = False , comment = "寵物編號" )  # 編號
    chip        = Column( String( 80 ) , comment = "晶片號碼" )  # 晶片號碼

    pet_class   = Column( String( 20 ) , nullable = False , comment = "寵物種類 ( Ex. 狗 / 鳥 / 魚 )" )   # 種類
    pet_species = Column( String( 30 ) , comment = "寵物品種 ( Ex. 西施犬 / 伯恩犬 )"  )  # 品種

    sex         = Column( String( 10 ) , comment = "寵物性別 : 公 / 母 / 不確定" ) # 性別
    weight      = Column( String( 10 ) , comment = "寵物體重" ) # 體重
    color       = Column( String( 15 ) , comment = "寵物毛色" ) # 毛色
    birthday    = Column( Date         , comment = "寵物生日" ) # 生日

    note        = Column( Text , comment = "寵物備註" )         # 備註

    is_dead       = Column( Boolean , default = False , comment = "是否死亡 _ 0 : 否 , 1 : 是" )    # 是否死亡
    is_rejected   = Column( Boolean , default = False , comment = "是否被拒接 _ 0 : 否 , 1 : 是" )  # 是否拒接
    reject_reason = Column( String( 150 ) , comment = "拒接理由" )  # 拒接理由

    created_at    = Column( TIMESTAMP , nullable = False , server_default = func.now() )    # 建立時間
    updated_at    = Column( TIMESTAMP , nullable = False , server_default = func.current_timestamp() , onupdate = func.current_timestamp() )  # 修改時間


    # [ 關聯 ]
    account       = relationship( "Account_Model"       , back_populates = "pet" )  # 店家帳號
    customer      = relationship( "Customer_Model"      , back_populates = "pet" )  # 店家客人

    service_order = relationship( "Service_Order_Model" , back_populates = "pet" , cascade = 'all, delete-orphan' )  # 所屬服務項目 : 訂單

    plan_order    = relationship( "Plan_Order_Model"    , back_populates = "pet" , cascade = "all,delete-orphan" ) # 相關購買方案
    plan_record   = relationship( "Plan_Record_Model"   , back_populates = "pet" , cascade = "all,delete-orphan" ) # 使用方案紀錄



    # 回傳 _ Model : 所有屬性
    def as_dict( self ) :
        return { c.key : getattr(self, c.key) for c in inspect(self).mapper.column_attrs }




