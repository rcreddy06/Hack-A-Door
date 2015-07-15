## Reference: http://pymotw.com/2/smtpd/

import smtplib
import datetime
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    print "Email has been Sent"
    server.quit()
    
sendemail(from_addr    = 'someone@door.com', 
          to_addr_list = ['teamalphahacking@gmail.com'],
          cc_addr_list = [''], 
          subject      = 'Authorization Alert', 
          message      = 'someone was successfully authorized at ' + str(datetime.datetime.now()), 
          login        = 'teamalphahacking@gmail.com', 
          password     = 'Hackathon2015')

