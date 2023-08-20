
from fastapi import FastAPI

app = FastAPI( )


@app.get( '/' )
def index() :

    return 'Hello _ 2023.08.19'





















