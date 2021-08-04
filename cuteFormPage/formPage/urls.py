from django.urls import path,include
from formPage import views

app_name = 'formPage'
urlpatterns = [
    path('signup/' , views.signupPage , name = 'signuppage'),
    path('register/' , views.registerPage , name = 'register'),
    path('basepage/' , views.basePage , name='basepage'),
    path('login/' , views.user_login , name='user_login'),
]
