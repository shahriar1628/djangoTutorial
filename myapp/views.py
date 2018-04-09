from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from embed_video.backends import detect_backend
from myapp.models import Person
from myapp.models import Section
from myapp.models import student
from .forms import NameForm


# Create your views here.
def hello(request):
    param = dict()
    language = 'bdt'
    if ('lang' in request.COOKIES):
        language = request.COOKIES['lang']
    return render_to_response('hello.html', {'language': language, 'today': '3-25-2017'})


def language(request, language='en-gb'):
    responce = HttpResponse('settings language to %s' % language)
    responce.set_cookie('lang', language)
    if ('firstName' in request.session):
        del request.session['firstName']
    return responce


class printStudent(ListView):
    model = student


class sectionStudent(ListView):
    def get_queryset(self):
        self.section = get_object_or_404(Section, sectionName=self.kwargs['section'])
        return student.objects.filter(section=self.section)


def get_name(reqest):
    if ('firstName' in reqest.session):
        return HttpResponseRedirect('/thanks')
    if (reqest.method == 'POST'):
        form = NameForm(reqest.POST, reqest.FILES)
        if (form.is_valid()):
            print(form.cleaned_data)
            reqest.session['firstName'] = form.cleaned_data['firstName']
            person = Person.create(form.cleaned_data['firstName'], form.cleaned_data['lastName'],
                                   form.cleaned_data['picture'], form.cleaned_data['profileVideo'])
            person.save()
            print(form.cleaned_data)
            return HttpResponseRedirect('/thanks')
    else:
        form = NameForm()
    return render(reqest, 'name.html', {'form': form})



class HomeView(TemplateView):
    template_name = 'video.html'
def embedVideo(request):
    param = dict()
    param['my_video'] = detect_backend('https://player.vimeo.com/video/263910146')
    print(detect_backend('https://player.vimeo.com/video/263910146').url)
    print(detect_backend('https://player.vimeo.com/video/263910146').thumbnail)
    print(detect_backend('https://player.vimeo.com/video/263910146').backend)
    print(param)
    #param['url'] = 'http://player.vimeo.com/video/263910146'
    #param['thumbnail'] = 'http://i.vimeocdn.com/video/693556885_640.jpg'
    #param['backend'] = 'VimeoBackend'
    return  render_to_response('embed_video.html',param)
