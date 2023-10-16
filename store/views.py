from django.shortcuts import render

def index(request):
    """
    View index
    """
    return render(request, 'store/index.html')
