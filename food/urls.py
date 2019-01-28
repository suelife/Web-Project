from django.urls import path
from . import views
app_name = 'food'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('list/', views.list, name = 'list'),
    path('list/create/', views.listcreate, name = 'listcreate'),
    path('list/delete/<int:id>', views.listdelete , name ='listdelete'),
    path('list/update/<int:id>', views.listupdate , name = 'listupdate'),
    # path('list/chart/', views.listchart , name = 'listchart'), 
    path('list/search/', views.listsearch , name = 'listsearch'),
    path('record/', views.record, name = 'record'),
    path('record_ajax/', views.record_ajax , name = 'record_ajax'),
    path('record/create/', views.recordcreate , name ='recordcreate'),
    path('record/delete/<int:id>', views.recorddelete , name ='recorddelete'),
    path('record/update/<int:id>', views.recordupdate , name = 'recordupdate'),
    path('record/chart/', views.recordchart , name = 'recordchart'),
    path('datatosql', views.datatosql),
]
