from django.http import JsonResponse
from django.shortcuts import render
from .models import PostMaster
from category.models import CategoryMaster
# Create your views here.

def home_page(request):
    post = PostMaster.objects.all()
    category = CategoryMaster.objects.all()
    context = {
        'post':post,
        'category':category,
    }
    return render(request, 'index.html',context)

def get_data_by_cat(request,id):
    # data = PostMaster.objects.filter(post_category_id=4)
    data = '000000000000000000000000000000000000000000000'
    json_data = {
        'data':data
    }
    return JsonResponse(json_data)