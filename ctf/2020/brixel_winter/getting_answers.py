import json 
import time
from urllib.parse import quote
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('http://timesink.be/quizbot/index.php')

def get_questions():
    time.sleep(2)
    questionName = "questions" + str(q)
    answerField = browser.find_element_by_id('insert_answer')
    question = browser.find_element_by_tag_name('h4').text
    d = {}
    d['question'] = question
    answerField.send_keys(Keys.ENTER)
    answer = browser.find_element_by_id('answer').text
    d['answer'] = answer
    return(questionName,d)
out = {}
q=0
while True:
    q+=1
    if(q==1001):
        break
    else:
        name, d = get_questions()
        out[name] = d
        
with open('questions.json','w') as f:
    json.dump(out, f, indent=2)