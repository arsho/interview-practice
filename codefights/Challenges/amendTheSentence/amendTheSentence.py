def amendTheSentence(s):
    sentence = ""
    for i,c in enumerate(s):
        if c.isupper():
            if i!=0:
                sentence+=" "+c.lower()
            else:
                sentence+=c.lower()                  
        else:
            sentence+=c            
    return sentence
