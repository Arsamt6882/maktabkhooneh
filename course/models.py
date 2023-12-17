from django.db import models
from django.db.models import CharField


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self) -> str:
        return f'{self.name}'

class Main_Learn(models.Model):
    name = models.CharField(max_length=50,  choices=[('برنامه‌نویسی', 'برنامه‌نویسی'),
                                                     ('زبان‌های خارجی', 'زبان‌های خارجی'),
                                                     ('آی‌تی و نرم‌افزار', 'آی‌تی و نرم‌افزار'),
                                                     ('مدیریت و کسب و کار', 'مدیریت و کسب و کار'),
                                                     ('مالی و سرمایه‌گذاری', 'مالی و سرمایه‌گذاری'),
                                                     ('دانشگاهی: فنی و مهندسی', 'دانشگاهی: فنی و مهندسی'),
                                                     ('دانشگاهی: علوم‌پایه، انسانی، پزشکی', 'دانشگاهی: علوم‌پایه، انسانی، پزشکی'),
                                                     ('مهارت‌های زندگی', 'مهارت‌های زندگی'),
                                                     ('هنر', 'هنر'),])
    about = models.TextField()

    def __str__(self) -> str:
        return f'{self.name}'


class Sub_Learn(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    subjects = models.ForeignKey(Main_Learn, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Sub_Sub_Learn(models.Model):
    name = models.CharField(max_length=50)
    subjects = models.ForeignKey(Sub_Learn, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name}'

class Course(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length= 10)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    category = models.ForeignKey(Sub_Sub_Learn, on_delete=models.CASCADE)
    description = models.TextField()
    other_courses_needed = models.ForeignKey("self", on_delete=models.CASCADE, blank = True, null = True)
    about = models.TextField()

    def __str__(self) -> str:
        return f'{self.name}'

