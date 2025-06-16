from django.shortcuts import render

def home_view(request):
    return render(request, 'solar/Index.html')

def about_view(request):
    return render(request, 'solar/about.html')

def contact_view(request):
    return render(request, 'solar/contact.html')

def services_view(request):
    return render(request, 'solar/service.html')

def team_view(request):
    return render(request, 'solar/team.html')

def blog_view(request):
    return render(request, 'solar/bloge.html')

def project_view(request):
    return render(request, 'solar/projects.html')

