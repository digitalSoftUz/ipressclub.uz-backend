from django.db import models


class Information(models.Model):
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    logo = models.ImageField(upload_to="Logo/")
    instagram_link = models.CharField(max_length=255)
    telegram_link = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    youtube_link = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    map = models.CharField(max_length=255)
    info = models.TextField()
    info_uz = models.TextField()
    info_ru = models.TextField()
    info_en = models.TextField()

    def __str__(self):
        return self.phone


class Partners(models.Model):
    logo = models.ImageField(upload_to="Partner logos")


class Team(models.Model):
    img = models.ImageField(upload_to="Team")
    fullname = models.CharField(max_length=255)
    fullname_uz = models.CharField(max_length=255)
    fullname_ru = models.CharField(max_length=255)
    fullname_en = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    position_uz = models.CharField(max_length=255)
    position_ru = models.CharField(max_length=255)
    position_en = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname


class Jamoa(models.Model):
    img = models.ImageField(upload_to="Team")
    fullname = models.CharField(max_length=255)
    fullname_uz = models.CharField(max_length=255)
    fullname_ru = models.CharField(max_length=255)
    fullname_en = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    position_uz = models.CharField(max_length=255)
    position_ru = models.CharField(max_length=255)
    position_en = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname


class Category(models.Model):
    name = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=555)
    name_uz = models.CharField(max_length=555)
    name_ru = models.CharField(max_length=555)
    name_en = models.CharField(max_length=555)
    mini_text = models.CharField(max_length=555)
    mini_text_uz = models.CharField(max_length=555)
    mini_text_ru = models.CharField(max_length=555)
    mini_text_en = models.CharField(max_length=555)
    text = models.TextField()
    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()
    date = models.DateField()
    img1 = models.ImageField(upload_to="News/", null=True, blank=True)
    img2 = models.ImageField(upload_to="News/", null=True, blank=True)
    video = models.FileField(upload_to="News/", null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    watcher = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class CategoryProjects(models.Model):
    name = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Projects(models.Model):
    category = models.ForeignKey(CategoryProjects, on_delete=models.CASCADE)
    name = models.CharField(max_length=555)
    name_uz = models.CharField(max_length=555)
    name_ru = models.CharField(max_length=555)
    name_en = models.CharField(max_length=555)
    mini_text = models.CharField(max_length=555)
    mini_text_uz = models.CharField(max_length=555)
    mini_text_ru = models.CharField(max_length=555)
    mini_text_en = models.CharField(max_length=555)
    text = models.TextField()
    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()
    date = models.DateField()
    img1 = models.ImageField(upload_to="News/", null=True, blank=True)
    img2 = models.ImageField(upload_to="News/", null=True, blank=True)
    video = models.FileField(upload_to="News/", null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Trips(models.Model):
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    img = models.ImageField(upload_to='Trips/')
    video_or_link = models.IntegerField(choices=(
        (1, 'Link'),
        (2, 'Video'),
    ))
    video = models.FileField(upload_to="Trips/", null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class AboutXPK(models.Model):
    name = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    text = models.TextField()
    text_uz = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()
    img = models.ImageField(upload_to="About XPK/")
    text1 = models.TextField()
    text1_uz = models.TextField()
    text1_ru = models.TextField()
    text1_en = models.TextField()


class Visitors(models.Model):
    quantity = models.IntegerField()
    date = models.DateField()


class VisitPoIp(models.Model):
    ip = models.CharField(max_length=255)
    date = models.DateField()


class Streaming(models.Model):
    link = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    title = models.CharField(max_length=255)
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


class Photos(models.Model):
    photo = models.ImageField(upload_to="Photos/")


class Videos(models.Model):
    img = models.ImageField(upload_to="Videos/")
    video_or_url = models.IntegerField(choices=(
        (1, 'video'),
        (2, 'link')
    ))
    video = models.FileField(upload_to="Videos/", null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True)

