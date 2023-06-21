from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    # При обращении помогает выводить только title.
    # Без него <QuerySet [<Articles: Articles object (1)>, <Articles: Articles object (2)>, <Articles: Articles object (3)>]>
    # С ним title новостей. Именно тайтл, который в бд забиваешь. В моем случае
    # <QuerySet [<Articles: Проверка работы>, <Articles: 9 отличных сервисов для проверки кода>, <Articles: Топ 10 игр для пандемии>]>
    # Можно забить anons, а можно косячок, но суть одна наркотики - говно.
    #  <QuerySet [<Articles: Очень крутая новость>, <Articles: хип-хоп>, <Articles: Мда уж>]>

    def __str__(self):
        return self.anons

    def get_absolute_url(self):
        return f'/news/{self.id}' #Начальный слеш не потеряй, а то башенку снесут

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        