from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request,'index.html')
def about(request):
  return render(request,'about.html')
def contact(request):
  return render(request,'contact.html')
def services(request):
  return render(request,'services.html')

def residential(request):
  return render(request,'residential.html')

def DTCP_approved (request):
  return render(request,'DTCP_approved .html')

def commercial(request):
  return render(request,'commercial.html')

def industrial(request):
  return render(request,'industrial.html')
def apartment(request):
  return render(request,'apartment.html')
def renovation(request):
  return render(request,'renovation.html')