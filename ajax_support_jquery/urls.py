from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [

    path('load_test',views.load_test),
    path('load_test_server/',views.load_test_server),
    path('jquery_get/',views.jquery_get),
    path('jquery_get_server/',views.jquery_get_server),
    path('jquery_post/',views.jquery_post),
    path('jquery_post_server/',views.jquery_post_server),
    path('jquery_ajax/',views.jquery_ajax),
    path('jquery_ajax_server/',views.jquery_ajax_server),
    path('cross/',views.cross),
    path('cross_server/',views.cross_server)

]