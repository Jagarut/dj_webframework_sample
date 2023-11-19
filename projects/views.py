from django.shortcuts import render
from .models import Project, Review

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
        # 'tags': tags,
    }
    return render(request, 'projects/single-project.html', context=context)
