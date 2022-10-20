from django.db import models

# Create your models here.


class Printer(models.Model):
    name = models.CharField(max_length=20)
    api_key = models.CharField(max_length=20, unique=True)
    check_type = models.CharField(choices=[('kitchen', 'kitchen'),
                                           ('client', 'client')],
                                  max_length=9)
    point_id = models.IntegerField()

    def __str__(self):
        return f'{self.point_id} - {self.name} {self.check_type}'


class Check(models.Model):
    printer_id = models.ForeignKey(Printer, on_delete=models.PROTECT)
    type = models.CharField(choices=[('kitchen', 'kitchen'),
                                     ('client', 'client')],
                            max_length=9)
    order = models.JSONField()
    status = models.CharField(choices=(('new', 'new'),
                                       ('rendered', 'rendered'),
                                       ('printed', 'printed')),
                              max_length=9)
    pdf_file = models.FileField(upload_to='./media/pdf/', null=True)

    def __str__(self):
        return f'{self.printer_id} {self.status}'


class Order(models.Model):
    point_id = models.IntegerField()
    order = models.JSONField()

    def __str__(self):
        return f'Order # {self.point_id}'
