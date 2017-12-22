import os


def creation(links='TEMP.txt'):

    torrents = open('torrents.txt', 'r').readlines()
    torr_dir_name = None

    create_folder()
    # create_folder('TORRENT_NAME_HERE')

    # OUTLINE
    #
    #  create folder save location
    # utorrent api - set default save location
    # parse link and put in api friendly format
    # utorrent api - send "start job" request
    # "          " - pause torrent (may not be needed)
    # change default save location, reparse, and send now
    #     "start job" request


def create_folder(name=None):

    def main():
        curr_dir = os.getcwd()
        # Gets root path (ie "C:/" or "C:\")
        curr_dir = curr_dir[0:3]

        QUESTION = 'What would you like to name the folder where everything will be saved? '
        SUCCESS_REPLY = 'Folder will be named: '
        try:
            if name is not None:
                folder_name = name
            elif name is None:
                folder_name = name_directory(QUESTION, SUCCESS_REPLY)
            os.mkdir(curr_dir + folder_name)
        except FileExistsError:
            print('That file already exists.')
            raise
        except Exception as e:
            print(e)
        else:
            print('Folder created:', curr_dir + folder_name)

    def name_directory(question='DEFAULT QUESTION', success_reply=None):
        try:
            f_name = input(question)
        except Exception as e:
            print(e)
        else:
            if success_reply is not None:
                print(success_reply, f_name)
            return f_name
        finally:
            pass

    main()


def cleanup(thing):
    pass


creation()
