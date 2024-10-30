from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from celery import shared_task
from .models import periodicMessage

fromEmail = "contacto@danielsotodev.com"

@shared_task()
def sendEmail(to, mensaje):
    try:
        subject = f'Mail enviado'
        to_email = [to]
        msg_html = render_to_string("emails/mailTemplates/correoEnviado.html", {
            'mensaje': mensaje,
        })
        msg = EmailMessage(subject=subject, body=msg_html, from_email=fromEmail, bcc=to_email)
        msg.content_subtype = "html"  # Main content is now text/html
        mail_sent = msg.send()
    except Exception as e:
        print(f"Se produjo una excepción: {str(e)}")
        mail_sent = 0
    return mail_sent



@shared_task
def my_scheduled_task():
    # Tu lógica aquí
    nuevoMensaje = periodicMessage(
        message = "Este mensaje es periodico"
    )
    nuevoMensaje.save()
