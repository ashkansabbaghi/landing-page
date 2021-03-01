from django.shortcuts import render
from .models import food

def food_list (req) :
    food_list = food.objects.all()
    context = {
        "foods"  : food_list
    }

    return render(req , "foods/index.html",context)


def food_details (req , id ): 
    food_detail = food.objects.get(id = id)
    context = {
        "food" : food_detail
    }
    return render (req , "foods/detail.html" , context)
