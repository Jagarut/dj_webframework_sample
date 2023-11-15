from django.shortcuts import render
# from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'Site to build out porfolio'
    },
    {
        'id': '3',
        'title': 'Pets Website',
        'description': 'Site to show my beautiful pets'
    },
]

def projects(request):
    msg = "projects page!"
    context = {
        'message': msg, 
        'number': 10,
        'projects': projectsList
    }

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for project in projectsList:
        if project['id'] == pk:
            projectObj = project
    return render(request, 'projects/single-project.html', {'project':projectObj})
