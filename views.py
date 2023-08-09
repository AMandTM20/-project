from django.shortcuts import render,reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def index(request):
    context = DATA
    template_name = 'calculator/templates/index.html'
    return render(request,template_name, context)

def omlet(request):
    servings = int(request.GET.get('servings', '1'))
    context = {
        'recipe': {
            'яйца, шт': 2*servings,
            'молоко, л': 0.1*servings,
            'соль, ч.л.': 0.5*servings
        }
    }
    template_name = 'calculator/templates/index.html'
    return render(request, template_name, context)


def pasta(request):
    servings = int(request.GET.get('servings', '1'))
    context = {
        'recipe': {
            'макароны, г': 0.3*servings,
            'сыр, г': 0.05*servings
        }
    }
    template_name = 'calculator/templates/index.html'
    return render(request, template_name, context)
#
#
def buter(request):
    servings = int(request.GET.get('servings', '1'))
    context = {
        'recipe': {
            'хлеб, ломтик': 1*servings,
            'колбаса, ломтик': 1*servings,
            'сыр, ломтик': 1*servings,
            'помидор, ломтик': 1*servings
        }
    }
    print('context: ',context)
    template_name = 'calculator/templates/index.html'
    return render(request, template_name, context)





















