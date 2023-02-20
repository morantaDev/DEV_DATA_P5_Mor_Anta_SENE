dict={'00':' ','1':'b','2':'a','22':'b','222':'c','3':'d','33':'e','333':'f','4':'g','44':'h','444':'i','5':'j','55':'k','555':'l','6':'m','66':'n','666':'o','7':'p','77':'q','777':'r','7777':'s','8':'t','88':'u','888':'v','9':'w','99':'x','999':'y','9999':'z'}
crypted=""
def transformer_en_miniscule(string):
    Maj=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    tmp=0
    for i in range(len(string)):
        if string[i] in Maj:
            tmp=ord(string[i])
            tmp=tmp+32
            tmp=chr(tmp)
            string = string[:i] + tmp + string[i+1:]
    return string
chaine=str(input("Entrer un mot ou une phrase\n")) 
minis=(transformer_en_miniscule(chaine))
print("\n"+minis+"\n")
for i in minis:
    if i in ['.',',',';',':','?','!',"'"]:
        crypted+=i
    else:
        for key, value in dict.items():
            if i==value:
                crypted+=key
            elif i==key:
                crypted+=value
            else:
                pass

print(crypted)















#def Chaine():    
    #text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus quibusdam odio laudantium ad delectus. Delectus culpa doloribus quis saepe similique placeat autem, temporibus perferendis. Rem non dolores nesciunt consequatur nostrum." 
    #text="J'ai 17,5 en algo."
    #return text