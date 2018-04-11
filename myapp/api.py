from tastypie.resources import ModelResource
from myapp.models import student
class StudentResource(ModelResource):
    class Meta:
        queryset = student.objects.all()
        resource_name= 'pupils'
