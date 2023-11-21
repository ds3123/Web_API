# coding : utf-8
# @Author : DS

from pydantic import BaseModel


'''

  @ 寵物 _ 品種 ( Ex. 柴犬 / 西施犬 / 獒犬 )

'''


# 寵物種類
class Pet_Class( BaseModel ) :

    account_id : int
    pet_class  : str


# 前端 _ 參數
class Pet_Species_In( BaseModel ) :

    pet_class_id : int
    pet_species  : str


# 後端 _ 資料庫
class Pet_Species_Out( BaseModel ) :

    id          : int
    pet_species : str
    pet_class   : Pet_Class  # 所屬寵物種類
