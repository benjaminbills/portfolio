from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_email(name, message, email):
  # Creating message subject and sender
  subject = 'New Contact from portfolio site'
  sender = 'oneobaben@gmail.com'
  reciever = 'obafemibenjamins@gmail.com'
  text_content = render_to_string('email/message.txt',{"name": name, "message":message,'email':email})
  html_content = render_to_string('email/message.html',{"name": name, "message":message,'email':email})

  msg = EmailMultiAlternatives(subject,text_content,sender,[reciever])
  msg.attach_alternative(html_content,'text/html')
  msg.send()