from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

#viewset
#configuring url to point to viewset; use a router; different urls for different methods unlike apiviewset
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') #basename to retrieve url
router.register('profile', views.UserProfileViewSet) #dont need a basename cause we have queryset in view
#apiview set
urlpatterns=[
	path('hello-view', views.HelloApiView.as_view()),
	path('login/', views.UserLoginApiView.as_view()),
	path('', include(router.urls))
]



