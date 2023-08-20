# coding : utf-8
# @Author : DS

from typing import Union
from fastapi import HTTPException
from sqlalchemy.orm import Session
from dao.schema import Customer_In
from util import pagination
import dao


# 讀取 _ 所有客戶
def read_all_customers( db : Session , page : int = 1 ) :

    # 讀取 _ 所有客戶
    db_customers = dao.read_all_customers( db )

    # 分頁資料
    customers_dict = pagination( db_customers , page )

    return customers_dict



