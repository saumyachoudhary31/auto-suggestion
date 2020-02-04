from django.shortcuts import render
from .models import MyModel
from .forms import MyModelForm
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse
from django.http import HttpResponse,JsonResponse
import json
# Create your views here.
class CreateMyModelView(CreateView):
    model = MyModel
    form_class = MyModelForm
    template_name = 'temps.html'
    def get_success_url(self):
        return reverse("book_list")
class BookList(ListView):
    model = MyModel
def abc(request):
    list=["nam@g.com","g@g.com"]
    for i in list:
        print(i)
    context=["nam@g.com","g@g.com"]
    print(context)
    for k in context:
        print(k)
    return render(request,"test.html",{"context":list})
def ajax_load_project(request):
    data=""
    if request.is_ajax():
        q = request.GET.get('term', '')
        print(q)
        list=["nam@g.com","g@g.com","naman@g.com","good@g.com","s@s.sam"]
        #projects = Project.objects.filter(title__istartswith=q)[:5]
        cor=[]
        results=[]
        for i in list:
            if q in i:
                results.append(i)
            else:
                pass 
        print(results)
        
        # for project in results:
        #     project_json = {}
        #     project_json['id'] = project
        #     #project_json['value'] = project.title
        #     #project_json['label'] = project.title
        #     cor.append(project_json)
        # data = cor
        # print(data)
        data={'list':results}
        return JsonResponse(data,safe=False)
    else:
        #data = 'fail'
         return HttpResponse("no cokie")
    #mimetype = 'application/json'
    #return JsonResponse(data,safe=False)
    #return HttpResponse(data,content_type='application/json')

def searchProject(request):
    template_name = 'testsearch.html'
    return render(request, template_name)