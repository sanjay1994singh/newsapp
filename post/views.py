from django.http import JsonResponse
from django.shortcuts import render

from advertisement.models import Advertisement
from .models import PostMaster
from category.models import CategoryMaster
# Create your views here.

def home_page(request):
    ads = Advertisement.objects.get(ads_name='TOP1')
    ads1 = Advertisement.objects.get(ads_name='TOP2')
    top1 = ads.advert.url
    top2 = ads1.advert.url
    post = PostMaster.objects.all()
    category = CategoryMaster.objects.all()
    context = {
        'top1':top1,
        'top2':top2,
        'post':post,
        'category':category,
    }
    return render(request, 'index.html',context)

def get_data_by_cat(request,id):
    data = PostMaster.objects.filter(post_category_id=id)
    if data:
        data_list = []
        for i in data:
            data_dic = {}
            data_dic['title'] = i.post_title
            data_dic['desc'] = i.post_desc
            data_dic['img'] = i.post_img.url
            data_dic['created_at'] = i.created_at
            data_list.append(data_dic)
    else:
        data_list = 0

    json_data = {
        'data': data_list
    }
    return JsonResponse(json_data)