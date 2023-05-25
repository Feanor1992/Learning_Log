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

