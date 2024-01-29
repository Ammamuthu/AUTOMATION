import subprocess
import time
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


logging.basicConfig(filename='Db_status.log',format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S')
log = []

# Mail setup
smtpServer = '121.243.77.117'
smtpPort = 587  # Port for TLS  
fromAddr = 'ammamuthu.m@3i-infotech.com'
toAddr = 'ammamuthu.m@3i-infotech.com'
paswrd = 'BattleisON@22'

to_adres_lst =['ammamuthu.m@3i-infotech.com']
server = smtplib.SMTP(smtpServer, smtpPort)
server.starttls()
server.login(fromAddr, paswrd)

while True:
    def check_database_status(hostname, port, service_name):
     # Construct the TNS entry
        tns_entry = f'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST={hostname})(PORT={port}))(CONNECT_DATA=(SERVICE_NAME={service_name})))'

     # Use tnsping to check the status
        command = f'tnsping {tns_entry}'

        try:
            subprocess.run(command, check=True, shell=True)
            logging.warning(f"The database on {hostname}:{port}/{service_name} is UP.")
        except subprocess.CalledProcessError as e:
            err = f"The database on {hostname}:{port}/{service_name} is DOWN. Error: {e}"
            logging.warning(err)
            log.append(err)

    # Check if there are any issues and send an email
    if log:
        email_subject = "Database Status Alert"
        email_body = "\n".join(log)
        # Create a MIMEText object to include HTML content
        html_content = f"""
        <html>
            <body>
                <header style="color:White; font-weight:bolder;">Website is Down</header>
                <tr><p style="color:black; font-weight:bold;">{email_body}</p></tr>
            </body>
        </html>
        """
    for to_email in to_adres_lst:

       email_message = MIMEMultipart()
       email_message.attach(MIMEText(html_content, 'html', 'utf-8'))
       email_message['Subject'] = email_subject
       email_message['From'] = fromAddr
       email_message['To'] = to_email

       server.sendmail(fromAddr, to_email, email_message.as_string())
       print(f"MAIL SENT to {to_email}....")



    print(log)
    log.clear()

   
    logging.warning('.....................................')
    print("Executing the script...")

    # Example usage

    database = [{"hostname": "localhost", "port": "1521", "service_name": "xe"},
            {"hostname": "10.50.1.19", "port": "1521", "service_name": "demo"}]

    for db in database:
        check_database_status(db["hostname"], db["port"], db["service_name"])

    time.sleep(100)

server.quit()

