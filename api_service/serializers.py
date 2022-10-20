from rest_framework import serializers

from .tasks import create_pdf
from . import models


class OrderSerializer(serializers.Serializer):
    point_id = serializers.IntegerField()
    order_id = serializers.IntegerField()
    order = serializers.JSONField()

    def create(self, validated_data):
        point_id = validated_data.get('point_id')
        printers = models.Printer.objects.filter(point_id=point_id)
        checks = [models.Check(printer_id=printer, type=printer.check_type,
                               order=validated_data, status='new')
                  for printer in printers]
        instances = models.Check.objects.bulk_create(checks)
        for check in instances:
            order_list = list()
            for element, value in check.order.get('order').items():
                new_element = dict()
                new_element['name'] = element
                new_element['value'] = value
                order_list.append(new_element)
            template = 'api_service/check_form.html'
            create_pdf.delay(template, check.order.get('order_id'), check.type,
                                       order_list, check.id)
        return instances

    def validate_point_id(self, value):
        printers = models.Printer.objects.filter(
            point_id=value)
        if not printers.exists():
            raise serializers.ValidationError(
                'У этой точки нет ни одного принтера'
            )
        return value

    def validate_order_id(self, value):
        point_id = self.initial_data.get('point_id')
        checks = models.Check.objects.all().values('order')
        printers = models.Printer.objects.filter(point_id=point_id)
        list_of_bills = list()
        for check in checks:
            list_of_bills.append(check.get('order').get('order_id'))
        if list_of_bills.count(value) == len(printers):
            raise serializers.ValidationError(
                    'Чеки для этого заказа уже были созданы.'
                )
        return value


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Check
        fields = '__all__'

