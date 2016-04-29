from django.conf.urls import url, patterns

from capture.views import UploadPage, HomePage, SuccessPage

urlpatterns = patterns(
    '',
    url(r"^home", HomePage.as_view(), name="home"),
    url(r"^upload", UploadPage.as_view(), name="upload"),
    url(r"^success", SuccessPage.as_view(), name="success")
)
