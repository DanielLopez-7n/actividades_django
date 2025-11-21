from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def member_list(request):
    members = Member.objects.all().order_by('-joined_date')
    context = {
        'members': members,
        'year': timezone.now().year,
    }
    return render(request, 'all_members.html', context)

  
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  miembros = Member.objects.all().values()
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'miembros' : miembros,   
  }
  return HttpResponse(template.render(context, request))