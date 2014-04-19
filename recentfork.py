#!/usr/bin/python

# Updates bnm_log.txt if there is new "Best New" data
# from pitchfork.  

# Requires pitchfork-bnm module at
# https://github.com/oldhill/pitchfork-bnm

import pitchfork_bnm.bestnewmusic as bnm

def main():

  # Get historical data from disc
  history_file = open_or_create('bnm_log.txt')
  
  full_history_log = history_file.read()
  latest_historical_set = full_history_log.split('\n')[0] #first line
  history_file.close()

  # Grab latest data from pitchfork.com/best
  current_artist = bnm.BestNewArtist()
  current_album = bnm.BestNewAlbum()
  current_set = current_artist+' -- '+current_album
  
  # Debug 
  print 'latest:  '+latest_historical_set
  print 'current: '+current_set

  # If there's a new set, write new history file
  if current_set != latest_historical_set:
    new_log = current_set+'\n'+full_history_log
    updated_history_file = open('bnm_log.txt', 'w')
    updated_history_file.write(new_log)
    updated_history_file.close()
    print 'file updated!'
  else:
    print 'no updates'

def open_or_create(filename):
  try:  
    file = open(filename, 'r') # If the file exists open it
  except IOError:
    file = open(filename, 'w') # If the file does not exist create it 
    file.close     
    file = open(filename, 'r') # Now open the file
  return file 

if __name__ == '__main__':
  main()
