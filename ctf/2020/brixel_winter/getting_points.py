import json 
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('http://timesink.be/quizbot/index.php')
q=0

with open('questions.json') as json_file:
    data = json.load(json_file)
    while(q!=1001):
        time.sleep(1)
        q+=1
        answerField = browser.find_element_by_id('insert_answer')
        answer = data["questions" + str(q)]["answer"]
        answerField.send_keys(answer)
        answerField.send_keys(Keys.ENTER)


