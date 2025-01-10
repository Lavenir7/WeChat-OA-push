# WeChat-OA-push

Use python script to push some informations (maybe set to a schedule) by WeChat Official Account.

## install requirements
```sh
pip install requests html5lib bs4 schedule feedparser
```

## add secrets
```sh
vim template_secrets.json
# add your secrets
mv template_secrets.json secrets.json
```

## run
```sh
python main.py # push immediately
```
```sh
python main_clock.py & # push on time
```

