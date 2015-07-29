from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext


def base(request):
    return render_to_response("base.html", context_instance=RequestContext(request))


def user_registration(request):
    if request.POST:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        form = UserCreationForm({
            'username': username,
            'password1': password1,
            'password2': password2,
        })
        try:
            form.save(commit=True)
            return HttpResponseRedirect("/")
        except ValueError:
            return render_to_response("registration/create_user.html",
                                      {'form': form},
                                      context_instance=RequestContext(request)
                                      )
    return render_to_response("registration/create_user.html",
                              {'form': UserCreationForm()},
                              context_instance=RequestContext(request)
                              )
