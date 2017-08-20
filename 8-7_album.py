def make_album(name, album):
    albums = {'name': name,
              'album': album}
    return albums

musician = make_album('Jimi Hedrix', 'Are You Experienced?')
musician = musician + make_album("Guns 'n Roses", "Appetite for Destruction")
#musician = make_album("Explosions in the Sky", "The Earth is not a Cold Dead Place")
print(musician)
