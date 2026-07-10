# notifier.py

from plyer import notification


def show_notification(title, message):
    """
    Display a Windows desktop notification.
    """

    try:

        notification.notify(

            title=title,

            message=message,

            app_name="Employee Report Automation",

            timeout=10

        )

    except Exception as e:

        print("\nUnable to Show Notification")

        print(e)