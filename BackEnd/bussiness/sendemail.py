import smtplib, ssl

class SendEmail:
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "tranquangha31082000@gmail.com"
    password = "xizyjoxtonbwffqk"

    def __init__(self) -> None:
        pass

    def sendEmailConfirmTour(self, tourCode, user):
        receiver_email = user["Email"]
        message = """From: From Tourguide <tranquangha31082000@gmail.com>
                    To: To %s
                    Subject: Confirm Tour

                    Hi. Tourguide has accepted a tour booking request with code: %s. Please log in to the system to confirm your booking. Love
                """ %(user["Email"], tourCode)

        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, message)

    def sendEmailCancelTour(self, tourCode, user):
        receiver_email = user["Email"]
        message = """From: From Tourguide <tranquangha31082000@gmail.com>
                    To: To %s
                    Subject: Confirm Tour

                    Hi. Tourguide has canceled the tour with code: %s. Please contact via chat channel for more information. Love
                """ %(user["Email"], tourCode)

        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, message)