from django.urls import path,include
from first_app import views

urlpatterns = [
	path('a/',views.show_a,name='new'),
	path('',views.diff,name='new'),
	path('render_page/',views.page,name='page'),
]