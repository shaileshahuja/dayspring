from django.conf.urls import url, patterns

from capture.views import UploadPage, HomePage

urlpatterns = patterns(
    '',
    url(r"^home", HomePage.as_view(), name="home"),
    url(r"^upload", UploadPage.as_view(), name="upload")
)
