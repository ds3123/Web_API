# coding : utf-8
# @Author : DS

from sqlalchemy import Column , String , Integer , inspect , ForeignKey , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 寵物 _ 種類 ( Ex. 狗 / 貓 / 鳥 ... )

'''


class Pet_Class_Model( Base_Model ) :

    __tablename__  = "pet_classes"  # 指定資料表名稱
    __table_args__ = { "comment" : "寵物 _ 種類 ( Ex. 狗 / 貓 / 鳥 ... )" }  # 資料表備註

    id             = Column( Integer , primary_key = True , autoincrement = True )  # 主鍵
    account_id     = Column( Integer , ForeignKey( "accounts.id" ) , nullable = False , comment = "所屬店家 id" )  # 所屬店家 id

    pet_class      = Column( String( 20 ) , unique = True , nullable = False , comment = "寵物種類"  )  # 寵物種類


    # [ 關聯 ]
    account       = relationship( "Account_Model"       , back_populates = "pet_class" )  # 店家帳號
    pet_species   = relationship( "Pet_Species_Model"   , back_populates = "pet_class" , cascade = "all,delete-orphan" )  # 所包含寵物品種


    # 回傳 _ Model : 所有屬性
    def as_dict( self ) :
        return { c.key : getattr(self, c.key) for c in inspect(self).mapper.column_attrs }






