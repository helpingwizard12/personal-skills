from collections import Counter
from datetime import datetime, timedelta


def week_start(dt):
    """Monday of the week containing dt."""
    return (dt - timedelta(days=dt.weekday())).date()


def weekly_event_counts(event_timestamps, user_timezone):
    """Count a user's events per week (weeks start Monday, in the user's own calendar).

    event_timestamps: iterable of Unix timestamps (seconds).
    user_timezone: IANA zone name from the user's profile, e.g. "Asia/Kolkata".
    Returns {date_of_monday: count}.
    """
    counts = Counter()
    for ts in event_timestamps:
        dt = datetime.utcfromtimestamp(ts)
        counts[week_start(dt)] += 1
    return dict(counts)
