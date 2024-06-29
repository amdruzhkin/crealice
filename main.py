import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

import pages

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(pages.router)

# Function to check if the request is from a common search bot


def is_search_bot(request: Request):
    user_agent = request.headers.get("User-Agent", "").lower()
    common_bots = ["googlebot", "yandexbot", "bingbot", "baiduspider"]
    return any(bot in user_agent for bot in common_bots)


@app.get("/robots.txt")
async def robots(request: Request):
    if is_search_bot(request):
        robots_path = os.path.join("static", "robots.txt")
        if os.path.exists(robots_path):
            return FileResponse(robots_path, media_type="text/plain")
        else:
            raise HTTPException(status_code=404, detail="robots.txt not found")
    else:
        raise HTTPException(status_code=404, detail="Not Found")


@app.get("/sitemap.xml")
async def sitemap(request: Request):
    if is_search_bot(request):
        sitemap_path = os.path.join("static", "sitemap.xml")
        if os.path.exists(sitemap_path):
            return FileResponse(sitemap_path, media_type="application/xml")
        else:
            raise HTTPException(status_code=404, detail="sitemap.xml not found")
    else:
        raise HTTPException(status_code=404, detail="Not Found")

if __name__ == '__main__':
    uvicorn.run(app='main:app',
                host='0.0.0.0',
                port=80)
                # ssl_certfile='certificates/certificate.crt',
                # ssl_keyfile='certificates/certificate.key',
                # ssl_ca_certs='certificates/certificate_ca.crt')
