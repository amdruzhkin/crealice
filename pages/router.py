from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get('/')
async def home(request: Request):
    context = {
        'title': 'CREALICE',
        'SEO': {
            'description': 'CREALICE - Ваша универсальная студия для всех ваших потребностей в 3D-печати в Сочи. Предлагает высококачественные услуги 3D-печати в короткие сроки. Воплотите свои идеи в жизнь с помощью наших профессиональных решений для 3D-печати.',
            'keywords': '3D-печать Сочи, Услуги 3D-печати Сочи, 3D-печать моделей Сочи, Студия 3D-печати Сочи, 3D-печать на заказ Сочи, Художественная 3D-печать Сочи, Разработка 3D-модели в Сочи, Доставка Сочи, Прототипирование Сочи, Моделирование Сочи, Мелкосерийная 3D-печать Сочи',
        }
    }
    return templates.TemplateResponse(name='index.html', request=request, context=context)


@router.get('/services')
async def home(request: Request):
    context = {
        'title': 'CREALICE',
        'SEO': {
            'description': 'CREALICE - Ваша универсальная студия для всех ваших потребностей в 3D-печати в Сочи. Предлагает высококачественные услуги 3D-печати в короткие сроки. Воплотите свои идеи в жизнь с помощью наших профессиональных решений для 3D-печати.',
            'keywords': '3D-печать Сочи, Услуги 3D-печати Сочи, 3D-печать моделей Сочи, Студия 3D-печати Сочи, 3D-печать на заказ Сочи, Художественная 3D-печать Сочи, Разработка 3D-модели в Сочи, Доставка Сочи, Прототипирование Сочи, Моделирование Сочи, Мелкосерийная 3D-печать Сочи',
        }
    }
    return templates.TemplateResponse(name='services.html', request=request, context=context)


@router.get('/about')
async def home(request: Request):
    context = {
        'title': 'CREALICE',
        'SEO': {
            'description': 'CREALICE - Ваша универсальная студия для всех ваших потребностей в 3D-печати в Сочи. Предлагает высококачественные услуги 3D-печати в короткие сроки. Воплотите свои идеи в жизнь с помощью наших профессиональных решений для 3D-печати.',
            'keywords': '3D-печать Сочи, Услуги 3D-печати Сочи, 3D-печать моделей Сочи, Студия 3D-печати Сочи, 3D-печать на заказ Сочи, Художественная 3D-печать Сочи, Разработка 3D-модели в Сочи, Доставка Сочи, Прототипирование Сочи, Моделирование Сочи, Мелкосерийная 3D-печать Сочи',
        }
    }
    return templates.TemplateResponse(name='about.html', request=request, context=context)
