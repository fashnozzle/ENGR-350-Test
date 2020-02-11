#Name: Joe Rebaza
#Program: Decrypt Cipher
#Date: 2/7/2020
import re
dList ):               
    message = ""                        #local variable holding plainText message
    shift = 10                          #shift value to decrypt message

    #for loop that goes through each char in the message
    for char in wordList:
        #if the char in the message matches with the ALPHABET dictionary
        if char in ALPHABET or char.isupper():
            #goes through if condition when the letter is uppercased
            if char.isupper():
                #finds the char in the ALPHABET and shifts it +10 with modulo 26 in case if passes 26
                character = ALPHABET[(ALPHABET.index(char.lower()) + shift) % 26]
                #returns char to uppercase
                character = character.upper()
            #if letter is not uppercased
            else:
                 #finds the char in the ALPHABET and shifts it +10 with modulo 26 in case if passes 26
                character = ALPHABET[(ALPHABET.index(char) + shift) % 26]
        #if char is not a letter
        else:
            #if char is not a letter it just adds it to the message without shifting
            character = char
        #character adds onto the plainText message
        message += character
    #returns finished message
    return message

#cipheredText
cipherWord = """Y adem iecu ev oek mekbt vehwuj je seccudj oekh setu, ie jxyi yi q hucydtuh je we rqsa
qdt seccudj uluho iydwbu bydu ed oekh setu. Oek ixekbt ru qrbu je unfbqyd uluho
iydwbu bydu ev setu, iydsu oek muhu jxu edu mxe mheju jxyi setu. Y xefu oek tytd'j jho
jhqdibqjydw jxyi ro xqdt vyhij, iydsu yj mekbt fherqrbo jqau oek q sekfbu xekhi. Jxyi yi
mxqj secfkjuhi qhu veh qdt oek ixekbt jqau qtlqdjqwu ev jxuc.Yv oek tyt jxyi ro xqdt, oek
ixekbt husediytuh huteydw yj ruskqiu teydw yj yd ro xqdt yi yduvvysyudjqdt jxqj'i mxo
jxyi junj yi ie bedw. Qbie, jxyi qiiywcudj sqbbi veh q icqbb fojxed fhewhqc. Edu mqo ev
ieblydw jxyi yi kiydw ijhydw.cqaujhqdi() qdt mxybu yj yi huseccudtut; yj yi dej
dusuiiqhybo jxu edbo efjyed oek xqlu. Yv oek tyt kiut cqaujhqdi(), fbuqiu unfbqyd je cu
xem yj mehai qdt Y qc ikhu oek xqt je kiu .jhqdibqju qi mubb, ie unfbqyd xem jxqj mehai
qi mubb. Edu bqij jxydw, unfbqyd xem oek qssekdjut veh ifusyqb sxqhqsjuhi? iksx qi ',.
()?:) [ifqsui], ujs' . Y Xefu oek xqt vkd mehaydw jxyi ekj :)."""

#string variable that calls decrypt method with cipherWord passing through: decrypt(cipherWord)
plainText = decrypt(cipherWord)
#prints plainText
print(plainText)
