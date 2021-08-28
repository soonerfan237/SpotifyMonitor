#TODO: email results of missing songs
import datetime
import smtplib

import read_config


def format_results(missing_songs, start_time):
    processing_time = datetime.datetime.now() - start_time
    contents = "Processing time - " + str(processing_time) + "\n"
    contents = contents + str(len(missing_songs)) + " missing songs.\n"
    contents = contents + "Artist | Song \n"
    for song in missing_songs:
        contents = contents + song["artist_name"] + " | " + song["song_name"] + "\n"
    return contents

def email_results(missing_songs, start_time):
    sent_from = "From: " + read_config.get_sender_email_address() + "\n"
    sent_to = "To: " + read_config.get_recipient_email_address() + "\n"
    subject = "Subject: Spotify Missing Songs Report\n"
    body = format_results(missing_songs, start_time)
    email_text = sent_from + sent_to + subject + body
    print(email_text)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(read_config.get_sender_email_address(), read_config.get_sender_email_password())
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

        print("Email sent!")
    except:
        print("Something went wrong with email.")
