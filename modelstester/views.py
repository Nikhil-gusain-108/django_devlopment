from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import card_details,teacher
from .forms import school_form
# Create your views here.
def modelstest(request):
    card_d = card_details.objects.all()
    return render(request,'modelstest.html',{"card_d":card_d})
def input_taker(request):
    teachers = teacher.objects.all()
    detail = None
    form = None
    if request.method == 'POST':
        form = school_form(request.POST)
        if form.is_valid():
            teach_obj = teacher()
            teach_obj.name=form.cleaned_data['name']
            teach_obj.save()
        return HttpResponseRedirect('/modelstester/input/')
    else:
        form = school_form()
    
    return render(request,'form_test.html',{'detail':detail,'form':form,'teacher':teachers})