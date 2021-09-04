class BaseController:
    def __init__(self, google_id):
        self.google_id = google_id


class BaseError(Exception):
    pass
