from django.shortcuts import render, get_object_or_404
from flask import request
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request,'jobs/home.html',{'jobs': jobs})

def detail(request,job_id):
    job_detail =  get_object_or_404(Job,pk=job_id)
    return render(request,'jobs/deatil.html',{'job':job_detail})
