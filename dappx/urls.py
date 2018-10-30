
from django.conf.urls import url
from . import views
# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^candidate_register/$',views.candidate_register,name='candidate_register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]