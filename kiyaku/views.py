from django.shortcuts import render

# Create your views here.
def item(request):
    return render(request,"kiyaku/item.html")
