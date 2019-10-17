import uuid
from datetime import datetime, timedelta, timezone
from django.db import models
import requests
from lxml import html
from .utils import delay_task

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    url = models.URLField(max_length=100, verbose_name='URL')
    minutes = models.PositiveIntegerField(default=0, verbose_name='Минуты', blank=True)
    seconds = models.PositiveIntegerField(default=0, verbose_name='Секунды', blank=True)
    start_time = models.DateTimeField(verbose_name='Время начала')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    code = models.CharField(max_length=100, verbose_name='Кодировка')
    header = models.CharField(max_length=100, blank=True, verbose_name='H1')
    report = models.CharField(max_length=100, default='', verbose_name='Отчет о выполнении')
    is_done = models.BooleanField(default=False, verbose_name='Выполнено')

    def save(self):
        self.start_time = datetime.now(timezone.utc) \
                          + timedelta(minutes=self.minutes, seconds=self.seconds)
        self.is_done = False
        self.report = ''
        self.title = ''
        self.code = ''
        self.header = ''

        super(Task, self).save()

        delay = self.minutes*60 + self.seconds
        delay_task(self, delay)

    def parse(self):

        result = {}
        try:
            response = requests.get(self.url)
        except requests.exceptions.RequestException as error:
            result['report'] = error

        if not result:
            if response.status_code == 200:
                tree = html.fromstring(response.text)

                titles = tree.xpath('//title/text()')
                encodes = tree.xpath('//meta[@charset]/@charset')
                headers = tree.xpath('//h1/text()')

                result['title'] = titles[0].strip() if titles else ''
                result['code'] = encodes[0].strip() if encodes else response.encoding
                result['header'] = ' /// '.join(map(lambda x: x.strip(), headers))

                result['report'] = 'ОК({})'.format(response.status_code)
            else:
                result['report'] = 'FAIL({})'.format(response.status_code)
        result['is_done'] = True
        result['start_time'] = datetime.now(timezone.utc)
        Task.objects.filter(url=self.url).update(**result)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
