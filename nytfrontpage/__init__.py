# coding: utf-8
import requests
from datetime import date
from datetime import datetime
from datetime import timedelta

__version__ = '0.1.0'

def get_image_url(date):
  """ Return the URL to the frontpage of the NYT on a certain date.

  :param date: a `datetime.date` object.
  :returns: a `str`, the URL to the image of the frontpage of the NYT on the
      requested date.
  """

  _frontpage_url_template = ('http://www.nytimes.com/images'
                             '/{year}/{month}/{day}/nytfrontpage/scan.jpg')
  return _frontpage_url_template.format(
      year=date.year,
      month=str(date.month).zfill(2),
      day=str(date.day).zfill(2),
    )

def get_image_data(date):
  """ Attempts to download the frontpage for a given date.

  :param date: a `datetime.date` object.
  :returns: a `str`, the contents of the image of the frontpage of the NYT on
      the requested date, or `None` if that image is not available.
  """
  response = requests.get(get_image_url(date), headers={
      'Host' : 'hsadvisory.lmsd.org',
      'User-Agent' : ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; '
                      'rv:9.0.1) Gecko/20100101 Firefox/9.0.1'),
      'Accept-Language' : 'en-us,en;q=0.5',
      'Accept-Encoding' : 'gzip, deflate',
      'Accept-Charset' : 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
      'Referrer' : 'http://www.nytimes.com/',
    })
  if response.status_code == 200:
    return response.content

  return None
