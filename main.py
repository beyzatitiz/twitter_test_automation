from twitter_project import TwitterProject

twitter = TwitterProject("TOtomasyonu", "Test.otomasyonu123", "#deprem")

twitter.login_with_twitter()
twitter.search_by_a_hashtag()
twitter.get_tweets()
twitter.save_to_file()

