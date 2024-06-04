import datetime

# timestamp→ timezone
timestamp = 1714094152  # Example Unix timestamp

# Create a timezone-aware datetime object in UTC
date_time = datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc)

print(date_time)

# timezone→ timestamp
# Assuming 'date_time' is a timezone-aware datetime object in UTC
date_time = datetime.datetime(2026, 10, 20, 21, 20, tzinfo=datetime.timezone.utc)

# Convert the timezone-aware datetime object back to a Unix timestamp
unix_timestamp = date_time.timestamp()

print(unix_timestamp)