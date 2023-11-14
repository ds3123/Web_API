# coding : utf-8
# @Author : DS


from sqlalchemy.orm import Session
from dao.model import Plan_Content_Model
from dao.schema import Plan_Content_In



# 讀取 _ 所有自訂方案 : 內容
def read_all_plan_contents( db : Session ) :

    return db.query( Plan_Content_Model ).all()



# 讀取 _ 特定自訂方案 : 內容 ( 依主鍵 id )
def read_plan_content_by_id( id : int , db : Session ) :

    return db.query( Plan_Content_Model ).filter( Plan_Content_Model.id == id ).first()



# 新增 _ 自訂方案 : 內容
def create_plan_content( plan_content : Plan_Content_In , db : Session ) :

    db_plan_content = Plan_Content_Model( **plan_content.dict() )

    db.add( db_plan_content )
    db.commit()

    db.refresh( db_plan_content )

    return db_plan_content


# 修改 _ 自訂方案 : 內容
def update_plan_content_by_id( id : int , plan_content : Plan_Content_In  , db : Session ) :

    db.query( Plan_Content_Model ).filter_by( id = id ).update( { **plan_content.dict() } )
    db.commit()


# 刪除 _ 自訂方案 : 內容
def delete_plan_content_by_id( id : int , db : Session ) :

    db.query( Plan_Content_Model ).filter_by( id = id ).delete()
    db.commit()

