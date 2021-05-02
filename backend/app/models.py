from django.db import models
from enum import Enum

class Incubators(models.Model):
    id = models.AutoField(primaryKey=True)
    incubator_name = models.CharField(max_length=255)
    location_url = models.CharField(max_length=260)
    city_name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    application = models.CharField(max_length=255)
    post_money_valuation = models.BigIntegerField()

class StartupNeeds(models.Model):
    class StarSystem(models.TextChoices):
        BD = "bad"
        VB = "very_bad"
        ST = "satisfactory"
        GD = "good"
        EX = "excellent"

    startup_id = models.ForeignKey(Incubators, on_delete=models.CASCADE)
    company_linkedIn = models.CharField(max_length=255)
    angellist_url = models.CharField(max_length=255)
    phy_amenities = models.CharField(
        max_length=2,
        choices=StarSystem.choices
    )
    seed_funding = models.CharField(
        max_length=2,
        choices=StarSystem.choices
    )
    research_labs = models.CharField(
        max_length=2,
        choices=StarSystem.choices
    )
    market_access = models.CharField(
        max_length=2,
        choices=StarSystem.choices
    )
    talent_access = models.CharField(
        max_length=2,
        choices=StarSystem.choices
    )
    further_funding = models.CharField(
        max_length=2,
        choices=StarSystem.choices
    )
    networking = models.CharField(
        max_length=2,
        choices=StarSystem.choices
    )
    technical_mentorship = models.CharField(
        max_length=2,
        choices=StarSystem.choices
    )
    logistics = models.CharField(
        max_length=2,
        choices=StarSystem.choices
    )
    business_mentorship = models.CharField(
        max_length=2,
        choices=StarSystem.choices
    )

class Industry(models.Model):
    startup_id = models.IntegerField()
    area_name = models.CharField(max_length=255)

class FocusArea(models.Model):
    inc_id = models.ForeignKey(Incubators, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=255)

class People(models.Model):
    inc_id = models.ForeignKey(Incubators, on_delete=models.CASCADE)
    linkedIn_url = models.CharField(max_length=255)

class PreviousRecommendations(models.Model):
    issue_date = models.DateField()
    startup_id = models.IntegerField(primary_key=True)
    recommendation = models.ForeignKey(Incubators, on_delete=models.CASCADE)
    score = models.IntegerField()
    selection_chance = models.IntegerField()

class PreviousRequests(models.Model):
    class RequirementUrgency(models.TextChoices):
        NR = "not_required"
        SR = "somewhat_required"
        NC = "necessary"
        EN = "extremely_necessary"
        DB = "dealbreaker"

    request_id = models.ForeignKey(PreviousRecommendations, to_field="recommendation")
    request_angellist = models.IntegerField()
    reviews = models.CharField(
        max_length=2,
        choices=RequirementUrgency.choices
    )
class KeyStartups(models.Model):
    startup_id = models.IntegerField(primary_key=True)
    company_linkedIn = models.CharField(max_length=255)
    startup_name = models.CharField(max_length=255)
    inc_id = models.ForeignKey(Incubators, Incubators)
    team_qualification = models.DecimalField()
    previous_experience = models.DecimalField()
    previous_exits = models.DecimalField()

class RequestIndustry(models.Model):
    startup_id = models.ForeignKey(PreviousRequests, to_field="request_id")
    area_name = models.CharField(max_length=255)
