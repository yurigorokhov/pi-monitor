from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import json

@respond_to('picture', re.IGNORECASE)
def picture(message):

    #TODO: take a picture!
    message.reply('Taking a picture, I hope Brewski is smiling ...')
    attachments = [{
        'fallback': 'Fallback text',
        'author_name': 'RaspberryPi',
        'author_link': 'https://www.adafruit.com/includes/templates/adafruit2013/images/little_pi.png',
        'image_url': 'https://www.adafruit.com/includes/templates/adafruit2013/images/little_pi.png',
        'text': 'Brewski!',
        'color': '#59afe1'
    }]
    message.send_webapi('', json.dumps(attachments))

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')

    # react with thumb up emoji
    message.react('+1')

# Fun
@respond_to('I love you')
def love(message):
    message.reply('I love you too!')

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
