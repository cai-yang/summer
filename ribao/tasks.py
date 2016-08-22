from __future__ import absolute_import

from celery import shared_task, chain

from ribao.models import Article, Daily

@shared_task
def publish_article(article_index):
    a=Article.objects.get(pk=article_index)
    if a.status=="1":
        return "Error: Already published"
    a.status="1"
    a.save()
    return "Article %d %s has been published successfully" % (a.pk, a.title)




@shared_task(retries=3)
def check(daily_index):
    try:
        d=Daily.objects.get(pk=int(daily_index))
    except:
        Daily.objects.create()
        #check.apply_async((daily_index + 1,), countdown=3)
        return "%d NO DAILY" % daily_index
    article_list = Article.objects.filter(daily = d)
    try:
        p=article_list[4].title
    except:
        #check.apply_async((daily_index,), countdown=3)
        return "%d NOT FULL" % daily_index
    flag = daily_index
    for article in article_list:
        if article.status=="0":
            #check.apply_async((daily_index,), countdown=3)
            return "%d NOT READY" % daily_index
    chain = publish_daily.s(daily_index)|check.s()
    chain()
    return "SENDING"

@shared_task
def add_to_daily(article_index,daily_index):
    try:
        article = Article.objects.get(pk=article_index)
    except:
        return "ERROR: ARTICLE DOES NOT EXSIT"
    try:
        article.daily = Daily.objects.get(pk=daily_index)
    except:
        Daily.objects.create()
        daily_index = daily_index + 1
        add_to_daily.apply_async((article,daily_index),countdown=3)
    article.save()
    return 'article %d %s has been added to daily %d successfully.' % (article.pk, article.title, daily_index)

@shared_task
def publish_daily(daily_index):
    if email_daily.apply_async((daily_index,), countdown=3):
        d = Daily.objects.get(pk=daily_index)
        d.status="2"
        d.save()
        return daily_index+1
    return daily_index


@shared_task
def email_daily(daily_index):
    return True

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
