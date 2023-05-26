from django.db import models


# We've created a class named Topic that inherits from Model
# a parent class included with Django that defines the basic functionality of a model.
class Topic(models.Model):
    """Topic that made by user"""
    # name topic and max length of the name
    text = models.CharField(max_length=200)

    # add current date and time of topic creation
    date_added = models.DateTimeField(auto_now_add=True)

    # def return string from the text attribute
    def __str__(self):
        """return a string representation of a model"""
        return self.text


class Entry(models.Model):
    """information that user learn on the topic"""
    # the foreign key contains a reference to another record in the database.
    # Thus, each entry is associated with a specific topic.
    # each entry is associated with a specific topic
    # on_delete=models.CASCADE - delete all entries in topic when topic deleted
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """stores additional information on model management"""
        # use the plural form of entries  when referring to moe then one entry
        verbose_name_plural = 'entries'

    def __str__(self):
        """return a string representation of a model"""
        return f'{self.text[:50]}...'

