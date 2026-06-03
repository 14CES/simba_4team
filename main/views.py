from django.shortcuts import render

# Create your views here.

def demo_firstpage(request):
    return render(request, 'main/demo_firstpage.html')