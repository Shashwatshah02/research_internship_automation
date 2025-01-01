import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Enter your Email account credentials here !
your_email = "sns@gmail.com"
your_password = ""


server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login(your_email, your_password)

# Define the subject and body of the email
subject = "Exploring Research Internship Opportunity in field of Computer Science and Engineering"
body = (
    "Respected Professor,\n\n"
    
    "I am ______, a Computer Engineering student ........"

"I am highly motivated to contribute to cutting-edge research at your esteemed institution and gain further hands-on experience in AI/ML and IoT ..... . I have attached the link to my resume for your consideration and would be grateful for the opportunity to discuss how I can contribute to your research endeavors.\n\n"
    "Please find my resume linked here: https://drive.google.com/view?usp=sharing \n\n"
    "Best regards,\n"
    "___________\n"
    "D.J. Sanghvi CoE\n"
    "Mumbai, Maharashtra, India\n"
    "+91 __________\n"
    "sns@gmail.com\n"
)


# 
professors = pd.read_csv('UCLA.csv') 

for index, row in professors.iterrows():

    msg = MIMEMultipart()
    msg['From'] = your_email
    msg['To'] = row['email']
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    server.send_message(msg)
    print(f"Email sent to {row['email']}")

server.quit()
