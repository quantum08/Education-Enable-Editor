from django.views import generic
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import UserForm, SignInForm
from django.views.generic import View

def Index(request):

    return render(request, "editor/index.html")



class Signin(View):
    form_class = SignInForm
    template_name = 'editor/signin.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process data
    def post(self, request):
        form = self.form_class(request.POST)

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('editor:index')
        else:
            return render(request, self.template_name, {'form': form})

        return  render(request, self.template_name, {'form': form})


def Signup(request):
    template = loader.get_template('editor/login.html')
    return HttpResponse(template.render(request))

def Editor(request):
    return render(request, "editor/editor.html")

def Html_one(request):
    return render(request, "editor/html/one.html")

def Html_two(request):
    return render(request, "editor/html/two.html")

def Html_three(request):
    return render(request, "editor/html/three.html")

def Html_four(request):
    return render(request, "editor/html/four.html")

def Html_five(request):
    return render(request, "editor/html/five.html")

def Html_six(request):
    return render(request, "editor/html/six.html")

def Html_seven(request):
    return render(request, "editor/html/seven.html")

def ace(request):
    return render(request, "editor/ace.html")


def logout_view(request):
    logout(request)
    return render(request, "editor/index.html", {"message": "logged out"})


class UserFormView(View):
    form_class = UserForm
    template_name = 'editor/miniProject.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process data
    def post(self, request):
        form = self.form_class(request.POST)


        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #change user password
            user.set_password(password)
            user.save()

            #return user if credential are correct

            user = authenticate(username=username, password=password)
            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('editor:index')

        return  render(request, self.template_name, {'form': form})

