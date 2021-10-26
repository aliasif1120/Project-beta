
import os
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',include("app1.urls")),
    path('about/me/',include("app1.urls")),
    path('email/',include("app1.urls")),
    path('contact/us/',include("app1.urls")),
    path('project1/',include("app1.urls")),
    path('project2/',include("app1.urls")),
    path('project3/',include("app1.urls"))

]
urlpatterns+=staticfiles_urlpatterns()