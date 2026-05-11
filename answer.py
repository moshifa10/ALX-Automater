from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

def ask_ai(question: str, options: list[str]) -> str:
    formatted = "\n".join(f"{i+1}. {o}" for i, o in enumerate(options))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": f"Question: {question}\nOptions:\n{formatted}\nReply with ONLY the answer text."
        }]
    )
    return response.choices[0].message.content.strip()


    
print("Hello World")
email_njabs = "moshifanjabulo@gmail.com"
passwor_njabs = "UJ4$CH?628veh_y"

email_kay = "Mahlarekarabo.702@gmail.com"
pass_kay = "CS@xN6DcGMF_MZJ"

web = webdriver.ChromeOptions()
web.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=web)

driver.get("https://ehub.alxafrica.com/login?_gl=1*1tllszm*_gcl_au*MjAyNTc0MDM5MS4xNzc4MjQ5Njk5*_ga*MTkwMjY0MTg3NS4xNzc4MjQ5NzQx*_ga_Y49H7D9C6F*czE3NzgyNDk3NDAkbzEkZzAkdDE3NzgyNDk3NDAkajYwJGwwJGgw*_ga_GKTJ66LE10*czE3NzgyNDk3NDAkbzEkZzAkdDE3NzgyNDk3NDAkajYwJGwwJGgw")

driver.maximize_window()
driver.implicitly_wait(30)
e = driver.find_element(By.XPATH, '//*[@id=":r0:-form-item"]')
p= driver.find_element(By.XPATH, '//*[@id=":r1:-form-item"]')

e.send_keys(email_kay)
p.send_keys(pass_kay)

login = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div/div[5]/form/button')
login.click()


driver.implicitly_wait(30)
continue_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/div[3]/div[3]/div[2]/div/button')
continue_button.click()


time.sleep(30)
driver.switch_to.new_window('tab')

driver.get("https://savanna.alxafrica.com/evaluation_quizzes/151")

# start_button = driver.find_element(By.XPATH, '//*[@id="curriculum_navigation_content"]/div[1]/div/div/div/div[3]/div[2]/div/button')

# start_button.click()

while True:
    time.sleep(10)
    print("Here")
    question = driver.find_element(By.XPATH, '//*[@id="curriculum_navigation_content"]/div[1]/div/div/div/div[3]/div/div/h2').text

    options = driver.find_elements(By.CSS_SELECTOR, '.hstack p')
    option_answers = [option.text for option in options]
    answer = ask_ai(question, option_answers)

    print(answer)
    break


