from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.registration, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('new-project/', views.postproject, name='newproject'),
    path('project/<id>', views.get_project, name='project'),
    path('search', views.search_projects, name='search'),
    path('api/projects', views.ProjectList.as_view()),
    path('api/profiles', views.ProfileList.as_view())

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)