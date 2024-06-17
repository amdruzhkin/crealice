from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get('/')
async def home(request: Request):
    context = {
        'title': 'CREALICE',
        'SEO': {
            'description': 'CREALICE 3D-Услуги в Сочи',
            'keywords': 'ключевые слова',
        }
    }
    return templates.TemplateResponse(name='index.html', request=request, context=context)

@router.get('/services')
async def home(request: Request):
    context = {
        'title': 'CREALICE',
        'SEO': {
            'description': 'Описание услуг',
            'keywords': 'ключевые слова',
        }
    }
    return templates.TemplateResponse(name='services.html', request=request, context=context)

@router.get('/about')
async def home(request: Request):
    context = {
        'title': 'CREALICE',
        'SEO': {
            'description': 'О нас',
            'keywords': 'ключевые слова',
        }
    }
    return templates.TemplateResponse(name='about.html', request=request, context=context)