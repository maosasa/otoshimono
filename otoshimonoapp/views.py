from django.shortcuts import get_object_or_404, render
from django.utils import timezone
import json
import uuid
from datetime import datetime, date

from otoshimonoapp.forms import OtoshimonoRegisterForm

from .models import OtoshimonoInfo

# json.dumpでJSON型に変換できない型の例外処理


def convertDataToJson(object):
    if isinstance(object, (datetime, date)):
        return object.isoformat()
    elif (isinstance(object, uuid.UUID)):
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


def form_location(request):
    context = {}
    return render(request, 'otoshimonoapp/form_location.html', context)


def add(request):
    form = OtoshimonoRegisterForm(request.POST, request.FILES)
    is_valid = form.is_valid()
    if not is_valid:
        return render(request, 'otoshimonoapp/form.html', {'form': form})

    cleaned_data = form.cleaned_data
    new_otoshimono = OtoshimonoInfo(
        obj_name=cleaned_data["obj_name"],
        place_found=cleaned_data["place_found"],
        place_now=cleaned_data["place_now"],
        pub_date=timezone.now(),
        location=cleaned_data["location"],
    )
    if cleaned_data["image"] != None:
        new_otoshimono.image = cleaned_data["image"]
    new_otoshimono.save()
    context = {'success_message': "「" +
               cleaned_data["obj_name"]+"」 が追加されました。ご報告ありがとうございます。"}
    return render(request, 'otoshimonoapp/form.html', context)
