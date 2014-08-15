#averyswords\urls.py

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'flashcards.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#url(r'^$', include('flashcards.urls', namespace="flashcards")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^words/', include('flashcards.urls', namespace="flashcards"))
	
)
