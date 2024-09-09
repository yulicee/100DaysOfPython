from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Function to click the main cookie repeatedly
def click_cookie(driver, cookie_id, clicks=50):
    cookie = driver.find_element(By.ID, cookie_id)
    for _ in range(clicks):
        cookie.click()

# Function to buy buildings based on available cookies
def buy_building(driver, building_id):
    try:
        building = driver.find_element(By.ID, building_id)
        building.click()
    except:
        pass

# Function to buy upgrades
def buy_upgrade(driver):
    try:
        upgrades = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
        if upgrades:
            upgrades[0].click()  # Buy the first available upgrade
    except:
        pass

# Function to click golden cookies if available
def click_golden_cookie(driver):
    try:
        golden_cookie = driver.find_element(By.CLASS_NAME, 'shimmer')
        golden_cookie.click()
    except:
        pass

# Function to check if a Frenzy is active
def is_frenzy_active(driver):
    try:
        buffs = driver.find_elements(By.ID, 'buffs')
        if buffs:
            frenzy = driver.find_elements(By.CLASS_NAME, 'frenzy')
            return len(frenzy) > 0
        return False
    except:
        return False

# Initialize Selenium WebDriver
driver = webdriver.Chrome()

# Open Cookie Clicker in the browser
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for the game to load
time.sleep(5)

# Select English (change if needed)
driver.find_element(By.ID, "langSelect-EN").click()

# Wait for the game interface to fully load
time.sleep(10)

# IDs for buildings (these can vary depending on game progression)
building_ids = [
    "product0",  # Cursor
    "product1",  # Grandma
    "product2",  # Farm
    "product3",  # Mine
    "product4",  # Factory
    "product5",  # Bank
    "product6",  # Temple
    "product7",  # Wizard Tower
    "product8",  # Shipment
    "product9",  # Alchemy Lab
    "product10", # Portal 
    "product11", # Time Machine
    "product12", # Antimatter Condenser
    "product13", # Prism
    "product14", # Chancemaker
    "product15", # Fractal Engine
    "product16", # Javascript Console
    "product17", # Idleverse
    "product18",
    # Add more buildings as needed
]

# Main game loop
try:
    while True:
        # Check if Frenzy is active
        if is_frenzy_active(driver):
            # Click faster during Frenzy
            click_cookie(driver, "bigCookie", clicks=200)
        else:
            # Regular clicking
            click_cookie(driver, "bigCookie", clicks=50)

        # Buy any upgrades available
        buy_upgrade(driver)

        # Buy buildings based on available cookies
        for building_id in building_ids:
            buy_building(driver, building_id)

        # Check for and click any golden cookies
        click_golden_cookie(driver)

        # Short delay between each cycle to not overload the game
        time.sleep(1)

except KeyboardInterrupt:
    print("Bot stopped.")

finally:
    # Close the browser after the game ends
    driver.quit()
