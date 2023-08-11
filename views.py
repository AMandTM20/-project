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
def dish_view(request, dish):
    number = int(request.GET.get('servings', 1))
    ingredients = {ingredient:(amount*number) for ingredient,
    amount in DATA[dish].items()}
    context = {'recipe': ingredients}
    return render(request, 'calculator/templates/index.html', context)

