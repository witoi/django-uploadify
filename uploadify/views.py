from django.http import HttpResponse
import django.dispatch
from django.views.decorators.csrf import csrf_exempt


upload_received = django.dispatch.Signal(providing_args=['data', 'extra'])
@csrf_exempt
def upload(request, *args, **kwargs):
    if request.method == 'POST':
        if request.FILES:
            upload_received.send(sender='uploadify', data=request.FILES['Filedata'], extra=request.POST)
    return HttpResponse('True')


