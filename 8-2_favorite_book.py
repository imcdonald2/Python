def make_album(artist_name, artist_album, album_tracks = ''):
    if album_tracks:
        album_contents = {
        'name': artist_name,
        'album': artist_album,
        'track_no': album_tracks
        }
    else:
        album_contents = {
        'name': artist_name,
        'album': artist_album
        }
    return album_contents

album1 = make_album('Jimi Hendrix', 'Are You Experienced?', '13')
album2 = make_album('Guns n Roses', 'Appetite for Destruction', '8')
album3 = make_album('Metallica', 'Master of Puppets')

album_list = [album1, album2, album3]
for album in album_list:
    print album
