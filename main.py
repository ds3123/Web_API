
from fastapi import FastAPI , Depends , Cookie , Response
from sqlalchemy.orm import Session
from controller import customers_controller



app = FastAPI( )



app = FastAPI(
                title = "客制網頁" ,
                # dependencies = [ Depends( get_token_header ) ]
                responses = {
                    404 : { "description": "無相關頁面" } ,
                    200 : { "description": "存取成功" }
                }
              )


# 載入 _ 各個類別的 API
app.include_router( customers_controller.router )        # 店家客戶





@app.get( '/' )
def index() :

    return 'Hello _ 2023.08.20'





















