class UploadNotifier:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, func):
        self.subscribers.append(func)

    def notify(self, document_name):
        for func in self.subscribers:
            func(document_name)


def email_notification(document_name):
    print(f"[EMAIL] {document_name} uploaded")

def dashboard_notification(document_name):
    print(f"[DASHBOARD] {document_name} available")