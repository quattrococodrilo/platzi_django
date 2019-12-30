from django.urls import path
from users import views

urlpatterns = [

    # Posts
    path('<str:username>/',
         views.DetailView.as_view(),
         name='detail'),

    # Management
    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'),
    path(
        route='signup/',
        view=views.singup_view,
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.update_profile,
        name='update_profile'
    ),

]
