import datetime
import time
import calendar

# 1. Get current date and time
def current_datetime():
    return datetime.datetime.now()

# 2. Get current date
def current_date():
    return datetime.date.today()

# 3. Get current time
def current_time():
    return datetime.datetime.now().time()

# 4. Convert string to datetime object
def string_to_datetime(date_str, format='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.strptime(date_str, format)

# 5. Convert datetime object to string
def datetime_to_string(date_obj, format='%Y-%m-%d %H:%M:%S'):
    return date_obj.strftime(format)

# 6. Add days to current date
def add_days_to_current_date(days):
    return datetime.date.today() + datetime.timedelta(days=days)

# 7. Subtract days from current date
def subtract_days_from_current_date(days):
    return datetime.date.today() - datetime.timedelta(days=days)

# 8. Add seconds to current time
def add_seconds_to_current_time(seconds):
    now = datetime.datetime.now()
    return now + datetime.timedelta(seconds=seconds)

# 9. Get day of the week
def day_of_week(date_obj):
    return date_obj.strftime('%A')

# 10. Get week number
def week_number(date_obj):
    return date_obj.isocalendar()[1]

# 11. Get first day of the month
def first_day_of_month(date_obj):
    return date_obj.replace(day=1)

# 12. Get last day of the month
def last_day_of_month(date_obj):
    next_month = date_obj.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

# 13. Get the number of days in a month
def days_in_month(year, month):
    return calendar.monthrange(year, month)[1]

# 14. Check if a year is a leap year
def is_leap_year(year):
    return calendar.isleap(year)

# 15. Get timestamp from datetime object
def datetime_to_timestamp(date_obj):
    return time.mktime(date_obj.timetuple())

# 16. Convert timestamp to datetime object
def timestamp_to_datetime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

# 17. Get the current Unix timestamp
def current_timestamp():
    return int(time.time())

# 18. Format datetime with timezone
import pytz
def current_time_with_timezone(timezone='UTC'):
    tz = pytz.timezone(timezone)
    return datetime.datetime.now(tz)

# 19. Get the difference in days between two dates
def date_difference(date1, date2):
    return (date2 - date1).days

# 20. Check if a given date is weekend
def is_weekend(date_obj):
    return date_obj.weekday() >= 5  # Saturday or Sunday

# 21. Get date of next Monday
def next_monday():
    today = datetime.date.today()
    days_ahead = 0 - today.weekday() + 7  # Monday is 0
    return today + datetime.timedelta(days=days_ahead)

# 22. Get date of last Friday
def last_friday():
    today = datetime.date.today()
    days_ago = today.weekday() - 4  # Friday is 4
    return today + datetime.timedelta(days=days_ago)

# 23. Get current time in ISO format
def current_time_iso():
    return datetime.datetime.now().isoformat()

# 24. Get the number of days until next weekend
def days_until_weekend():
    today = datetime.date.today()
    return 5 - today.weekday() if today.weekday() < 5 else 0

# 25. Parse and format date in multiple formats
def parse_and_format_date(date_str, input_format='%Y-%m-%d', output_format='%d-%m-%Y'):
    parsed_date = datetime.datetime.strptime(date_str, input_format)
    return parsed_date.strftime(output_format)

# 26. Get the start and end date of the current week
def start_and_end_of_current_week():
    today = datetime.date.today()
    start_of_week = today - datetime.timedelta(days=today.weekday())  # Monday
    end_of_week = start_of_week + datetime.timedelta(days=6)  # Sunday
    return start_of_week, end_of_week

# 27. Get the current month and year
def current_month_year():
    now = datetime.datetime.now()
    return now.month, now.year

# 28. Get number of seconds since epoch
def seconds_since_epoch():
    return int(time.time())

# 29. Get the last day of the year
def last_day_of_year(year):
    return datetime.date(year, 12, 31)

# 30. Convert to UTC from local time
def to_utc(local_datetime):
    local_timezone = pytz.timezone("US/Eastern")  # adjust for local timezone
    local_time = local_timezone.localize(local_datetime)
    return local_time.astimezone(pytz.utc)

# 31. Get ISO week number
def iso_week_number(date_obj):
    return date_obj.isocalendar()[1]

# 32. Check if current date is a workday
def is_workday():
    today = datetime.date.today()
    return today.weekday() < 5

# 33. Get the next n working days
def next_n_working_days(n):
    today = datetime.date.today()
    days_added = 0
    while days_added < n:
        today += datetime.timedelta(days=1)
        if today.weekday() < 5:  # If it's a weekday
            days_added += 1
    return today

# 34. Calculate time difference between two datetime objects
def time_difference(datetime1, datetime2):
    return abs(datetime2 - datetime1)