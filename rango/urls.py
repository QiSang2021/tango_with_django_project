from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('page/<slug:page_name_slug>/', views.show_page, name='show_page'),
    path('category/<category_name_slug>/add_page/', views.add_page, name='add_page'),
    path("profile/", views.profile, name="profile"),
    path("article/", views.article, name="article"),
    path('article/<slug:article_title_slug>/', views.show_article, name='show_article'),
    path('page/<page_name_slug>/submit_comment/', views.submit_comment, name='submit_comment'),
    path("add_article/",views.add_article,name='add_article'),
    path("item/", views.item, name="item"),
]
