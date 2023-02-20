
phrase = str(input("Entrer une phrase\n"))

text=""

for i in range(len(phrase)):
    if phrase[i-1]==' ' and phrase[i]==' ':
        continue
    else:
        text+=phrase[i]
print(text)



