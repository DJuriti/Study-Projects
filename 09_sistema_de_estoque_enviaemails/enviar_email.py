import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

EMAIL = os.getenv("EMAIL")
SENHA = os.getenv("SENHA")

email = EmailMessage()

email["Subject"] = "Relatório de Estoque"
email["From"] = EMAIL
email["To"] = EMAIL  # ou o e-mail do destinatário

email.set_content(
    "Olá!\n\nSegue em anexo o relatório de estoque.\n\nAtenciosamente."
)

with open("relatorio.pdf", "rb") as arquivo:
    pdf = arquivo.read()

email.add_attachment(
    pdf,
    maintype="application",
    subtype="pdf",
    filename="relatorio.pdf"
)

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.starttls()

smtp.login(EMAIL, SENHA)
smtp.send_message(email)
smtp.quit()