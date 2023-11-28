from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .tables import ProjectNamesTable
from .models import b2p_project_name
from .forms import project_lists_form

@login_required
def home(request) :
    request.session['current_page'] = 'Home'
    return render(request,'main/home.htm')

@login_required
def project_lists(request) :
    request.session['current_page'] = 'Project Lists'
    table = ProjectNamesTable(b2p_project_name.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=25)
    return render(request,'main/project_lists.htm', {"table": table})

@login_required
def project_lists_add(request) :
    request.session['current_page'] = 'Project Lists'
    msg = None
    if request.method == 'POST':
        form=project_lists_form(request.POST)
        if form.is_valid():
            #form.save()
            msg = "Successfully add new record!"
        else: 
            msg = "Error in saving record!"
    else:
        form=project_lists_form()

    return render(request,'main/project_lists_add.htm', {"form": form, "msg" : msg})
