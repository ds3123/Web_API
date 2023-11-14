# coding : utf-8
# @Author : DS

from fastapi import APIRouter , Depends , HTTPException , status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from dao.sql import get_db
from util.helper import Hash
from util.auth import create_access_token
from dao.model import Employee_Model
from dao import Employee_Authorization
import service


router = APIRouter(
                     tags = [ 'authentication' ]
                  )


# 取得 _ token ( for 後台登入 : 員工 )
@router.post( '/employee_token' , summary = '取得 _ token ( fro 後台登入 : 員工 )' )  # '/employee_token' 須與 oauth2.py 中的 OAuth2PasswordBearer 參數 : tokenUrl 一致
def get_employee_token( request : Employee_Authorization , db : Session = Depends( get_db ) ) :

    # 查詢 _ 登入員工資料
    return service.read_employee_by_login( request.account , request.password , db )



# 取得 _ token ( for 前台 : 一般顧客 )
@router.post( '/customer_token' , summary = '取得 _ token ( for 前台 : 一般顧客 ' ) # '/customer_token' 須與 oauth2.py 中的 OAuth2PasswordBearer 參數 : tokenUrl 一致
def get_customer_token( request : OAuth2PasswordRequestForm = Depends() , db : Session = Depends( get_db ) ) :

    # 查詢 _ 登入顧客資料
    ...

