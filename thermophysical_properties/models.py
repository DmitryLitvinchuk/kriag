from django.db import models



# class Post(models.Model):
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200, blank=True, null=True)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.TextField(max_length=150, blank=True)
#     gender = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     info = models.TextField(max_length=500, blank=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# #Вещество
# class Substance(models.Model):
#     #Название
#     name = models.CharField(max_length=30)
#     #Химическая формула
#     chemical_formula = models.CharField(max_length=30, blank=True)

#     def __str__(self):
#         return "%s %s" % (self.name, self.chemical_formula)

#     class Meta:
#         verbose_name = 'Вещество'
#         verbose_name_plural = 'Вещества'

# #Таблицы физических свойств криопродуктов

# #Таблица 1.1
# #Усредненный состав сухого воздуха [31]
# class ACDA(models.Model):
#     #Компонент
#     component = models.ForeignKey(Substance, on_delete=models.CASCADE)
#     #Химическая формула
#     chemical_formula = models.CharField(max_length=30, blank=True)
#     #Объемная доля компонента в воздухе, %
#     cvf = models.CharField(max_length=100)
#     #Массовая доля компонента в воздухе, %
#     cmf = models.CharField(max_length=100)

