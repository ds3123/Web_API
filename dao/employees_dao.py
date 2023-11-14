# coding : utf-8
# @Author : DS


from sqlalchemy.orm import Session
from dao.model import Employee_Model
from dao.schema import Employee_In
from util import Hash



# 讀取 _ 所有員工
def read_all_employees( db : Session ) :

    return db.query( Employee_Model ).all()

# 讀取 _ 特定員工 ( 依主鍵 id )
def read_employee_by_id( id : int , db : Session ) :

    return db.query( Employee_Model ).filter( Employee_Model.id == id ).first()

# 讀取 _ 特定員工 ( 先依 "帳號" 搜尋 )
def read_employee_by_account( account : str , db : Session ) :

    return db.query( Employee_Model ).filter( Employee_Model.account == account ).first()

# 讀取 _ 特定店家，所有員工
def read_account_all_employees( db : Session , account_id : str ) :

    return db.query( Employee_Model ).filter( Employee_Model.account_id == account_id ).all()


# 新增 _ 員工
def create_employee( employee : Employee_In , db : Session ) :

    new_employee = Employee_Model(
                                   account_id      = employee.account_id ,
                                   account         = employee.account ,
                                   password        = Hash.bcrypt( employee.password ) , # Hash 加密
                                   name            = employee.name ,
                                   nickname        = employee.nickname ,
                                   sex             = employee.sex ,
                                   serial_id       = employee.serial_id ,
                                   mobile_phone    = employee.mobile_phone ,
                                   tel_phone       = employee.tel_phone ,
                                   birthday        = employee.birthday ,
                                   email           = employee.email ,
                                   line            = employee.line ,
                                   address         = employee.address ,
                                   salary_type     = employee.salary_type ,
                                   position_type   = employee.position_type ,
                                   position_status = employee.position_status
                                 )

    db.add( new_employee )
    db.commit()
    db.refresh( new_employee )  # refresh 主要是取得 _ 資料庫新增資料後的 id

    return new_employee

# 修改 _ 員工
def update_employee_by_id( id : int , employee : Employee_In , db : Session ) :

    db.query( Employee_Model ).filter_by( id = id ).update( { **employee.dict() } )
    db.commit()



# 刪除 _ 員工
def delete_employee_by_id( id : int , db : Session ) :

    db.query( Employee_Model ).filter_by( id = id ).delete()
    db.commit()

