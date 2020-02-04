from django.urls import path
from .import views
urlpatterns = [
    path('path/',views.CreateMyModelView.as_view()),
    #path('sucess/',views.BookList.as_view(),name="sucess")
    path('book/',views.BookList.as_view(),name ='book_list'),
    path('abcd',views.abc),
    path('SuggestProject/', views.ajax_load_project, name='ajax_load_project'),
    path('searchtest/', views.searchProject, name='searchProject'),
]
