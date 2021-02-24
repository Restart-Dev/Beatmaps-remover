import os


def onRemove(songs_folder, artist):
    removed_bm = 0

    if songs_folder.endswith("\\"):
        songs_folder = songs_folder
    else:
        songs_folder = f'{songs_folder}\\'

    artist = artist.lower()
    with os.scandir(songs_folder) as beatmaps:
        for beatmap_folder in beatmaps:
            with os.scandir(songs_folder + beatmap_folder.name) as beatmaps_files:
                for file in beatmaps_files:
                    if file.name.endswith(".osu"):
                        with open(f'{songs_folder}{beatmap_folder.name}\\{file.name}', encoding="utf8") as __beatmap__:
                            options = __beatmap__.readlines()
                            for line in options:
                                if f'creator:{artist}' in line.lower():
                                    __beatmap__.close()
                                    os.remove(f'{songs_folder}{beatmap_folder.name}\\{file.name}')
                                    print(f"Removed {file.name}")
                                    removed_bm = removed_bm + 1

                                else:
                                    pass
    print(f"\nRemoved {removed_bm} Beatmaps from {artist}")
    input('Press enter to exit.')
    exit(0)
