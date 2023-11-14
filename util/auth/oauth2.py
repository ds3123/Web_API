# coding : utf-8
# @Author : DS

from fastapi import Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError
from typing import Optional
from datetime import datetime , timedelta
from sqlalchemy.orm import Session
from dao.sql import get_db
from dotenv import load_dotenv
import os

# 下載環境變數
load_dotenv()

# 設定 _ 所要保護的 API url ( 參數 : tokenUrl -->  須與 authentication.py 中的 Api url : '/employee_token' , '/customer_token'  一致 )
oauth2_employee = OAuth2PasswordBearer( tokenUrl = 'employee_token' )  # for 後端 : 員工
oauth2_customer = OAuth2PasswordBearer( tokenUrl = 'customer_token' )  # for 前端 : 顧客



# 隨機序號 ( 可在終端中，輸入 : openssl rand -hex 32 取得 )
SECRET_KEY    = os.getenv( 'JWT_SECRET' )

# 演算法
ALGORITHM     = 'HS256'


# 建立 _ JWT token
def create_access_token( data : dict , expires_delta : Optional[ timedelta ] = None ) :

  # 淺拷貝 data 字典
  to_encode = data.copy()

  if expires_delta :
    expire = datetime.utcnow() + expires_delta
  else :
    expire = datetime.utcnow() + timedelta( minutes = 15 ) # Token 有效時間：15 分

  # 更新 data 字典 : 加入 { "exp" : expire }
  to_encode.update( { "exp" : expire } )

  encoded_jwt = jwt.encode( to_encode , SECRET_KEY , algorithm = ALGORITHM )

  return encoded_jwt
