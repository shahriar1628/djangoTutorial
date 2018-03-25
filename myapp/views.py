from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from myapp.models import student
from django.shortcuts import get_object_or_404
from myapp.models import Section
from myapp.models import Book
from myapp.models import Person
from .forms import NameForm
import datetime
from django.template import RequestContext
# Create your views here.
def hello(request):
    param = dict()
    language = 'bdt'
    if('lang' in request.COOKIES):
        language = request.COOKIES['lang']
    return render_to_response('hello.html',{'language' :language,'today': '3-25-2017'})
        
def language(request, language = 'en-gb'):
    responce = HttpResponse('settings language to %s' %language)
    responce.set_cookie('lang',language)
    return  responce


class printStudent(ListView):
    model = student

class sectionStudent(ListView):

    def get_queryset(self):
        self.section = get_object_or_404(Section,sectionName=self.kwargs['section'])
        return student.objects.filter(section = self.section)
def get_name (reqest):
    print("enter")
    if(reqest.method == 'POST'):
        form = NameForm(reqest.POST,reqest.FILES)
        if(form.is_valid()):
            print(form.cleaned_data)
            person = Person.create(form.cleaned_data['firstName'], form.cleaned_data['lastName'],form.cleaned_data['picture'],form.cleaned_data['profileVideo'])
            person.save()
            print(form.cleaned_data)
            return HttpResponseRedirect('/thanks')
    else:
        form = NameForm()
    return render(reqest,'name.html',{'form':form})


