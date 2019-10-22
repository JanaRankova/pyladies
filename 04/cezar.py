plaintext = input('Zadajte vetu, ktoru chcete prelozit:  ')
key = int(input('Zadajte kluc, ktorym chcete spravu sifrovat:  '))


text = ''


for znak in plaintext:
    if znak.isupper():
        text = text + chr((ord(znak) + key - 65) % 26 + 65)     
    elif znak.islower():
        text = text + chr((ord(znak) + key - 97) % 26 + 97)     
    else:
        text = text + znak


print('Povodny text: ', plaintext)
print('Sifrovany text: ', text)