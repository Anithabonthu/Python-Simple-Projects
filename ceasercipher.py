alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(text,key):
    cipher=""
    for ch in text:
        if ch in alpha:
            pos=alpha.index(ch)
            new=(pos+key)%26
            cipher+=alpha[new]
        else:
            cipher+=ch
        
    print(cipher)
def decryption(text,key):
    plane=""
    for ch in text:
        if ch in alpha:
            pos=alpha.index(ch)
            pos1=(pos-key)
            if pos1<0:
                pos1=pos1+26
            new=pos1%26
            plane+=alpha[new]
        else:
            plane+=ch
        
    print(plane)
end=False
while not end:
    what_to_do=input("Enter encrypt for encryption and decrypt for decryption:")
    text=input("Enter the text:")
    text=text.lower()
    shift=int(input("enter shift key:"))
    if what_to_do=="encrypt":
        encryption(text,shift)
    elif what_to_do=="decrypt":
        decryption(text,shift)
    play_again=input("yes for play and no for quit")
    if play_again=="yes":
        end=False
    else:
        end=True
