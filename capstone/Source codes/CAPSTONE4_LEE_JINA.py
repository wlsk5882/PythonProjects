'''
author                    : Jina Lee
original creation date    : Dec. 9, 2015
last modification date    : 

Capstone Project Activity #4
Produce an listing of tokens / concepts and output them to the monitor in ascending order. 
You must you an additional external library of your choosing to complete this activity.


Submit your source code [filename = CAPSTONEA4_LASTNAME_FIRSTNAME.py]
and external text files through Blackboard.


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
    
    #removing puntuation: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    #using punctuation list from string library
    nopunct = [w for w in text if w not in string.punctuation] #print(string.punctuation)
    withoutPunctuation = ''.join(nopunct) ;print(withoutPunctuation)
    
    # remove stopwords
    my_stops = stopwords.words('english')
    print(my_stops)
    #my_stops.append("\n")
    normalized = [w for w in withoutPunctuation.split() if w.lower() not in my_stops]
    
    
    norm_text = ' '.join(normalized)

    print(norm_text)


main()