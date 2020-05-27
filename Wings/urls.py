
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_quiz/', include('questionnaire.urls')),
    path(r'old_quiz/', include('quiz.urls')),

]

