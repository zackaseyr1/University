from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='home'), 
	path('suggest/', views.suggest, name='suggest'),
    path('generate', views.Generate_Image, name='Generate_Image'),
	path('login/', views.login_user, name='login'),
	path('logout/', views.logout_user, name='logout'),
	path('register/', views.register_user, name='register'),
	path('past', views.past, name='past'),
	path('delete_past/<Past_id>', views.delete_past, name='delete_past'),
    path('past2/', views.past2, name='past2'),
    path('past2/delete/<int:image_id>/', views.delete_past2, name='delete_past2'),
]
