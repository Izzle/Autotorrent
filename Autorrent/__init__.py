import os


def creation(links='TEMP.txt'):
    torrents = open('torrents.txt', 'r').readlines()
    curr_dir = os.getcwd()
    torr_dir_name = 'test_torrent_directory'
    
    # Get the root directory
    curr_dir = curr_dir[0:3]
    try:
        os.mkdir(curr_dir + torr_dir_name)
    except FileExistsError:
        print('That file already exists.')
        name_folder()
        # create folder save location
        # utorrent api - set default save location
        # parse link and put in api friendly format
        # utorrent api - send "start job" request
        # "          " - pause torrent (may not be needed)
        # change default save location, reparse, and send now
        #     "start job" request
class CreateFolder(name='Torrent_Folder'):
    curr_dir = os.getcwd()
    # Gets root path (ie "C:/" or "C:\")
    curr_dir = curr_dir[0:3]
    try:
        name_directory('What would you like to name the folder where everything will be saved?')
        # f_name = input('What would you like to name the folder where everything will be saved?')
    except Exception as e:
        print(e)
    else:
        print('worked!')


    def name_directory(question='DEFAULT QUESTION',):
        try:
            f_name = input(question)
        except 
        





def cleanup(thing):
    pass

#creation()
name_folder()
