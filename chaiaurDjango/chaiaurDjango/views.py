from django.http import HttpResponse
from django.shortcuts import redirect, render
from chai.models import Contact

def home(request):
    # return HttpResponse("Hello.world , chai aur code mein aapka swagat hai...")
    return render(request , 'website/index.html')

def about(request):
    return render(request, 'website/about.html')


def contact(request):
    if request.method == 'POST':
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
    
        contact = Contact(firstname = first_name , lastname = last_name , email = email, subject = subject , message = message)

        contact.save()

        return redirect('contact')
    return render(request, 'website/contact.html')
