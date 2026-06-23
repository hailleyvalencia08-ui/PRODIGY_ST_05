from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize driver (Chrome example)
driver = webdriver.Chrome()

# Open demo site
driver.get("https://shoplane-by-lassie.netlify.app/")
driver.maximize_window()

# Step 1: Add item to cart
driver.find_element(By.XPATH, "(//button[text()='Add to Cart'])[1]").click()
time.sleep(2)

# Step 2: Go to cart
driver.find_element(By.ID, "cart").click()
time.sleep(2)

# Step 3: Proceed to checkout
driver.find_element(By.ID, "checkout").click()
time.sleep(2)

# Step 4: Fill checkout form
driver.find_element(By.ID, "name").send_keys("Test User")
driver.find_element(By.ID, "email").send_keys("test@example.com")
driver.find_element(By.ID, "address").send_keys("123 Test Street")
driver.find_element(By.ID, "payment").send_keys("4111111111111111")

# Step 5: Submit form
driver.find_element(By.ID, "submit").click()
time.sleep(3)

# Step 6: Verify success message
success_message = driver.find_element(By.ID, "success").text
assert "Thank you for your purchase" in success_message

print("Checkout flow automated successfully!")

driver.quit()
