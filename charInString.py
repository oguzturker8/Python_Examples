def FindString(text,ch):
    count = 0
    for i in text:
        if i == ch:
            count += 1
    return 'Metinde %s %d defa gecmistir' % (ch,count)
while 1:
    print(FindString(input("Metni giriniz : "),input("Aranacak karakteri giriniz : ")))
    
