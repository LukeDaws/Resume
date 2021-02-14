from django.http import (FileResponse, 
    Http404, 
    HttpResponse,
    )
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    
    return render(request, "home.html", {})

def pdf_view(request, *args, **kwargs):
    try:
        return FileResponse(open('media/pdfs/Luke_Daws_Resume.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def resume_view(request, *args, **kwargs):
    return render(request, "resume.html", {})

def project_view(request, *args, **kwargs):
    return render(request, "S3322003_Assignment.html", {})

def contact_view(request, *args, **kwargs):
    
    return render(request, "contact.html", {})

