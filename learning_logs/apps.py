from django.apps import AppConfig


class LearningLogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'learning_logs'
    label = 'learning_logs' # 19.2.2 打不开localhost问的deepseek
