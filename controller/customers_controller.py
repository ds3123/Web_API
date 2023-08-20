# coding : utf-8
# @Author : DS

from fastapi import Depends , APIRouter , HTTPException , Cookie , Request
from typing import List , Union , Any , Dict , Optional
from dao.schema import Customer_In , Customer_Out
import service
from sqlalchemy.orm import Session
from dao.sql import get_db


router = APIRouter(
                     prefix       = "/customers" ,
                     tags         = [ "店家 _ 客戶" ] ,
                     # dependencies = [ Depends( verify_request_jwt_token ) ] ,  # JWT Token 驗證
                     responses    = { 404 : {"description": "Not found"} } ,
                  )


# 讀取 _ 特定店家，所有客戶
@router.get( '/' , summary = '所有客戶' , description = '讀取 _ 所有客戶' )
def read_all_customers( request : Request , page : int = 1 , db : Session = Depends( get_db ) ) :

    return service.read_all_customers( db , page )



