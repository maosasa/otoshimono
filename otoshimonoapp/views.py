from django.shortcuts import get_object_or_404, render

from .models import OtoshimonoInfo

def index(request):
    latest_otoshimono_list = OtoshimonoInfo.objects.order_by('-pub_date')[:100]
    context = {'latest_otoshimono_list': latest_otoshimono_list}
    return render(request, 'otoshimonoapp/index.html', context)

def detail(request, otoshimono_id):
    otoshimono = get_object_or_404(OtoshimonoInfo, pk=otoshimono_id)
    return render(request, 'otoshimonoapp/detail.html', {'otoshimono': otoshimono})