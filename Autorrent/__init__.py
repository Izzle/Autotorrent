import os


def creation(links='TEMP.txt'):
	torrents = open('torrents.txt', 'r').readlines()
	#print(torrents)
	curr_dir = os.getcwd()
	print(curr_dir)
	#os.mkdir('~\test_directory')
        # create folder save location
        # utorrent api - set default save location
        # parse link and put in api friendly format
        # utorrent api - send "start job" request
        # "          " - pause torrent (may not be needed)
        # change default save location, reparse, and send now
        #     "start job" request


def cleanup(thing):
	pass

creation()
