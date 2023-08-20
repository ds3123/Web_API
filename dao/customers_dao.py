# coding : utf-8
# @Author : DS

from sqlalchemy import desc
from sqlalchemy.orm import Session
from dao.model import Customer_Model
from dao.schema import Customer_In , Customer_Out
from typing import Union



# 讀取 _ 所有客戶
def read_all_customers( db : Session ) :

    return db.query( Customer_Model ).order_by( desc( Customer_Model.id ) ).all()





