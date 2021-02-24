# Sotarks Remover
# Restart#0001
import os
import getpass
from src.Beatmap_remover.Utils.clear import clear
from src.Beatmap_remover.Listeners.onRemove import onRemove
os.system("title "+'Beatmaps remover by Restart#0001')
pc_name = getpass.getuser()

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def main():
    with open(os.path.join(__location__, 'songs_folder.txt')) as songs_folder_file:
        songs_file = songs_folder_file.readline()

        if os.path.exists(songs_file):
            artist = input('Beatmaps creator username: ')
            onRemove(songs_folder=songs_file, artist=artist)

        else:
            clear()
            print(f"Could not find the folder {songs_file}")
            input("Press enter to continue")
            main()


main()
