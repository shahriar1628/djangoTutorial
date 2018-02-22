from django.shortcuts import render

# Create your views here.
def hello(request):
    param = dict()
    param['today'] = '2/20/2018'
    return render(request, "hello.html", param)
