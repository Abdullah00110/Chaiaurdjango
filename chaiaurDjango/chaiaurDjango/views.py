from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello.world , chai aur code mein aapka swagat hai...")
    return render(request , 'website/index.html')

def about(request):
    return HttpResponse("Hello.world , chai aur django mein aapka swagat hai...")


def contact(request):
    return HttpResponse("Hello.world , chai aur python mein aapka swagat hai...")