from django.urls import path
from CSE import views
from .views import Forms, StudentList, StudentDetail, StudentUpdate, StudentDelete

urlpatterns = [
    path("home", views.home, name = 'home'),
path("prodcts", views.prodcts, name = 'prodcts'),
path("service", views.service, name = 'service'),
path("contacts", views.contacts, name = 'contacts'),
path("aboutus", views.aboutus, name = 'aboutus'),

path("students", views.students, name = 'students'),
path('forms', Forms.as_view(), name = 'forms'),
    path('list', StudentList.as_view(), name = 'list'),
    path('<pk>/detail', StudentDetail.as_view(), name = 'detail'),
    path('<pk>/update', StudentUpdate.as_view(), name = 'update'),
    path('<pk>/delete', StudentDelete.as_view(), name = 'delete'),
    





]