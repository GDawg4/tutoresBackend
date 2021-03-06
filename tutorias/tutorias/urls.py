"""tutorias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)

from universities.views import UniversityViewSet
from faculties.views import FacultyViewSet
from careers.views import CareerViewSet
from users.views import UserViewSet

from events.views import EventViewSet
from classrooms.views import ClassroomViewSet
from courses.views import CourseViewSet
from hosts.views import HostViewSet
from tutors.views import TutorViewSet
from event_types.views import EventTypeViewSet
from event_assigns.views import EventAssignViewSet
from classes.views import ClassesViewSet
from tutorias_sessions.views import SessionViewSet
from day_hour.views import DayHourViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'universities', UniversityViewSet)
router.register(r'faculties', FacultyViewSet)
router.register(r'careers', CareerViewSet)
router.register(r'events', EventViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'hosts', HostViewSet)
router.register(r'event_types', EventTypeViewSet)
router.register(r'tutors', TutorViewSet)
router.register(r'event_assigns', EventAssignViewSet)
router.register(r'classes', ClassesViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'day_hour', DayHourViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/token-auth/', obtain_jwt_token),
    url(r'^api/v1/token-refresh/', refresh_jwt_token),
]
