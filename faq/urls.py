from __future__ import absolute_import

from django.contrib.auth.decorators import login_required
from django.conf.urls.defaults import *
from django.conf import settings
from . import views as faq_views

urlpatterns = patterns('',
    url(regex = r'^$',
        view  = faq_views.TopicList.as_view(),
        name  = 'faq_topic_list',
    ),
    url(regex = r'^submit/thanks/$',
        view  = faq_views.SubmitFAQThanks.as_view(),
        name  = 'faq_submit_thanks',
    ),
)

if settings.FAQ_ALLOW_QUESTION:
    if settings.FAQ_REQUIRE_AUTH:
        urlpatterns += patterns('',
            url(regex = r'^submit/$',
                view  = login_required(faq_views.SubmitFAQ.as_view()),
                name  = 'faq_submit',
            ),
        )
    else:
        urlpatterns += patterns('',
            url(regex = r'^submit/$',
                view  = faq_views.SubmitFAQ.as_view(),
                name  = 'faq_submit',
            ),
        )
    
urlpatterns += patterns('',
    url(regex = r'^(?P<slug>[\w-]+)/$',
        view  = faq_views.TopicDetail.as_view(),
        name  = 'faq_topic_detail',
    ),
    url(regex = r'^(?P<topic_slug>[\w-]+)/(?P<slug>[\w-]+)/$',
        view  = faq_views.QuestionDetail.as_view(),
        name  = 'faq_question_detail',
    ),
)
