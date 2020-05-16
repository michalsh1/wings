
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('michis_questionnaire', include('questionnaire.urls')),
    path(r'', include('quiz.urls')),

]

