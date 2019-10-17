import sys
from datetime import datetime, timezone
from django.apps import AppConfig

class ParserurlConfig(AppConfig):
    name = 'parserURL'
    verbose_name = 'Парсер URL'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True

        from .models import Task
        from .utils import delay_task

        for task in Task.objects.filter(is_done=False):
            start_time = task.start_time - datetime.now(timezone.utc)
            delay = start_time.total_seconds()
            delay_task(task, delay)
