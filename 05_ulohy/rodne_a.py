rodne_cislo = input('Zadajte svoje rodne cislo vo formate xxxxxx/xxxx:  ')

if (rodne_cislo[6] == '/' and rodne_cislo[0:6].isdigit() and rodne_cislo[7:11].isdigit() and len(rodne_cislo) == 11):
    rc_format = True
else:
    rc_format = False
print(rc_format)
