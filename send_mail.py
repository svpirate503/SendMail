import smtplib
import em
def send_mail(emaill,password):
    root = smtplib.SMTP('smtp.gmail.com:587')
    root.starttls()  
    root.login(emaill,password)
    message = "Mensaje de Python"
    root.sendmail(em.email,em.to,message)


send_mail(em.email,em.password)
