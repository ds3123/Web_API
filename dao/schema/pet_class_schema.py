# coding : utf-8
# @Author : DS

from pydantic import BaseModel
from typing import List
from .account_schema import Account_In
from .pet_species_schema import Pet_Species_In



'''

  @ 寵物 _ 種類 ( Ex. 狗 / 貓 / 鳥 ... )

'''


# 前端 _ 參數
class Pet_Class_In( BaseModel ) :

    account_id : int
    pet_class  : str



# 後端 _ 資料庫
class Pet_Class_Out( Pet_Class_In ) :

    id          : int

    # 關聯
    account     : Account_In              # 所屬店家帳號
    pet_species : List[ Pet_Species_In ]  # 所包含寵物品種
