# coding : utf-8
# @Author : DS


from sqlalchemy import Column , String , Integer , inspect , ForeignKey , func
from sqlalchemy.orm import relationship
from .Base_Model import Base_Model


'''

   @ 寵物 _ 品種 ( Ex. 柴犬 / 西施犬 / 獒犬 )

'''


class Pet_Species_Model( Base_Model ) :

    __tablename__  = "pet_species"  # 指定資料表名稱
    __table_args__ = { "comment": "寵物 _ 品種 ( Ex. 柴犬 / 西施犬 / 獒犬 )" }  # 資料表備註


    id            = Column( Integer , primary_key = True , autoincrement = True ) # 主鍵
    pet_class_id  = Column( Integer , ForeignKey( "pet_classes.id" ) , nullable = False , comment = "所屬寵物種類 id" ) # 所屬寵物種類 id

    pet_species   = Column( String( 30 ) , nullable = False , comment = "寵物品種" )  # 寵物品種


    # [ 關聯 ]
    pet_class     = relationship( "Pet_Class_Model" , back_populates = "pet_species" ) # 所屬種物種類



    # 回傳 _ Model : 所有屬性
    def as_dict( self ) :
        return { c.key : getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

