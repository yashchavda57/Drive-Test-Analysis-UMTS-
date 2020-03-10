from django.urls import path
from django.contrib import admin
from . import views

app_name = "userinterface"

urlpatterns = [
    path('', views.home, name = 'home'),
    path('tableview', views.tableview, name = 'table-view'),
    path('uploadform', views.model_form_upload, name='model_form_upload'),
    path('data/TEST.xlsx', views.testview1, name = 'test-view1'),
    path('data/DataSet.xlsx', views.testview2, name = 'test-view2'),

    path('mapview', views.mapview, name = 'map-view'),
    path('graphview', views.graphview, name = 'graph-view'),
    path('solutionview', views.solutionview, name = 'solution-view'),
    path('pdfview', views.pdfview, name = 'generate-pdf-view'),
]
