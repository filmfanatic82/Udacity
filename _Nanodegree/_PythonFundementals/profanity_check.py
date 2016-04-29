#read text from doc

import urllib

def read_text():
    quotes = open("/Users/jesshd/Desktop/test.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
#check text for curse words

def check_profanity(text_to_check):
    urllib.urlopen ("http://www.wdylike.appspot.com/?q=shot"+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif

read_text()
