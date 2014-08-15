from django.db import models

class Flashcard(models.Model):
	def __unicode__(self):
		return self.content
		
	content = models.CharField(max_length=200)
	activedate = models.DateField('Active Date')
	enddate = models.DateField('End Date', null=True, blank=True)
	readdate = models.DateField('Date Read', null=True, blank=True)
	marked = models.BooleanField()
	mastered = models.BooleanField()
	read_status = models.BooleanField()
	times_viewed =  models.IntegerField(default=0,null=True, blank=True)
