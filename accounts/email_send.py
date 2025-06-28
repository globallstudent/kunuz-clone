from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template, TemplateDoesNotExist
from celery import shared_task


@shared_task
def send_email(subject, intro_text, email, token, template=None, password=None):
    to_email = email
    context = {
        "subject": subject,
        "intro_text": intro_text,
        "token": token,
        "password": password,
        "frontend_url": "voocommerce.com",
    }
    if template:
        try:
            html_content = render_to_string(template, context)
            email_message = EmailMessage(subject, html_content, to=[to_email])
            email_message.content_subtype = "html"
        except TemplateDoesNotExist:
            # Fallback to plain text
            body = f"{intro_text}\nToken: {token}\nPassword: {password if password else ''}"
            email_message = EmailMessage(subject, body, to=[to_email])
    else:
        body = f"{intro_text}\nToken: {token}\nPassword: {password if password else ''}"
        email_message = EmailMessage(subject, body, to=[to_email])
    email_message.send()
