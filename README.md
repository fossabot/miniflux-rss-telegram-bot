## miniflux-rss-telegram-bot

![Docker Build Status](https://img.shields.io/docker/build/bluebird1/miniflux-rss-telegram-bot.svg)
![Docker Automated build](https://img.shields.io/docker/automated/bluebird1/miniflux-rss-telegram-bot.svg)


Telegram rss robot supported by miniflux

### Requirements
`python>3.4`
`miniflux`

### install
#### docker
edit .env file
`docker run --env-file=.env -d bluebird1/miniflux-rss-telegram-bot`
#### python
```
# pip -r requirements.txt
# export token <you bot token>
# export host <you miniflux host>
# export port <you miniflux por>
# export username <you miniflux admin username>
# export password <you miniflux admin password>
# python run.py
```

### use bot
```
/new_user  <username> <password> #create you account
/bind <username> <password> #bind you account
/discover <url> # try auto discover rss feed
/add_feel <feedurl> <category_id> # add feed
/export # export you feed
/get_entries  <num> # get rss
```

###  Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

