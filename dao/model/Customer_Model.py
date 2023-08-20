# coding : utf-8
# @Author : DS

from sqlalchemy import Column , String , Integer , ForeignKey , Date , Text , TIMESTAMP , inspect
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model

'''

    @ 店家客戶

'''

class Customer_Model( Base_Model ) :

    __tablename__ = 'customers' # 資料表

    id            = Column(Integer, primary_key=True, autoincrement=True)  # 主鍵

    account_id    = Column(Integer, ForeignKey("accounts.id"))  # 所屬店家 id
    name          = Column(String(20))  # 姓名
    sex           = Column(String(15))  # 性別
    serial_id     = Column(String(30), unique=True)  # 身分證字號
    mobile_phone  = Column(String(20), unique=True)  # 手機號碼
    tel_phone     = Column(String(20))  # 家用電話
    address       = Column(String(120))  # 通訊地址
    birthday      = Column(Date)  # 生日
    email         = Column(String(100), unique=True)  # Email
    line          = Column(String(50), unique=True)  # Line
    note          = Column(Text)  # 備註

    created_at    = Column(TIMESTAMP)  # 建立時間


    # 回傳 _ Model : 所有屬性
    def as_dict( self ) :
        return { c.key : getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    # 作用 :
    def __str__( self ) :
        return f" id : { self.id }  / name : { self.name }  "




