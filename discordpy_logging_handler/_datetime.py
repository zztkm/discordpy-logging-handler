from datetime import datetime


def aware_now() -> datetime:
    now = datetime.now()
    return now
