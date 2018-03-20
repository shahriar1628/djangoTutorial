from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from myapp.models import student
from django.shortcuts import get_object_or_404
from myapp.models import Section
from myapp.models import Book
from myapp.models import Person
from .forms import NameForm
# Create your views here.
def hello(request):
    param = dict()
    book = Book.create("Pride and Prejudice")
    book.save()
    param['today'] = '2/20/2018'
    return render(request, "hello.html", param)

class printStudent(ListView):
    model = student

class sectionStudent(ListView):

    def get_queryset(self):
        self.section = get_object_or_404(Section,sectionName=self.kwargs['section'])
        return student.objects.filter(section = self.section)
def get_name (reqest):
    print("enter")
    if(reqest.method == 'POST'):
        form = NameForm(reqest.POST)
        if(form.is_valid()):
            person = Person.create(form.cleaned_data['firstName'], form.cleaned_data['lastName'])

            person.save()
            print("hello world!!!!!")
            print(form.cleaned_data)
            return HttpResponseRedirect('/thanks')
    else:
        form = NameForm()

    return render(reqest,'name.html',{'form':form})
