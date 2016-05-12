
def word_process (a):
    cifer = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'}
    spisok=list()
    while a > 0:
        b = a % 10
        spisok.append (cifer[b])
        a = a / 10
    s = ""
    spisok.reverse()
    for i in range(len(spisok)):
        s+=str(spisok[i])+" "
    print s
word_process (146)