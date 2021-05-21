from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]