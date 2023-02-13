from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    data = Recipedb.objects.all()
    return render(request, 'index.html', {'data':data})

def recipe(request):
    return render(request, 'recipe.html')

def getdata(request):
    if request.method == 'POST':
        name1 = request.POST['recipe_name']
        image1 = request.FILES['recipe_image']
        ing = request.POST['ingredients']
        ins = request.POST['instructions']
        data = Recipedb(recipe_name = name1, recipe_image = image1, ingredients = ing, instructions = ins)
        data.save()
        return redirect('index')

def table(request):
    data = Recipedb.objects.all()
    return render(request, 'table.html', {'data':data})

def edit(request,id):
    data = Recipedb.objects.filter(id=id)
    return render(request, 'edit.html', {'data':data})

def update(request,id):
    if request.method == 'POST':
        name1 = request.POST['recipe_name']
        image1 = request.FILES['recipe_image']
        ing = request.POST['ingredients']
        ins = request.POST['instructions']
        Recipedb.objects.filter(id=id).update(recipe_name = name1, recipe_image = image1, ingredients = ing, instructions = ins)
        return redirect('/table')

def delete(request,id):
    data = Recipedb.objects.filter(id=id).delete()
    return redirect('/table')