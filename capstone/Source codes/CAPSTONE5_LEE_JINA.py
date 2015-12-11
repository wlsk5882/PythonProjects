'''
author                    : Jina Lee
original creation date    : Dec. 9, 2015
last modification date    : 

Capstone Project Activity #5
Produce an listing of tokens / concepts along with their frequency and
 output them to the monitor in frequency ascending order.

You must you an additional external library of your choosing to complete this activity.
You need to provide comments in your program. You should have a comment block at the start of your code that identifies yourself, original creation date, last modification date, and gives a description of the program. You will need to provide comments for each procedure and variable. Comments will be a part of each activity grade.

Submit your source code [filename = CAPSTONEA5_LASTNAME_FIRSTNAME.py] and your external text files through Blackboard.  You may resubmit as many times as you like up to, the due date/time.  All work must be submitted via Blackboard.

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