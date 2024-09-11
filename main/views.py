from django.shortcuts import render

def show_main(request):
    context = {
        'appname' : 'naiki-apparel',
        'npm' : '2306217185',
        'name': 'Muhammad Reyhan Ardian',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
# Create your views here.
