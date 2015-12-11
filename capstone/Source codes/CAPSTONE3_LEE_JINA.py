'''
author                    : Jina Lee
original creation date    : Dec. 9, 2015
last modification date    : 

Capstone Project Activity #3
1.) Print out CAPSTONEA2_LASTNAME_FIRSTNAME_FILE1.txt,
 and manually identify the noise and normalization you have to complete.  
Prior to completing step #1, you can use the NLTK library to create a small program 
to make a list of ngrams of size 3 that may help you find compound concepts
 (which you then print to a temporary file).  If you create this small program, please attach it to your submission as CAPSTONEA3extraCredit_LASTNAME_FIRSTNAME.py for extra credit.  If you choose not to do this step, you have to identify the compound concepts manually in step #1.

2.) Replace all noise, punctuation and whitespace, 
    and perform appropriate substitutions for stemming,
        creating compound concepts, and normalization.

You can use the NLTK library to help with this, but it will also involve some manual coding 
on your part.

3.) Output the new results to a second external text file:  CAPSTONEA3_LASTNAME_FIRSTNAME_FILE1.txt
You need to provide comments in your program. You should have a comment block at the start of your code that identifies yourself, original creation date, last modification date, and gives a description of the program. You will need to provide comments for each procedure and variable. Comments will be a part of each activity grade.

Submit your source code [filename = CAPSTONEA3_LASTNAME_FIRSTNAME.py] and external file [filename = CAPSTONEA3_LASTNAME_FIRSTNAME_FILE1.txt] through Blackboard.  Also submit your source code for the extra credit if you decided to do it [filename = CAPSTONEA3extraCredit_LASTNAME_FIRSTNAME.py]
'''

import requests
from bs4 import BeautifulSoup
import string
from nltk.corpus import stopwords

def main():
    ### 1) print 'CAPSTONEA2_LEE_JINA_FILE1.txt' file
    filename='CAPSTONEA2_LEE_JINA_FILE1.txt'
    with open(filename,'r') as f:
        text=f.read()
        print(text)

    #removing puntuation: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    mypuncts =  string.punctuation
    mypuncts+=('\n')
    nopunct = [w for w in text if w not in mypuncts] #print(string.punctuation)
    withoutPunctuation = ''.join(nopunct) ;print(withoutPunctuation)
    
    # remove stopwords
    my_stops = stopwords.words('english')
    print(my_stops)
    #my_stops.append("\n")
    normalized = [w for w in withoutPunctuation.split() if w.lower() not in my_stops]
    
    
    norm_text = ' '.join(normalized)

    print(norm_text)

    cleared_tokens=[]
    for token in norm_text.split():
        if (token.startswith('TA') | token.startswith('P2P')| token.startswith('USCERT')):
            cleared_tokens.append(token)
            print('1: ', token, cleared_tokens[len(cleared_tokens)-1])
        else:
            if (any(x.isupper() for x in token[1:len(token)-1])):
                print('2-1: ', token)
                uppers=[]
                for x in token:
                    uppers.append(x) if x.isupper()==True else ''
                    print(x, uppers)
                seperated=token.split(uppers[0])
                for element in seperated:
                    cleared_tokens.append(element)
                print('2-2: ', token, cleared_tokens[len(cleared_tokens)-1])
            else :
                cleared_tokens.append(token)
                print('3: ', token, cleared_tokens[len(cleared_tokens)-1])
                      
        
    print(cleared_tokens)
    result = ' '.join(cleared_tokens)
    
    outputFilename='CAPSTONEA3_LEE_JINA_FILE1.txt'
    with open(outputFilename,'w') as f:
        f.write(result)
        
        



main()