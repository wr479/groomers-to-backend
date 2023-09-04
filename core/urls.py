
from django.urls import re_path, path


from . import views

sitemaps = {
    'textpage': views.TextPageSitemap,
    'staticviews': views.StaticViewsSitemap,
}

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('reviews/', views.ReviewsView.as_view(), name="revievs"),
    path('price/', views.PriceView.as_view(), name="price"),
    # Переделать
    path('ajax/', views.AjaxView.as_view(), name="ajax"),
    # path('contact-form/', contact_form, name='contact_form'),
    # path('contacts/', TemplateView.as_view(**{"template_name": "contacts.html"}), name="contacts"),
    path('page/<slug:page_slug>/', views.GenericTextPageView.as_view(), name="text_page"),
    path('sitemap.xml', views.sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', views.robots_txt_view),
    # path('submit_form/', views.submit_form, name='submit_form'),
]
