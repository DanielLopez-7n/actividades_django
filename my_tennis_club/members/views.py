from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Member
from django.db.models import Q

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
  column_fistname = miembros.values_list('first_name')
  records_daniel = Member.objects.filter(first_name='Daniel')
  record_AND_daniel = Member.objects.filter(first_name='Daniel', id=11).values()
  record_OR_daniel = Member.objects.filter(Q(first_name='Violeta') | Q(first_name='Orlando')).values()
  record_like_start_M = Member.objects.filter(first_name__startswith='M').values()
  record_like_ends_S = Member.objects.filter(first_name__endswith='s').values()
  record_like_contains_ez = Member.objects.filter(first_name__contains='ez').values()
  record_like_icontains_z = Member.objects.filter(first_name__icontains='z').values()
  record_range_id = Member.objects.filter(id__range=(2, 5)).values()
  order_by_asc = Member.objects.all().order_by('first_name').values()
  order_by_desc = Member.objects.all().order_by('first_name').values()
  
  
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    'miembros' : miembros,
    'column_fistname': column_fistname,
    'records_daniel': records_daniel,
    'record_AND_daniel': record_AND_daniel,
    'record_OR_daniel': record_OR_daniel,
    'record_like_start_M': record_like_start_M,
    'record_like_ends_S': record_like_ends_S,
    'record_like_contains_ez': record_like_contains_ez,
    'record_like_icontains_z': record_like_icontains_z,
    'record_range_id': record_range_id,
    'order_by_asc': order_by_asc,
    'order_by_desc': order_by_desc,
  }   
  
  return HttpResponse(template.render(context, request))
  