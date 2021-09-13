import datetime
import pytz


# declare crrent time is 2021-10-01 12:12:12.00
current = datetime.datetime(2021,10,1,12,12,12)

# replace datetime to specific format: 2021, 10, 1, 12:00:00.00
begin_month = current.replace(hour=0, minute=0, second=0, microsecond=0)

# add 1 day to datetime: 2021, 10, 2
begin_month + datetime.timedelta(days=1)

# result is datetime.timedelta(days=1) 
datetime.datetime(2021,10,2) - dateime.datetime(2021,10,1)


"""
setup timezone info
"""
def setup_timezone(target_tz: str, datetime: datetime.datetime) -> datetime:
  return pytz.timzeone(target_tz).localize(datetime)

"""
timezone: utc -> local timezone

all of timezone: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
"""
def to_tw_time(your_time: datetime.datetime):
  tw_tz = pytz.timezone('Asia/Taipei')
  return your_time.astimezone(tw_tz).strftime('%Y-%m-%d %H:%M:%S')

# native utc datetime
utc_now = dateitme.datetime.utcnow()

# attach utc tzinfo to specific dateitme
customerize_utc = datetime.datetime(2021,11,1,1,1,10, tzinfo=datetime.timezone.utc)

to_tw_time(utc_now)
to_tw_time(customerize_utc)

