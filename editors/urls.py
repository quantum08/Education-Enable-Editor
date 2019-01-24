
from django.conf.urls import url
from . import views

app_name = 'editor'
urlpatterns = [
    #front page
    url(r'^$', views.Index, name='index'),

    #sign in
    url(r'^signin/$', views.Signin.as_view(), name='Signin'),


    #sign up
    url(r'^signup$', views.Signup, name='Signup'),


    #Register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #editor
    url(r'^editor/$', views.Editor, name='editor'),

#editor
    url(r'^html_one/$', views.Html_one, name='html_one'),

    url(r'^html_two/$', views.Html_two, name='html_two'),

    url(r'^html_three/$', views.Html_three, name='html_three'),
    url(r'^html_four/$', views.Html_four, name='html_four'),
    url(r'^html_five/$', views.Html_five, name='html_five'),
    url(r'^html_six/$', views.Html_six, name='html_six'),
    url(r'^html_seven/$', views.Html_seven, name='html_seven'),


#ace

url(r'^ace/$', views.ace, name='ace'),
]
