from django.shortcuts import render
from django.views.generic import ListView
from myapp.models import student
from django.shortcuts import get_object_or_404
from myapp.models import Section
# Create your views here.
def hello(request):
    param = dict()
    param['today'] = '2/20/2018'
    return render(request, "hello.html", param)

class printStudent(ListView):
    model = student

class sectionStudent(ListView):

    def get_queryset(self):
        self.section = get_object_or_404(Section,sectionName=self.kwargs['section'])
        return student.objects.filter(section = self.section)

