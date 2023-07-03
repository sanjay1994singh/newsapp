from django.http import JsonResponse
from django.shortcuts import redirect, render

from advertisement.models import Advertisement,OtherAds
from .models import PostMaster
from category.models import CategoryMaster
# Create your views here.

def home_page(request,id=0):
    if id is not 0:
        post = PostMaster.objects.filter(post_category_id=id).order_by('-created_at')[:25]
    else:
        post = PostMaster.objects.all().order_by('-created_at')[:25]
    try:
        loader = Advertisement.objects.get(ads_name='LOADER')
        loader_img = loader.advert.url
        ads = Advertisement.objects.get(ads_name='TOP1')
        top1 = ads.advert.url
        ads1 = Advertisement.objects.get(ads_name='TOP2')
        top2 = ads1.advert.url
        side2 = Advertisement.objects.get(ads_name='SIDE2')
        side2 = side2.advert.url
        category = CategoryMaster.objects.all()
    except Exception as e:
        print(e,"----error in home_page function in post app --")

    context = {
        'top1':top1,
        'top2':top2,
        'side2':side2,
        'post':post,
        'category':category,
        'loader_img':loader_img
    }
    return render(request, 'index.html', context)

def get_data_by_cat(request,id):
    data = PostMaster.objects.filter(post_category_id=id).order_by('-created_at')[:25]
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
    category = CategoryMaster.objects.all()
    post = PostMaster.objects.all().order_by('-created_at')[:5]
    otherpost = PostMaster.objects.all().exclude(id=obj_id).order_by('-created_at')[:25]
    single_post = PostMaster.objects.get(id=obj_id)
    other_ads = OtherAds.objects.all()
    context = {
        'obj_id':obj_id,
        'category':category,
        'post':post,
        'post_data':single_post,
        'otherpost':otherpost,
        'other_ads':other_ads,
    }
    return render(request,'post_detail.html',context)

def add_post(request,id=0):
    if request.method == 'POST':
        form = request.POST
        post_title = form.get('post_title')
        post_text = form.get('post_text')
        select_cat = form.get('select_cat')
        post_img = request.FILES.get('post_img')
        
        try:
            if id == 0:
                obj = PostMaster.objects.create(post_title=post_title,
                                        post_desc=post_text,
                                        post_category_id=select_cat,
                                        post_img=post_img)
                id = obj.id
                if obj:
                    id = id
                    msg = 'post saved successfully.'

            else:
                PostMaster.objects.filter(id=id).update(post_title=post_title,
                                                             post_desc=post_text,
                                                             post_category_id=select_cat,
                                                             )
                
                if post_img is not None:
                    image_data = PostMaster.objects.get(id=id)
                    image_data.post_img = post_img
                    image_data.save()
                
                id = id
                msg = 'post updated successfully.'

        except Exception as e:
            msg = 'post saved failed.'
            print(e,'--- error in create post function ----')
        json_data = {
            'id':id,
            'msg':msg,
        }
        return JsonResponse(json_data)
    
    try:
        post_obj = PostMaster.objects.get(id=id)
    except:
        post_obj = ''
    
    category = CategoryMaster.objects.all()
    context = {
        'category':category,
        'post_obj':post_obj,
        'id':id,
    }
    return render(request,'create_post.html',context)

def list_page(request):
    list_post = PostMaster.objects.all().order_by('-created_at')[:30]
    context = {
        'list_post':list_post
    }
    return render(request,'post_list.html',context)

def delete_post(request,id):
    post_delete = PostMaster.objects.filter(id=id).delete()
    return redirect('/list_page/')

def create_ads(request):
    if request.method == 'POST':
        otherads = request.FILES.get('otherads')
        Other_Ads = OtherAds.objects.create(other_ads=otherads)
        json_data = {
            'msg':'Your Advertisement has been added.'
        }
        return JsonResponse(json_data)
    
def ads_list(request):
    ads_list = OtherAds.objects.all()
    context = {
        'ads_list':ads_list
    }
    return render(request, 'ads_list.html', context)

def delete_ads(request,id):
    OtherAds.objects.get(id=id).delete()
    return redirect('/ads_list/')
