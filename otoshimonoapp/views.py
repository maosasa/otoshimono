from django.shortcuts import get_object_or_404, render
from django.utils import timezone
import json
import uuid
from datetime import datetime, date

from .models import OtoshimonoInfo

# json.dumpでJSON型に変換できない型の例外処理
def convertDataToJson(object):
    if isinstance(object, (datetime, date)):
        return object.isoformat()
    elif(isinstance(object, uuid.UUID)):
        return str(object)

def index(request):
    latest_otoshimono_list = OtoshimonoInfo.objects.order_by('-pub_date')[:100]
    context = {
        'latest_otoshimono_list': json.dumps(list(latest_otoshimono_list.values()), ensure_ascii=False, default=convertDataToJson),
        'image_url_list': json.dumps([item.image.url for item in latest_otoshimono_list], ensure_ascii=False, default=convertDataToJson)
        }
    return render(request, 'otoshimonoapp/index.html', context)

def detail(request, otoshimono_id):
    otoshimono = get_object_or_404(OtoshimonoInfo, pk=otoshimono_id)
    return render(request, 'otoshimonoapp/detail.html', {'otoshimono': otoshimono})

def about(request):
    context = {}
    return render(request, 'otoshimonoapp/about.html', context)

def listing(request):
    latest_otoshimono_list = OtoshimonoInfo.objects.order_by('-pub_date')[:100]
    context = {'latest_otoshimono_list': latest_otoshimono_list}
    return render(request, 'otoshimonoapp/list.html', context)

def form(request):
    context = {}
    return render(request, 'otoshimonoapp/form.html', context)

def add(request):
    try:
        title = request.POST['title']
        place_found = request.POST['place_found']
        place_now = request.POST['place_now']
        location = request.POST['location']
    except (KeyError, OtoshimonoInfo.DoesNotExist):
        return render(request, 'otoshimonoapp/form.html', {
            'error_message': "You didn't fill the title.",
        })
    else:
        new_otoshimono = OtoshimonoInfo(
            obj_name=title,
            place_found=place_found,
            place_now=place_now,
            pub_date=timezone.now(),
            location=location,
        )
        if 'image' in request.FILES:
            limit_image_size = 10* 1024 * 1024
            if request.FILES['image'].size > limit_image_size:
                return render(request, 'otoshimonoapp/form.html', {
                    'error_message': "Image size must be less than 10MB.",
                })
            else:
                new_otoshimono.image = request.FILES['image']
        new_otoshimono.save()
        context = {'success_message': "「"+title+"」 が追加されました。ご報告ありがとうございます。"}
    return render(request, 'otoshimonoapp/form.html', context)
