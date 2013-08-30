#!/usr/bin/python

# Gets stuff from Pitchfork's awesome 'Best New Music' section
# Note: this is just regexing the HTML... so may stop working if page structure changes
# This is not written by, or affiliated with Pitchfork at all

import urllib2
import re


def GetPitchforkData():
  # grab all the data...
  web_page = urllib2.urlopen('http://www.pitchfork.com/best')
  all_the_html = web_page.read()
  # parse for Best New stuff...
  demarcator = 'bnm-hub-features-1' # surrounds first row of best new things
  relevant_block = re.findall(demarcator+'(.*?)'+demarcator, all_the_html)[0]
  return relevant_block


def BestNewArtist():
  relevant_block = GetPitchforkData()
  relevant_artist = re.findall('h1>'+'(.*?)'+'</h1', relevant_block)
  return relevant_artist[0]


def BestNewAlbum():
  relevant_block = GetPitchforkData()
  relevant_album = re.findall('h2>'+'(.*?)'+'</h2', relevant_block)
  return relevant_album[0]
  

# Use this to test; it should print artist and album on command line
def main():
  
  test_artist = BestNewArtist()
  test_album = BestNewAlbum()
  
  print '\n>>>>>>>>>>>>>>>>>\n'
  print test_artist
  print test_album
  print '\n>>>>>>>>>>>>>>>>>\n'


if __name__ == '__main__':
    main()
