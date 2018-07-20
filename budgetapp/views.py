from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Project,Category
from django.views.generic import CreateView
from django.forms import ModelForm

def project_list(request):
    return render(request,'budget/list.html')

def project_detail(request,project_slug):
    # print(Project.objects.all())
    project = get_object_or_404(Project,slug = project_slug)
    category_list = Category.objects.filter(project = project)
    return render(request,'budget/detail.html',{'project':project,'expense_list':project.expenses.all()})



class AddForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['budget'].widget.attrs.update({'class' : 'form-control'})
    
    class Meta:
        model = Project
        fields = ['name', 'budget']

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'budget/add_project.html'
    form_class = AddForm
    def form_valid(self,form):
        self.object = form.save(commit = False)
        self.object.save()

        categories = self.request.POST['categoryString'].split(',')
        for category in categories:
            Category.objects.create(
                project = Project.objects.get(id=self.object.id),
                name = category
            ).save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return slugify(self.request.POST['name'])
