import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

senders = {
    'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
    'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123#',
'rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1',
'nicrey4@comcast.net': 'Dabears54',
'mordechai@mail.com': 'Mordechai',
'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
'tarabedford@comcast.net': 'Money4me',
'mycockneedsit@mail.com': 'benjamin3',
'saralaine@mail.com': 'sarlaine12!1',
'jonb2006@verizon.net': '1969Camaro',
'rjhssa1@verizon.net': 'Donna613*',
'cameron.doug@charter.net': 'Jake2122$',
'bridget.shappell@comcast.net': 'Brennan1',
'rugs8@comcast.net': 'baseball46',
'averyjacobs3@mail.com': '1960682644!',
'lstefanick@hotmail.com': 'Luv2dance2',
'bchavez123@mail.com': 'aadrianachavez',
'lukejamesjones@mail.com': 'tinkerbell1',
'emahoney123@comcast.net': 'Shieknmme3#',
'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
'jet747@cox.net': 'Sadie@1234',
'landsgascareservices@mail.com': 'Alisha25@',
'samantha224@mail.com': 'Madden098!@',
'kbhamil@wowway.com': 'Carol1940',
'email@bjasper.com': 'Lhsnh4us123!',
'biggsbrian@cox.net': 'Trains@2247Trains@2247',
'dzzeblnd@aol.com': 'Geosgal@1',
'jtrego@indy.rr.com': 'Jackwill14!',
'chrisphonte.rj@comcast.net': 'Junior@3311',
'tvwifiguy@comcast.net': 'Bill#0101',
'defenestrador@mail.com': 'm0rb1d8ss',
'glangley@gmx.com': 'ironhide',
'charlotte2850@hotmail.com': 'kelalu2850'

}
receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def logo():
    
    print("TG KILLER")


def menu():
    print("1. Account.")
    print("2. Channel.")
    print("3. Authors")
    print("4. Bot")
    choice = input("Choose category: ")
    return choice
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    logo()
    choice = menu()
    
    if choice == '1':
        print("1. Spamming")
        print("2. Doxing")
        print("3. Trolling")
        print("4. Destroying sessions")
        print("5. With premium")
        print("6. With virtual number")
        comp_choice = input("Choose: ")
        
        if comp_choice in ["1", "2", "3"]:
            print("Follow the instructions.")
            username = input("Username without \'@\': ")
            id = input("TG ID: ")
            chat_link = input("Chat link (chat should be public): ")
            violation_link = input("Link to the offending message: ")
            print("Wait a little bit")
            comp_texts = {
            "1": [
                f"Hello, dear support. I found a user on your platform who sends a lot of unnecessary messages - SPAM. His username is {username}, his ID is {id}, chat link is {chat_link}, violation link is {violation_link}. Please take action against this user.",
                f"Hi Telegram support, this user is spamming, please help. This is his account: username: {username}, ID: {id}, chat link: {chat_link}, violation link: {violation_link}."
            ],
            "2": [
                f"Hello, dear support, I found a user on your platform who is distributing other people's data without their consent. His username is {username}, his ID is {id}, chat link is {chat_link}, link to violation is {violation_link}. Please take action against this user by blocking his account.",
                f"Hi Telegram support, this user is doxing people. Please take action. Username: {username}, ID: {id}, chat link: {chat_link}, violation link: {violation_link}."
            ],
            "3": [
                f"Hello, dear Telegram support. I found a user who openly uses foul language and spams in chats. His username is {username}, his ID is {id}, the link to the chat is {chat_link}, the link to the violation is {violation_link}. Please take action against this user by blocking his account.",
                f"Hi Telegram support, this user is trolling and using foul language. Please take action. Username: {username}, ID: {id}, chat link: {chat_link}, violation link: {violation_link}."
            ]
        }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'Complaint on telegram user', comp_body)
                    print(f"Message was sent to {receiver} from {sender_email}!")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice == "4":
            print("Follow the instructions.")
            username = input("Username without \'@\': ")
            id = input("TG ID: ")
            print("Wait a little bit")
            comp_texts = {
                "4": f"Hello, dear support. I accidentally clicked on a phishing link and lost access to my account. Its username is {username}, its ID is {id}. Please delete the account or reset the sessions"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Complaint on telegram user', comp_body)
                    print(f"Message was sent to {receiver} from {sender_email}!")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice in ["5", "6"]:
            print("Follow the instructions.")
            username = input("Username without \'@\': ")
            id = input("TG ID: ")
            comp_texts = {
                "5": f"Good day, Telegram support! Account {username}, {id} uses a virtual number purchased on the number activation website. It has no relation to the number, the number does not relate to it in any way. Please sort this out. Thanks in advance!",
                "6": f"Hello Telegram support! Account {username} {id} purchased premium in your messenger to send spam messages and bypass Telegram restrictions. Please check this complaint and take action!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Complaint on telegram user', comp_body)
                    print(f"Message was sent to {receiver} from {sender_email}!")
                    sent_emails += 9999
                    time.sleep(5)


    elif choice == "2":
        
        print("1. Personal data")
        print("2. Animal abuse")
        print("3. Child pornography")
        print("4. Illegal services")
        ch_choice = input("Choose: ")

        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input("Link on channel: ")
            channel_violation = input("Link on violation: ")
            print("Wait a little bit")
            comp_texts = {
                "1": f"Hello, dear Telegram support. I found a channel on your platform that distributes personal data of innocent people. Channel link - {channel_link}, links to violations - {channel_violation}. Please block this channel.",
                "2": f"Hello, dear Telegram support. I found a channel on your platform that distributes animal cruelty. Channel link - {channel_link}, links to violations - {channel_violation}. Please block this channel.",
                "3": f"Hello, dear Telegram support. I found a channel on your platform that distributes pornography involving minors. Channel link - {channel_link}, links to violations - {channel_violation}. Please block this channel.",
                "4": f"Hello, dear Telegram moderator, I want to complain to you about channel that sells doxing and swatting services. Telegram channel link: {channel_link} Violation link: {channel_violation} Please block this channel."
                }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Complaint on telegram user', comp_body)
                    print(f"Message was sent to {receiver} from {sender_email}!")
                    sent_emails += 100000
                    time.sleep(5)

    elif choice == "3":
        print("falc")

    elif choice == "4":
        print("1. Personal data")
        print("2. Developing.......")
        bot_ch = input("Choose: ")

        if bot_ch == "1":
            bot_user = input("Bot username: ")
            print("Wait a little bit")
            comp_texts = {
                "1": f"Hello, dear Telegram support. I found a bot on your platform that searches for personal data of your users. Link to the bot - {bot_user}. Please sort this out and block this bot."
                }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Complaint on telegram user', comp_body)
                    print(f"Message was sent to {receiver} from {sender_email}!")
                    sent_emails += 1
                    time.sleep(5)
        
        

  
if __name__ == "__main__":
    main()
