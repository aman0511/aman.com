from django.shortcuts import render
from UrlDetails import *
from django.views.decorators.csrf import csrf_exempt
import time


def resume(request):
    return render(request, 'resume.html')


@csrf_exempt
def url_description(request):
    if request.method == 'POST':
        start = time.clock()
        url = request.POST['url']
        url_details = UrlDetails(url)
        data = url_details.get_details
        data['time'] = time.clock() - start
        return render(request, 'url.html', context=data)
    else:
        return render(request, 'url.html')
