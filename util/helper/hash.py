# coding : utf-8
# @Author : DS

from passlib.context import CryptContext


'''

  # 密碼 ： Hash 加密

'''


pwd_cxt = CryptContext( schemes = 'bcrypt'  , deprecated = 'auto' )

class Hash() :

    # 對密碼進行 hash 加密
    def bcrypt( password : str ) :
        return pwd_cxt.hash( password )

    # 驗證 _ 所未經 hash 加密的密碼，其 hash 值，是否與資料庫中該密碼 hash 值相符合
    def verify( hashed_password , plain_password ) :
        return pwd_cxt.verify( plain_password , hashed_password )



if __name__ == '__main__':

    text = "ds3123"

    crypted = Hash.bcrypt( text )

    print( 'gggg' , crypted )

    print( 'fff' , Hash.verify( crypted , text ) )


