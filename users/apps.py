from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    # import it to make sure the creating and saving profile will work
    def ready(self):
        import users.signals
