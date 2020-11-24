# polling/urls.py

from django.urls import path
from polling.views import list_view, detail_view  # , index, detail, results, vote

# path('', index, name='index'),
urlpatterns = [
    path("", list_view, name="poll_index"),
    path("polls/<int:poll_id>/", detail_view, name="poll_detail"),
]

# path('question/<int:question_id>/', detail, name='detail'),
# path('question/<int:question_id>/results/', results, name='results'),
# path('question/<int:question_id>/vote/', vote, name='vote'),
