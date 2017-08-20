def make_album(artist_name, artist_album):
    album_contents = {
    'name': artist_name,
    'album': artist_album
    }
    return album_contents

active = True
while active:
    input_name = input("What is the artist's name?\n" +
    "(type quit to exit)")

    if input_name == 'quit':
        active = False
        continue

    input_album = input("What is " + input_name + "'s album called?\n" +
    "(type quit to exit)")

    if input_album == 'quit':
        active = False
        continue

    new_album = make_album(input_name, input_album)
    print(new_album)
