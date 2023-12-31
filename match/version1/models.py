from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class Department(models.Model):
    department_name = models.CharField(max_length=20)

def upload_to(instance, filename):
    return 'accounts/{filename}'.format(filename=filename)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    role = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to=upload_to, default='accounts/default.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'role', 'department')

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Projects(models.Model):
    title = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='projects')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


class ProjectMilestones(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    milestone = models.CharField(max_length=250)
    milestone_description = models.CharField(max_length=250)
    milestone_complete = models.BooleanField(null=False, default=False)

    
class ProjectComment(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    
class ProjectMilestoneTask(models.Model):
    project_milestone = models.ForeignKey(ProjectMilestones, on_delete=models.CASCADE)
    task = models.CharField(max_length=250)
    completed = models.BooleanField()


class MilestoneTaskSerializer(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    project_milestone = models.ForeignKey(ProjectMilestones, on_delete=models.CASCADE)
    task = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)


class Interest(models.Model):
    interest_name = models.CharField(max_length=20)


class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    account = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class RA(models.Model):
    availability = models.BooleanField(default=True)  # Use BooleanField for true or false
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    account = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Faculty_Interest(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)


class RA_Interest(models.Model):
    rA = models.ForeignKey(RA, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)


class RA_Project(models.Model):
    rA = models.ForeignKey(RA, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500)


class Skills(models.Model):
    skill_name = models.CharField(max_length=400)


class Project_Skills(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)


class RA_Skills(models.Model):
    rA = models.ForeignKey(RA, on_delete=models.CASCADE)
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE)