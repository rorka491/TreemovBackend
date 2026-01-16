from datetime import datetime, time, timedelta


def time_diff(start_time: time, end_time: time) -> timedelta:
    return timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second) - timedelta(
        hours=end_time.hour, minutes=end_time.minute, seconds=end_time.second
    )

