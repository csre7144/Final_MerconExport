from django.shortcuts import render
from django.contrib import messages
from me_project.models import ContactInfo

# Create your views here.
def home(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']

            ContactInfo.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            messages.success(request, 'Your message has been sent successfully.')
        except Exception as e:
            messages.error(request, f"Error: {e}")
    return render(request, 'index.html')

def carpet_pg(request):
    return render(request,'carpet.html')

def furniture_pg(request):
    return render(request, 'furniture.html')

def jute_pg(request):
    return render(request, 'jute.html')

def leather_pg(request):
    return render(request, 'leather.html')

def marble_pg(request):
    return render(request, 'marble.html')

def textile_pg(request):
    return render(request, 'textile.html')