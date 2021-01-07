""" Models for the ViloSky app. """
from django.db import models
from cuser.models import AbstractCUser


class CustomUser(AbstractCUser):
    """ A model to hold the user entity with a unique email instead of username.
    Otherwise, it contains all other fields that a normal user has (first_name,
    last_name, email, password, etc.)
    """
    middleNames = models.CharField(max_length=100)


class UserProfile(models.Model):
    """ A model to hold the actual user profile related to a user. It also contains
    flags relevant to permissions indicating if the user is an HR rep or a ViloSky
    admin.
    TODO @Alex - Discuss having sector, status, even company? as choices field.
    """
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_vilosky_admin = models.BooleanField(default=False)
    is_hr_representative = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    company = models.CharField(max_length=255, null=True)
    employment_sector = models.CharField(max_length=255, null=True)
    employment_status = models.CharField(max_length=255, null=True)
    time_worked_in_industry = models.DurationField(null=True)


class Qualification(models.Model):
    """ A model to hold qualifications related to a user.
    TODO @Alex - Discuss having level and subjects as choices field.
    """
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='qualifications')
    level = models.CharField(max_length=255)
    subjects = models.CharField(max_length=255)


class Paragraph(models.Model):
    """ A model to hold paragraphs of text which will form a report.
    Related to the ViloSky admin who has created them.
    """
    created_by = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='paragraphs_created')
    static_text = models.TextField()


class Link(models.Model):
    """ A model to hold links, part of each paragraph. """
    paragraph = models.ForeignKey(
        Paragraph, on_delete=models.CASCADE, related_name='links')
    url = models.URLField()


class Keyword(models.Model):
    """ A model to hold keywords, part of each paragraph. """
    paragraph = models.ForeignKey(
        Paragraph, on_delete=models.CASCADE, related_name='keywords')
    key = models.CharField(max_length=255)
    score = models.IntegerField()


class Action(models.Model):
    """ A model to hold actions, part of each paragraph. """
    paragraph = models.ForeignKey(
        Paragraph, on_delete=models.CASCADE, related_name='actions')
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)


class Report(models.Model):
    """ A model to hold reports consisting of multiple paragraphs.
    Each report is assigned to an individual user.
    """
    paragraphs = models.ManyToManyField(
        Paragraph, related_name='reports_included_in')
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='reports_assigned')


class Session(models.Model):
    """ A model to hold page sessions data. A session may be related to a user
    but it may also not if the actual user is not register or logged in.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    page = models.CharField(max_length=255)
    time_spent_on_page = models.DurationField()
    clicks_on_page = models.PositiveIntegerField()
