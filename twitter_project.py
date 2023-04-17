from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


class TwitterProject:

    def __init__(self, user_name, user_password, hashtag_word):
        self.user_name = user_name
        self.user_password = user_password
        self.hashtag_word = hashtag_word
        self.driver = webdriver.Chrome()
        self.tweets = []

    def login_with_twitter(self):
        self.driver.get("https://twitter.com/?lang=tr")
        twitter_login_button = self.driver.find_element(By.XPATH,
                                                        '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a/div/span/span')
        twitter_login_button.click()
        time.sleep(5)
        name_input = self.driver.find_element(By.XPATH,
                                              '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        name_input.click()
        name_input.send_keys(self.user_name)
        continue_button = self.driver.find_element(By.XPATH,
                                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        continue_button.click()
        time.sleep(5)
        pasword_input = self.driver.find_element(By.XPATH,
                                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pasword_input.send_keys(self.user_password)
        login_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        login_button.click()
        time.sleep(15)

    def search_by_a_hashtag(self):
        search_input = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
        search_input.send_keys(self.hashtag_word)
        search_input.send_keys(Keys.RETURN)
        time.sleep(10)

    def get_tweets(self):
        for i in range(5):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            elements = self.driver.find_elements(By.XPATH, '//*[@data-testid="tweetText"]')

            for element in elements:
                self.tweets.append(element.text)

    def save_to_file(self):
        tweet_str = "\n".join(self.tweets)
        with open("tweets.txt", "w", encoding='utf-8') as file:
            file.write(tweet_str)

