from __future__ import unicode_literals

from django.db import models

# Create your models here.
'''
Common Info:
  Source language:
  Language level (how to define this. start simple)
    Novice, Intermediate, Advanced
  Country of origin
  List links to source sites
    Free access
    Purchase access
  Initial publication date

Audio/Video:
  Common Info:
    Dubbed languages
    Type (live action, animated)
    Main characters types
    Available subtitles
    Available scripts
    Genre
    Quality
  Films
  TV Series
    Number of seasons
    Number of episodes

Written
  Common Info:
    Translations available
    Glossary
    Access
      Online, purchase, website, app, store
    Number of pages
    Unknown words per page
    Number of pictures
    Target audience
    Popup dictionary-able
    Supported media
      nook, kindle, iOS, Android, etc.

  Books
    Genre
  Comics
    Genre
  Newspapers
    Type
  Magazine / Articles
    Genre
    Subject
    Length of articles (range or average)

Audio
  Common Info:
    Type
    Genre
    Political View
    Access
      online, purchase, website, app, station
    Transcripts available
  Radio
  Podcasts
    Audio/video?

Apps
  Type
  Supported operating systems



'''

class MediaBase(models.Model):
  source_language = models.CharField(50)
  language_level = models.PositiveSmallIntegerField()
  country_of_origin = models.CharField(50)
  links = models.URLField()

  class Meta:
        abstract=True # Set this model as Abstract

class Film(MediaBase):
  dubbed_languages = models.CharField(50)
  type = models.CharField(50)
  avaiable_subtitles = models.CharField(50)
  available_scripts = models.CharField(50)
  genre = models.CharField(50)
  video_quality = models.CharField(50)

class TvShow(MediaBase):
  dubbed_languages = models.CharField(50)
  type = models.CharField(50)
  avaiable_subtitles = models.CharField(50)
  available_scripts = models.CharField(50)
  genre = models.CharField(50)
  video_quality = models.CharField(50)
