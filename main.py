
from fastapi import FastAPI , Depends , Cookie , Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from controller import accounts_controller , \
                       authentication_controller , \
                       employees_controller , \
                       customers_controller , \
                       pets_controller , \
                       pet_classes_controller , \
                       pet_species_controller , \
                       services_controller , \
                       service_contents_controller , \
                       service_prices_controller , \
                       service_orders_controller , \
                       plans_controller , \
                       plan_contents_controller , \
                       plan_prices_controller , \
                       products_controller , \
                       product_images_controller , \
                       product_orders_controller

from dao.model.Base_Model import Base_Model
from dao.sql.sql_SQLAlchemy import engine



# 啟動 uvicorn 伺服器後，會針對所設定的資料庫( e_web )，依據各個 Model 檔，建立所有資料表
# Base_Model.metadata.create_all( engine )

app = FastAPI(
                title     = "客制網頁" ,
                # dependencies = [ Depends( get_token_header ) ]
                responses = {
                    404 : { "description" : "無相關頁面" } ,
                    200 : { "description" : "存取成功"  }
                }
              )

origins = [

            # < 允許特定網域 >
            "http://localhost" ,
            "http://localhost:3000" ,
            "http://localhost:3001" ,
            "http://localhost:8000" ,
            "http://localhost:8080" ,
            "http://127.0.0.1:8000" ,
            "http://[::1]" ,
            "http://[::1]:8000"

            # < 通配符 "*" 允许来自任何域名的请求 --> NOTE: 但請求有攜帶 credential ( Ex. Cookie ) ， 不能用通配符 * >
            # "*"

          ]

app.add_middleware(

    CORSMiddleware ,
    allow_origins     = origins ,
    allow_credentials = True ,     # 允許前端攜帶 Cookie ( Axios 也有類似設定 ) --> for JWT
    allow_methods     = ["*"] ,
    allow_headers     = ["*"] ,

)


# 載入 _ 各個類別的 API
app.include_router( accounts_controller.router )         # 帳號
app.include_router( authentication_controller.router )   # 授權

app.include_router( employees_controller.router )        # 員工 / 成員
app.include_router( customers_controller.router )        # 客戶

app.include_router( pets_controller.router )             # 寵物
app.include_router( pet_classes_controller.router )      # 寵物種類
app.include_router( pet_species_controller.router )      # 寵物種類

app.include_router( services_controller.router )         # 服務項目
app.include_router( service_contents_controller.router ) # 服務項目：內容
app.include_router( service_prices_controller.router )   # 服務項目：價錢
app.include_router( service_orders_controller.router )   # 服務項目：訂單

app.include_router( plans_controller.router )            # 自訂方案
app.include_router( plan_contents_controller.router )    # 自訂方案：內容
app.include_router( plan_prices_controller.router )      # 自訂方案：價格

app.include_router( products_controller.router )         # 商品項目
app.include_router( product_images_controller.router )   # 商品項目：圖片
app.include_router( product_orders_controller.router )   # 商品項目：訂單



@app.get( '/' )
def index() :

    return 'Hello _ 2023.08.20'





















