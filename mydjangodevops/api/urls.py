from django.urls import path, include

urlpatterns = [
        path('blog/', include(('mydjangodevops.blog.urls', 'blog'))),
]
