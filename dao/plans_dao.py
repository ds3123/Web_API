# coding : utf-8
# @Author : DS


from sqlalchemy.orm import Session
from dao.model import Plan_Model
from dao.schema import Plan_In


# 讀取 _ 所有自訂方案
def read_all_plans( db : Session ) :

    return db.query( Plan_Model ).all()


# 讀取 _ 特定店家，所有自訂方案
def read_account_all_plans( account_id : str , db : Session ) :

    return db.query( Plan_Model ).filter( Plan_Model.account_id == account_id ).all()


# 讀取 _ 特定自訂方案 ( 依主鍵 id )
def read_plan_by_id( id : int , db : Session ) :


    # 查詢 _ 特定服務項目
    result = db.query( Plan_Model ).filter( Plan_Model.id == id ).first()


    '''
       # 以下主要是為方案項目，加上 _ plan_prices 資料表上的 : 方案價格
    '''


    # 取出 _ 該特定項目 : 相對應內容選項
    # plan_content = result.plan_content


    # 遍歷 _ 第二層服務項目內容選項，查詢其是否有設定過 _ 服務價格
    # for content in plan_content :
    #
    #     first_id  = content.plan_id  # 服務項目 id
    #     second_id = content.id          # 服務項目內容 id
    #
    #     res = db.query( Service_Price_Model ) \
    #               .filter(
    #                        Service_Price_Model.service_id == first_id ,
    #                        Service_Price_Model.service_content_id == second_id
    #                      )\
    #               .first()
    #
    #     # 若在 service_prices 資料表，有價格 --> 新增 service_content_price 索引，並賦值價格
    #     if res :
    #         content.service_content_price = res.price

    # 賦值
    # result.plan_content = plan_content

    return result


# 新增 _ 自訂方案
def create_plan( plan : Plan_In , db : Session ) :

    db_plan = Plan_Model( **plan.dict() )

    db.add( db_plan )
    db.commit()

    db.refresh( db_plan )

    return db_plan


# 修改 _ 自訂方案
def update_plan_by_id( id : int , plan : Plan_In , db : Session ) :

    db.query( Plan_Model ).filter_by( id = id ).update( { **plan.dict() } )
    db.commit()


# 刪除 _ 自訂方案
def delete_plan_by_id( id : int , db : Session ) :

    db.query( Plan_Model ).filter_by( id = id ).delete()
    db.commit()