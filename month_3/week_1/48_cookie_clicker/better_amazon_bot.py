from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.de/Instant-Pot-113-0061-01-EU-Stainless-Silver/dp/B0979K4RQN/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1DBHCS3DNJ6DA&dib=eyJ2IjoiMSJ9.0v-J73Q_5KsnThybXdAc0nN9zVUESTl_Wcot1lxeutQ9AuP3HLtYgLOZvlokoWehZP7GRVvM7ecMIUCDYZM86CgHhyfPAEy9qpCQymaedk-efy3RVtekS34hZYu82MeUEPYVAttE9iGEhC2gcjLnAJ7AEPw0fyLhExHlpBsDJBx_t0hblynbWQZnuXUZPwCk4D_dLvxz8tQlSO3FaOZcq6dy4YcACaljQRI96I9LlMM.kMuA9y-vNv9MZ9s9RZBzoRpM1U6wxNfQ84T4gdDtw1U&dib_tag=se&sprefix=instant+pot%2Caps%2C135&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

# driver.close()
driver.quit()