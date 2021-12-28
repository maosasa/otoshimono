from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import OtoshimonoInfo

def index(request):
    latest_otoshimono_list = OtoshimonoInfo.objects.order_by('-pub_date')[:100]
    context = {'latest_otoshimono_list': latest_otoshimono_list}
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
    except (KeyError, OtoshimonoInfo.DoesNotExist):
        return render(request, 'otoshimonoapp/form.html', {
            'error_message': "You didn't fill the title.",
        })
    else:
        new_otoshimono = OtoshimonoInfo(
            obj_name=title,
            place_found=place_found,
            place_now=place_now,
            pub_date=timezone.new()
        )
        new_otoshimono.save()
        context = {}
    return render(request, 'otoshimonoapp/form.html', context)

