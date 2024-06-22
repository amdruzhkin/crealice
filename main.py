import uvicorn
from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pages

app = FastAPI()
app.add_middleware(HTTPSRedirectMiddleware)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(pages.router)

if __name__ == '__main__':
    uvicorn.run(app='main:app',
                host='0.0.0.0',
                port=443,
                ssl_certfile='certificate.crt',
                ssl_keyfile='certificate.key')


