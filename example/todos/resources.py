from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from todos.models import ToDo


class ToDoResource(ModelResource):

    class Meta:
        resource_name = "todos"
        queryset = ToDo.objects.all()
        authorization = Authorization()