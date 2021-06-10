from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:id>/', views.get_page, name='get_page'),
    path('form_page/', views.form_page, name='form_page'),
    path('<int:pk>/update/', views.PageUpdateView.as_view(), name='page-update'),
    path('<int:pk>/delete/', views.PageDeleteView.as_view(), name='page-delete')
]