song = """Got a doll, baby, I love her so
        Nothing else like her anywhere you go
        Man, she's anything but calm
        A regular pint sized atom bomb

        Atom bomb baby, little atom bomb
        I want her in my wigwam
        She's just the way I want her to be
        A million times hotter than TNT

        Atom bomb baby loaded with power
        Radioactive as a TV tower
        A nuclear fission in her soul
        Loves with electronic control
    """

def pick_char():
    """Ask for a char to search for."""
    char = input('Ktory znak by ste chceli vyhladat v piesni? ')
    return char

def modify(song):
    """Modifies all chars to lowercase and converts string into list."""
    song = song.lower()
    song_list = list(song)
    return song_list

def search_char(song_list, char):
    """Searches for char user asked for."""
    count = song_list.count(char)
    return count


song_list = modify(song)
char = pick_char()
print(search_char(song_list, char))
