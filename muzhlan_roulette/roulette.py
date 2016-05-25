import random
import os
import yaml
from flask import Flask, render_template
from steamapi import core, user


app = Flask("Muzhlan Roulette")
# read and update config
conf_file_location = os.path.abspath(os.path.join(os.path.dirname(__file__), "../resources/roulette.yml"))
with open(conf_file_location) as conf_file:
    config = yaml.safe_load(conf_file)
app.config.update(config)

# supply steam web api key
core.APIConnection(api_key=app.config.get('steam_api_key'))


@app.route('/')
def roulette(player_tag=app.config.get('player_tag')):
    try:
        steam_user = user.SteamUser(userurl=player_tag)
        content = "You have {0} games. Random game: {1}".format(len(steam_user.games), random.choice(steam_user.games))
        img = steam_user.avatar_medium
        return render_template('hello.html', name=steam_user.name, content=content, img=img)
    except Exception as error:
        app.log_exception(error)
        # we might not have permission to the user's friends list or games, so just carry on with a blank message
        return render_template('hello.html', name=player_tag)


def main():
    app.run()

if __name__ == '__main__':
    main()
