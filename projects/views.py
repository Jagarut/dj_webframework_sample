from django.shortcuts import render
from .models import Project, Review
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    
    context = {
        'projects': projects
    }

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    # tags = projectObj.tags.all()

    context = {
        'project':projectObj,
    }
    return render(request, 'projects/single-project.html', context=context)

def createProject(request):
    context = {'form': ProjectForm()}
    return render(request, "projects/project_form.html", context)