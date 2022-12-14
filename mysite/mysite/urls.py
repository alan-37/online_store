
from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from orders import views as orders_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('', include('mainapp.urls')),
    path('regedit/', user_views.regedit, name='regedit'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('exit/', auth_views.LogoutView.as_view(template_name='mainapp/index.html'), name='exit'),
    path('profile/', user_views.profile, name='profile'),
    path('basket_adding/', orders_views.basket_adding, name='adding'),
    path('checkout/', orders_views.checkout, name='checkout',),
    path('checkout/<str:id>/', orders_views.delete_cart, name='delete',),
    path('order_info/', orders_views.order_info, name='order_info',),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)