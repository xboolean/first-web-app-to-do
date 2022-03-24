from django.db import models
from django.utils.html import escape, mark_safe
from django.conf import settings
from datetime import date
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=17)
    badge_name = models.CharField(max_length=40)

    def __str__(self):
        return self.title
    
    def get_html_badge(self):
        title = escape(self.title)
        badge_name = escape(self.badge_name)
        html = '<span class="badge rounded-pill %s">%s</span>' % (badge_name, title)
        return mark_safe(html)

    class Meta:
        verbose_name_plural = 'Categories'

class Task(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    session = models.CharField(max_length=32, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail_view", kwargs={"pk": self.pk})
    

    @property
    def time_left(self):
        time = self.deadline - date.today()
        if time.days >1:
            return "%s days" % (time.days)
        elif time.days==1:
            return "%s day" % (time.days)
        elif time.days==0:
            return 'Expiring task'
        elif time.days<0:
            return 'Expired task'
    
    @property
    def red_row(self):
        time = self.deadline - date.today()
        if time.days<0:
            return 'class=table-danger'
        else:
            pass

    class Meta:
        ordering = ['-date_created']
    

