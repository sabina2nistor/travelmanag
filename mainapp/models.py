from django.db import models

class Travel(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Travel({})".format(self.name)

    class Meta:
        db_table = "Travel"

class Destination(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    travel = models.ForeignKey(Travel,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Destination({},{})".format(self.country,self.city)

    class Meta:
        db_table = "Destination"



