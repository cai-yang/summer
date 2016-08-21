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




@shared_task
def check(daily_index):
    try:
        d=Daily.objects.get(pk=int(daily_index))
    except:
        return "NO DAILY"
    article_list = Article.objects.filter(daily = d)
    try:
        p=article_list[4].title
    except:
        return "NOT FULL"
    flag = daily_index
    for article in article_list:
        if article.status=="0":
            return "NOT READY"
            break
    chain = publish_daily.s(daily_index)|check.s()
    chain()
    return "SENDING"

@shared_task
def publish_daily(daily_index):
    if email_daily(daily_index):
        d = Daily.objects.get(pk=daily_index)
        d.status="2"
        d.save()
        return daily_index+1
    return daily_index


@shared_task
def email_daily(daily_index):
    return "Daily No.%s has been e-mailed." % daily_index

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
