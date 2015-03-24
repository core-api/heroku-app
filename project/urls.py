from django.conf.urls import url
from project.notes.views import note_list, note_detail


urlpatterns = [
    url(r'^', note_list),
    url(r'^(?P<pk>[^/]+)', note_detail)
]
