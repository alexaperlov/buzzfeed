#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:57:31 2018
BuzzFeed - find articles based on user input
@author: alexa.perlov
"""
import requests
import webbrowser

def search(source, q, publishedAt):
    printing = False
    if(source != 'null' and q != 'null' and publishedAt != 'null'):
        url = ('https://newsapi.org/v2/top-headlines?'
               'sources=' + delete_space(source) + '&'
               'q=' + add_and(q) +'&'
               'publishedAt='+publishedAt+'&'
               'sortBy=popularity&'
               'apiKey=9f52b5e69ee54b9591389a382577ddaa')
    elif(source == 'null' and q != 'null' and publishedAt == 'null'):  
        url = ('https://newsapi.org/v2/top-headlines?'
               'q=' + add_and(q) +'&'
               'sortBy=popularity&'
               'apiKey=9f52b5e69ee54b9591389a382577ddaa')
    elif(source != 'null' and q == 'null' and publishedAt == 'null'):
        url = ('https://newsapi.org/v2/top-headlines?'
               'sources=' + delete_space(source) + '&'
               'sortBy=popularity&'
               'apiKey=9f52b5e69ee54b9591389a382577ddaa')
    elif(source == 'null' and q != 'null' and publishedAt != 'null'):  
        url = ('https://newsapi.org/v2/top-headlines?'
               'q=' + add_and(q) +'&'
               'publishedAt='+publishedAt+'&'
               'sortBy=popularity&'
               'apiKey=9f52b5e69ee54b9591389a382577ddaa')
    elif(source != 'null' and q == 'null' and publishedAt != 'null'):
        url = ('https://newsapi.org/v2/top-headlines?'
               'sources=' + delete_space(source) + '&'
               'publishedAt='+publishedAt+'&'
               'sortBy=popularity&'
               'apiKey=9f52b5e69ee54b9591389a382577ddaa')
    elif(source != 'null' and q != 'null' and publishedAt == 'null'):  
        url = ('https://newsapi.org/v2/top-headlines?'
               'sources=' + delete_space(source) + '&'
               'q=' + add_and(q) +'&'
               'sortBy=popularity&'
               'apiKey=9f52b5e69ee54b9591389a382577ddaa')
    elif(source == 'null' and q == 'null' and publishedAt != 'null'):  
        url = ('https://newsapi.org/v2/top-headlines?'
               'publishedAt='+publishedAt+'&'
               'country=us&'
               'sortBy=popularity&'
               'apiKey=9f52b5e69ee54b9591389a382577ddaa')
    elif(source == 'null' and q == 'null' and publishedAt == 'null'):  
        url = ('https://newsapi.org/v2/top-headlines?'
               'country=us&'
               'sortBy=popularity&'
               'apiKey=9f52b5e69ee54b9591389a382577ddaa')
    
    response = requests.get(url)
    json = response.json()

    try:
        for i in json['articles']:
            #print out article titles and description that correspond w user input
            print(i['title'] + ': ' + i['description']) 
            printing = True
    except: 
        #error checking
        if(printing == False):
            print("No articles found for given inputs")
            main()
        else:
            pass
    
    read = input('Did you find an article to read? (Y/N)')
    
    if( read == 'Y'):
        article = input("enter the title of the article you want to read")
        
        for i in json['articles']:
            if i['title'] == article:
                webbrowser.open(i['url']) #send user to website of desired article
    else:
        main() #if the user hasn't found a desired article, start over
            

def main():
    print("What do you feel like reading today?")
    #get user input
    q = input('List some key words seperated by spaces (if not applicable, enter "null"): ')
    source = input('Do you have a desired news source (if not applicable, enter "null"): ')
    publishedAt = input('Is there a specific time period (if not applicable, enter "null"): (YYYY-MM-DD)')
    #pass user input into function to find articles
    search(source, q, publishedAt)


#insert dashes instead of spaces for url
def delete_space(word):
    returnword = ''
    for i in word:
        if i == ' ':
            returnword += '-'
        else:
            returnword += i
    return(returnword)

#insert & instead of spaces for lists
def add_and(word):
    returnword = ''
    for i in word:
        if i == ' ':
            returnword += '&'
        else:
            returnword += i
    return(returnword)

            
if __name__ == "__main__":
    main()