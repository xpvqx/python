flera_ord = input('skriv ett par ord: ')
#dela upp strängen i en lista: seperera vid mellanslaget!
ordlista = flera_ord.split()
#itererar över orden i listan:
longest=''

for ett_ord in ordlista:
    if len(ett_ord) > len(longest):
        longest = ett_ord
print (longest)
