from django.db import models
class Member(models.Model):
    member_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

class Post(models.Model):
    parent = models.ForeignKey('self', null=True, related_name='comments')
    post_id = models.CharField(max_length=255, unique=True)

    member = models.ForeignKey(Member, related_name='posts')
    message = models.TextField()
    link = models.TextField(blank=True, null=True)
    link_name = models.TextField(blank=True, null=True)
    num_likes = models.IntegerField(null=True)
    num_comments = models.IntegerField(null=True)
    
    date_added = models.DateTimeField(auto_now_add=True) 
    #FB date and time
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField(null=True)


    def __unicode__(self):
        return "%s - %s..." % (self.member.name, self.message[:10])

    @property
    def message_short(self):
        return "%s..." % self.message[:255]

    class Meta:
        ordering = ('date_created',)
