import notify2

notify2.init("notify-vaccine")

def showNotification(PINCODE):
    summary = "Vaccine availability notification"
    body = f"There might be some slots available for the vaccine in area {PINCODE}"
    n = notify2.Notification(summary,
                         body,
                         ""
                        )
    n.show()
    

def showError():
    summary = "Notify-Vaccine Conection Error"
    body = f"!!!!!! The code just stopped due to unknown error. Rerun the script after few seconds."
    n = notify2.Notification(summary,
                         body,
                         ""
                        )
    n.show()
