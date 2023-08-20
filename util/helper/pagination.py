# coding : utf-8
# @Author : DS


from dotenv import load_dotenv
import os
import math

'''

   @ 分頁

'''

load_dotenv()


def pagination( data : [] , page : int = 1 ) -> [] :

    # 資料總筆數
    data_total     = len( data )

    # 每個分頁資料筆數
    per_page_Num  = int( os.getenv( 'PER_PAGINATION_NUM' ) )

    # 計算 _ 分頁按鈕數
    page_btn_num  = math.ceil( data_total / per_page_Num )

    # 每個分頁資料
    pet_page_data = data[ ( page - 1 ) * per_page_Num : page * per_page_Num ]

    return { "per_page_data" : pet_page_data , "page_btn_num" : page_btn_num , "total_data_sum" : data_total }