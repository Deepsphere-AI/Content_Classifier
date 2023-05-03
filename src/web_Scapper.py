import requests

def find_the_input(input_text:str):
    url = 'https://openai-openai-detector.hf.space/'
    text_input = input_text

    response = requests.get(url, params=text_input)
    string_dict = response.text
    dict_obj = eval(string_dict)
    human = round(dict_obj['real_probability']*100,2)
    GPT = round(dict_obj['fake_probability']*100,2)
    if human < GPT:
        return 'The given content is generated by GPT : '+ str(GPT) + ' %'
    else:
        return 'The given content is generated by Human : '+ str(human) + ' %'
    # return response.text

import requests
from bs4 import BeautifulSoup

def get_paragraphs(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the paragraph element(s) using BeautifulSoup
    paragraphs = soup.find_all('p')

    # Extract the text content of each paragraph element
    paragraph_texts = [p.text for p in paragraphs if len(p.text)>30] 
    
    return paragraph_texts
