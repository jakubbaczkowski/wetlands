from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.


class ProfileUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name="profile_user")
    first_name = models.CharField(("Vorname"), max_length=150, null=False, blank=True)
    last_name = models.CharField(("Nachname"), max_length=150, null=False, blank=True)
    username = models.CharField(("Benutzername"), max_length=100, null=True)
    email = models.EmailField(("Email-Adresse"), max_length=100, null=True)

    def __str__(self):
        return str(self.username)


class UserStats(models.Model):
    data = models.CharField(("Test"), max_length=150, null=False, blank=True)

    def __str__(self):
        return str(self.data)


class Publications(models.Model):
    id = models.AutoField(primary_key=True)
    id_import = models.IntegerField()
    # TODO: fix type for crossref id
    id_scopus = models.BigIntegerField(blank=True, null=True)
    id_crossref = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    abstract = models.TextField(blank=True, null=True)
    doi = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    pages = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=255, blank=True, null=True)
    volume = models.CharField(max_length=255, blank=True, null=True)
    issue = models.CharField(max_length=255, blank=True, null=True)
    issn = models.CharField(max_length=255, blank=True, null=True)
    journal = models.CharField(max_length=255, blank=True, null=True)
    disciplines = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    first_author_name = models.CharField(max_length=255)
    first_author_scopus_id = models.BigIntegerField(blank=True, null=True)
    first_author_affiliation_name = models.CharField(max_length=255, blank=True, null=True)
    first_author_affiliation_country = models.CharField(max_length=255, blank=True, null=True)
    co_authors = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    keywords = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    citations_count = models.IntegerField(blank=True, null=True)
    references_crossref_id = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    references_scopus_id = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    citation_latest = models.TextField(blank=True, null=True)
    research_method = models.CharField(max_length=255, blank=True, null=True)
    site_description = models.TextField(blank=True, null=True)
    spatial_scale = models.CharField(max_length=255, blank=True, null=True)
    temporal_scale = models.IntegerField(blank=True, null=True)
    ground_truth = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    citation_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}: {self.title} by {self.first_author_name}"
