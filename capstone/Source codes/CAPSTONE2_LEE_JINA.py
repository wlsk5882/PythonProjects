'''
author                    : Jina Lee
original creation date    : Dec. 9, 2015
last modification date    : 

Capstone Project Activity 2

1.) Cleanup your unstructured text by removing all web source code.
    I suggest using BeautifulSoup get_text() to do this, but it will also involve some manual coding on your part.
    
2.) Output the results to an external text file:  CAPSTONEA2_LASTNAME_FIRSTNAME_FILE1.txt

You need to provide comments in your program.
You should have a comment block at the start of your code that identifies yourself, original creation date, last modification date, and gives a description of the program. You will need to provide comments for each procedure and variable. Comments will be a part of each activity grade.

Submit your source code [filename = CAPSTONEA2_LASTNAME_FIRSTNAME.py] 
and  external file [filename = CAPSTONEA2_LASTNAME_FIRSTNAME_FILE1.txt]
 through Blackboard.  You may resubmit as many times as you like up to, the due date/time.  All work must be submitted via Blackboard.
Please keep in mind that you cannot skip activities.  You work at your own pace.


'''

import requests
from bs4 import BeautifulSoup



def main():
    # gets a response from web page, www.us-cert.gov/ncas/alerts
    url = r'https://www.us-cert.gov/ncas/alerts'
    
    r = requests.get(url)
    #print(r.headers)
    
    content = r.content
    
    soup = BeautifulSoup(content, 'html.parser')
    
    text_raw = soup.get_text()
    #print(text_raw)
    
    
    with open('text_raw.txt','w') as f:
        f.write(text_raw)
        #f.close()
    
    
    
    '''
    removing web source codes, which are appearing with strings
        1. between <!--//--> and //--><!]]>
        2. between <!--/*--> and /*--><!]]>*/
    '''
    
    removeDic={}
    removeDic[r'<!--//-->'] = r'//--><!]]>'
    removeDic[r'<!--/*-->'] = r'/*--><!]]>*/'
    
    
    text=removeThisRange(text_raw,removeDic)
    
    
    ### save text as txt file
    outputFile='CAPSTONEA2_LEE_JINA_FILE1.txt'
    with open(outputFile,'w') as f:
        f.write(text)
        print(outputFile,' has been created.')


# find index of each string representing begin and end of web-source code,
# then will remove all characters between start index and end index.
def removeThisRange(text,removeDic):
    # key: start string, value: end string
    for key, value in removeDic.items():
        while(text.find(key)!=-1):
            idx_start = text.index(key)
            idx_end = text.index(value)+len(value)
            # to debug the part to be removed
            #print('\n##############REMOVING: ',text[idx_start:idx_end])
            text = text[:idx_start-1]+'\n'+text[idx_end+1:]
    return text


main()