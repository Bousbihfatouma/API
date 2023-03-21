from django.contrib import admin
from django.urls import path, include
from blog import views

# importe la vue
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('api/', include('posts.urls')),
]
# définie la fonction à appeler