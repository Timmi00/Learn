def make_album(
        singer: str,
        album: str,
        tracks: str = None
):
    if tracks:
        catalog: dict = {'singer': singer, 'album': album, 'tracks': tracks}
        print(catalog)
    else:
        catalog: dict = {'singer': singer, 'album': album}
        print(catalog)


while True:
    singer_name: str = input('Введите имя исполнителя: ')
    if not singer_name:
        break
    album_name: str = input('Введите название альбома: ')
    track_numbers: str = input('Введите колличество треков: ')
    make_album(singer_name, album_name, track_numbers)
