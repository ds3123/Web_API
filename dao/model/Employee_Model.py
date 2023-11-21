# coding : utf-8
# @Author : DS

from sqlalchemy import Column , String , Integer , ForeignKey , Date , Text , TIMESTAMP , inspect , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model

'''

    @ 店家 _ 員工 / 成員

'''

class Employee_Model( Base_Model ) :

    __tablename__   = "employees" # 資料表
    __table_args__  = { "comment" : "員工資料表" }  # 資料表備註

    id              = Column( Integer , primary_key = True , autoincrement = True )       # 主鍵
    account_id      = Column( Integer , ForeignKey( "accounts.id" , ondelete = "CASCADE" )  , nullable = False , comment = "所屬店家 id"  ) # 所屬店家 id

    account         = Column( String( 100 ) , unique = True, nullable = False , comment = "帳號"  ) # 帳號
    password        = Column( String( 150 ) , nullable = False , comment = "密碼" ) # 密碼

    name            = Column( String( 50 ) , nullable = False , comment = "姓名" )  # 姓名
    nickname        = Column( String( 50 ) , comment = "暱稱" )  # 暱稱

    sex             = Column( String( 10 ) , nullable = False , comment = "性別" )  # 性別
    serial_id       = Column( String( 30 ) , unique = True, nullable = False , comment = "身分證字號" ) # 身分證字號
    mobile_phone    = Column( String( 20 ) , unique = True, nullable = False , comment = "手機號碼" )   # 手機號碼
    tel_phone       = Column( String( 30 ) , comment = "家用電話" )  # 家用電話

    birthday        = Column( Date , comment = "生日" )        # 生日

    email           = Column( String( 80 ) , comment = "Email"  ) # Email
    line            = Column( String( 50 ) , comment = "Line"  )  # Line
    address         = Column( String( 150 ) , comment = "通訊地址" ) # 通訊地址

    salary_type     = Column( String( 30 ) , comment = "計薪類別 ( Ex. 正職 / 計時 )" )       # 計薪類別 ( Ex. 正職 / 計時 )
    position_type   = Column( String( 30 ) , comment = "職位類別 ( Ex. 櫃台 / 美容 / 接送 )" )  # 職位類別 ( Ex. 櫃台 / 美容 / 接送
    position_status = Column( String( 20 ) , comment = "職位現況 ( Ex. 在職 / 離職 )" )        # 職位現況 ( Ex. 在職 / 離職

    created_at = Column( TIMESTAMP , nullable = False, server_default = func.now())  # 建立時間
    updated_at = Column( TIMESTAMP , nullable = False, server_default = func.current_timestamp(), onupdate = func.current_timestamp())  # 修改時間

    # [ 關聯 ]
    shop_account = relationship( "Account_Model", back_populates = "employee" )  # 所屬店家帳號



    # 回傳 _ Model : 所有屬性
    def as_dict( self ) :
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


