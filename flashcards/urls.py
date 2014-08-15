#flashcards\urls.py
from django.conf.urls import patterns, url
from flashcards import views

urlpatterns = patterns('',

                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<flashcard_id>\w+)/$', views.detail, name='detail'),
					   url(r'^(?P<flashcard_id>\w+)/update/$', views.update, name='update'),
                        # ex: /polls/5/results/                       
                       
)
