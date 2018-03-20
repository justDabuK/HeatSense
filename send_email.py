import smtplib


def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % to_addr_list
    header += 'Cc: %s\n' % cc_addr_list
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.ehlo()
    server.starttls()
    server.login(login, password)
    server.sendmail(from_addr, to_addr_list, message)
    server.quit()


def main():
    sendemail(
        'heatsense5000@gmail.com',
        'kevinjust87@gmail.com',
        '', 'E-Mail test ',
        'first e-mail test',
        'heatsense5000@gmail.com',
        'TMSBausses'
    )

if __name__ == "__main__":
    main()
