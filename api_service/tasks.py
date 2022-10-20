import time
from wkhtmltopdf import wkhtmltopdf, RenderedFile
from service_food.celery import app
from .models import Check
from celery import shared_task


@shared_task
def create_pdf(template, order_id, printer_type, order_list, check_id,
               context: dict = dict):
    context['order_id'] = order_id
    context['order_list'] = order_list
    context['printer_type'] = printer_type
    file = RenderedFile(template=template,
                        context=context)
    wkhtmltopdf(pages=[file.filename],
                       output=f'media/pdf/{order_id}_{printer_type}.pdf')
    check_instance = Check.objects.get(id=check_id)
    check_instance.status = 'rendered'
    check_instance.pdf_file = f'pdf/{order_id}_{printer_type}.pdf'
    check_instance.save()


