# coding : utf-8
# @Author : DS


from sqlalchemy.orm import Session
from dao.model import Service_Content_Model
from dao.schema import Service_Content_In



# 讀取 _ 所有服務項目 : 內容
def read_all_service_contents( db : Session ) :

    return db.query( Service_Content_Model ).all()


# 讀取 _ 特定服務項目 : 內容 ( 依主鍵 id )
def read_service_content_by_id( id : int , db : Session ) :

    return db.query( Service_Content_Model ).filter( Service_Content_Model.id == id ).first()


# 新增 _ 服務項目 : 內容
def create_service_content( service_content : Service_Content_In , db : Session ) :

    db_service_content = Service_Content_Model( **service_content.dict() )

    db.add( db_service_content )
    db.commit()

    db.refresh( db_service_content )

    return db_service_content


# 修改 _ 服務項目 : 內容
def update_service_content_by_id( id : int , service_content : Service_Content_In  , db : Session ) :

    db.query( Service_Content_Model ).filter_by( id = id ).update( { **service_content.dict() } )
    db.commit()


# 刪除 _ 服務項目 : 內容
def delete_service_content_by_id( id : int , db : Session ) :

    db.query( Service_Content_Model ).filter_by( id = id ).delete()
    db.commit()