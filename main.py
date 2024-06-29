import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pages

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(pages.router)

if __name__ == '__main__':
    uvicorn.run(app='main:app',
                host='0.0.0.0',
                port=80)
                # ssl_certfile='certificates/certificate.crt',
                # ssl_keyfile='certificates/certificate.key',
                # ssl_ca_certs='certificates/certificate_ca.crt')


