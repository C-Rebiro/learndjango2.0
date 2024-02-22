from django.shortcuts import render

def home(request):
    return render(request, 'Index.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'Contact.html')

def gallery(request):
    return render(request, 'Gallery.html')
