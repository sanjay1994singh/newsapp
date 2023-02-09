from django.http import JsonResponse
from django.shortcuts import render

from advertisement.models import Advertisement
from .models import PostMaster
from category.models import CategoryMaster
# Create your views here.

def home_page(request):
    ads = Advertisement.objects.get(ads_name='TOP1')
    top1 = ads.advert.url
    ads1 = Advertisement.objects.get(ads_name='TOP2')
    top2 = ads1.advert.url
    side2 = Advertisement.objects.get(ads_name='SIDE2')
    side2 = side2.advert.url
    post = PostMaster.objects.all().order_by('-created_at')[:25]
    category = CategoryMaster.objects.all()
    context = {
        'top1':top1,
        'top2':top2,
        'side2':side2,
        'post':post,
        'category':category,
    }
    return render(request, 'index.html',context)

def get_data_by_cat(request,id):
    data = PostMaster.objects.filter(post_category_id=id).order_by('-created_at')
    if data:
        data_list = []
        for i in data:
            data_dic = {}
            data_dic['id'] = i.pk
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

def view_post_details(request,obj_id):
    obj_id = obj_id
    post = PostMaster.objects.all().order_by('-created_at')[:5]
    single_post = PostMaster.objects.get(id=obj_id)
    context = {
        'obj_id':obj_id,
        'post':post,
        'post_data':single_post,
    }
    return render(request,'post_detail.html',context)