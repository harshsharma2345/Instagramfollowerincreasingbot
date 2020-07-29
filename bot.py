from instapy import InstaPy
session = InstaPy(username='aesthetic_heros', password='agoodfriend', headless_browser=True)
session.login()
   
session.follow_by_tags(["sixpackabs", "bodybuilding","fitness", "weighttraining","nutrition","vegan","veganbodybuilding"], amount=10)
session.like_by_tags(["sixpackabs", "bodybuilding","fitness", "weighttraining","nutrition","vegan","veganbodybuilding"], amount=10)
session.set_comments(["Nice!", "amazing","keep it up"])
session.set_do_comment(True, percentage=100)
session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                              peak_likes_hourly=57,
                              peak_likes_daily=585,
                               peak_comments_hourly=21,
                               peak_comments_daily=182,
                                peak_follows_hourly=48,
                                peak_follows_daily=None,
                                 peak_server_calls_hourly=None,
                                  peak_server_calls_daily=4700)