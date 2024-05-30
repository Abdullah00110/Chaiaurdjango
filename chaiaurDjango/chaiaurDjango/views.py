from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello.world , chai aur code mein aapka swagat hai...")
    return render(request , 'website/index.html')

def about(request):
    return HttpResponse("Ye page bhi ban jaayega sabr rakho itni jaldi kya hai")


def contact(request):
    return render(request, 'website/Contact.html')