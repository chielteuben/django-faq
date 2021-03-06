from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from faq.models import Topic, Question 

from datetime import datetime

class FaqTopicSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        topics = Topic.objects.all()
        return topics 

    def lastmod(self, obj):
        return datetime.now() 

    def location(self, obj):
        return reverse('faq_topic_detail', args=[obj.slug])

class FaqQuestionSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        topics = Question.objects.filter(status=1)
        return topics 

    def lastmod(self, obj):
        return obj.updated_on

    def location(self, obj):
        return reverse('faq_question_detail', args=[obj.topic.slug, obj.slug])
