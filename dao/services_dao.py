# coding : utf-8
# @Author : DS


from sqlalchemy.orm import Session
from dao.model import Service_Model , Service_Price_Model
from dao.schema import Service_In , Service_Out



# 讀取 _ 所有服務項目
def read_all_services( db : Session ) :

    return db.query( Service_Model ).all()


# 讀取 _ 特定店家，所有服務項目
def read_account_all_services( account_id : str , db : Session ) :

    return db.query( Service_Model ).filter( Service_Model.account_id == account_id ).all()


# 讀取 _ 特定服務 ( 依主鍵 id )
def read_service_by_id( id : int , db : Session ) :

    # 查詢 _ 特定服務項目
    result = db.query( Service_Model ).filter( Service_Model.id == id ).first()

    '''
       # 以下主要是為服務項目，加上 _ service_prices 資料表上的 : 服務價格
    '''

    # 取出 _ 該特定項目 : 相對應內容選項
    service_content = result.service_content

    # 遍歷 _ 第二層服務項目內容選項，查詢其是否有設定過 _ 服務價格
    for content in service_content :

        first_id  = content.service_id  # 服務項目 id
        second_id = content.id          # 服務項目內容 id

        res = db.query( Service_Price_Model ) \
                  .filter(
                           Service_Price_Model.service_id == first_id ,
                           Service_Price_Model.service_content_id == second_id
                         )\
                  .first()

        # 若在 service_prices 資料表，有價格 --> 新增 service_content_price 索引，並賦值價格
        if res :
            content.service_content_price = res.price

    # 賦值
    result.service_content = service_content

    return result



# 新增 _ 服務項目
def create_service( service : Service_In , db : Session ) :

    db_service = Service_Model( **service.dict() )

    db.add( db_service )
    db.commit()

    db.refresh( db_service )

    return db_service



# 修改 _ 服務項目
def update_service_by_id( id : int , service : Service_In , db : Session ) :

    db.query( Service_Model ).filter_by( id = id ).update( { **service.dict() } )
    db.commit()


# 刪除 _ 服務項目
def delete_service_by_id( id : int , db : Session ) :

    db.query( Service_Model ).filter_by( id = id ).delete()
    db.commit()

