
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('oa/general', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/products/', include('menucode.urls.product_urls')),
    path('api/category/', include('menucode.urls.category_urls')),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)