from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from groq import Groq
from dotenv import load_dotenv
import re
import os
from selenium.common.exceptions import NoSuchElementException





load_dotenv()
client = Groq()



def ask_ai(question: str, options: list[str]) -> int:
    formatted = "\n".join(f"{i+1}. {o}" for i, o in enumerate(options))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": f"Question: {question}\nOptions:\n{formatted}\nReply with one of the options only numbering just number of that answer please"
        }]
    )

    saved = response.choices[0].message.content.strip().strip(",").strip(".")
    return int(saved)


    
print("Hello World")

web = webdriver.ChromeOptions()
web.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=web)

driver.get("https://ehub.alxafrica.com/login?_gl=1*1tllszm*_gcl_au*MjAyNTc0MDM5MS4xNzc4MjQ5Njk5*_ga*MTkwMjY0MTg3NS4xNzc4MjQ5NzQx*_ga_Y49H7D9C6F*czE3NzgyNDk3NDAkbzEkZzAkdDE3NzgyNDk3NDAkajYwJGwwJGgw*_ga_GKTJ66LE10*czE3NzgyNDk3NDAkbzEkZzAkdDE3NzgyNDk3NDAkajYwJGwwJGgw")

driver.maximize_window()
driver.implicitly_wait(30)
e = driver.find_element(By.XPATH, '//*[@id=":r0:-form-item"]')
p= driver.find_element(By.XPATH, '//*[@id=":r1:-form-item"]')


e.send_keys(os.getenv(key="email"))
p.send_keys(os.getenv(key="password"))

login = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div/div[5]/form/button')
login.click()


driver.implicitly_wait(30)
continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div[3]/div[3]/div[2]/div/button')
continue_button.click()


time.sleep(30)

counter = 154


test = [155,156,159]
test2 = [153]

for i in test:
    driver.switch_to.new_window('tab')
    driver.get(f"https://savanna.alxafrica.com/evaluation_quizzes/{i}")
    # driver.get("https://savanna.alxafrica.com/evaluation_quizzes/159")
    try:
        start_button = driver.find_element(By.XPATH, '//*[@id="curriculum_navigation_content"]/div[1]/div/div/div/div[3]/div[2]/div/button')
        start_button.click()
    except NoSuchElementException:
        print("No such start button")

    while True:
        try:
            element = driver.find_element(By.TAG_NAME, "h3")
            if element.text.strip() == "Overview":
                print("Found Overview")
                break
        except NoSuchElementException:
            print("No h3 tag found on this page")
        time.sleep(3)
        print("Here")
        question = driver.find_element(By.XPATH, '//*[@id="curriculum_navigation_content"]/div[1]/div/div/div/div[3]/div/div/h2').text

        options = driver.find_elements(By.CSS_SELECTOR, '.hstack p')
        option_answers = [option.text for option in options]
        answer = ask_ai(question, option_answers)
        # clean_answer = re.sub(r'^\d+\.\s*', '', answer).strip()
        print(answer)
        print(option_answers[answer-1])
        answer_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'button[aria-label*="{option_answers[answer-1]}"]')))
        # answer_button = driver.find_element(By.CSS_SELECTOR, f'button[aria-label*="{clean_answer}"]')

        # answer_button.click()
        driver.execute_script("arguments[0].click();", answer_button)

        submit_button = driver.find_element(By.XPATH, '//*[@id="curriculum_navigation_content"]/div[1]/div/div/div/div[3]/div/form/div[2]/div[2]/button')
        driver.execute_script("arguments[0].click();", submit_button)

