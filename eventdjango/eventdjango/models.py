from django.db import models


class Event(models.Model):
    def __unicode__(self):
        return self.title
    title = models.CharField("Title", max_length=50)
    subtitle = models.CharField("Subtitle", max_length=100, blank=True)
    slogan = models.CharField("Slogan", max_length=255, blank=True) # or tagline
    about = models.TextField("About") # or description
    start_date = models.DateTimeField("Start Date Time")
    end_date = models.DateTimeField("End Date Time")
    organizer = models.CharField("Organizer", max_length=255) # can be an institution, company, person, or group
    email = models.EmailField("Contact Email", max_length=75)
    phone = models.CharField("Phone Number", max_length=20, blank=True)
    homepage = models.URLField(blank=True)
    logo = models.ImageField("Logo", upload_to='photos/events', blank=True)
    venue = models.CharField("Venue", max_length=255)

# Commented because the event can be general which doesn't fit into any subclasses
#    class Meta:
#        abstract = False

class Conference(Event):


class Hackathon(Event):


class Talk(Event):
    sp_name = models.CharField("Speaker Name", max_length=100)
    sp_email = models.EmailField("Speaker Email", max_length=75)
    sp_phone = models.CharField("Speaker Phone", max_length=20, blank=True)
    photo = models.ImageField("Logo", upload_to='photos/events', blank=True)
