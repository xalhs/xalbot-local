# xalbot

A twitch bot that supports various interactions on a twitch channel.

## Features


- command-response support
- Text to speech (both as a command and as a channel point reward)
- twitch channel point integration;   
   once configured, it can read channel point redemptions and do various commands like the text to speech mentioned above
- points feature   
   Can give viewers points automatically   
   Points can be given (with the !give command) or gambled (with the !Roulette command)    
- changing title/game
- math (can do many different math operations)
- showing follow age (how long a user has been following another user)
- 8ball command
- shoutout command
- uptime (how long user has been live for)
- urban command (fetches the top response from urban dictionary for said object and sends it in chat)
- wiki command (fetches wikipedia reponse for said object and sends it in chat)



## How to run
To run you need a twitch account to run as your "bot" this can be either your main or your second account.
Once you have chosen which account you want as a bot, go to Settings.py in the modules folder and start completing the empty fields

for the PASS field go to https://twitchapps.com/tmi/ and connect your bot account, then take the token and set the OAUTH's value as a string

in the IDENT field add your bot's twitch name

in the CHANNEL field just add the channel you want the bot to run on

for some functions you'll need a CLIENT_ID so for that field you have to create a twitch application more info here https://dev.twitch.tv/docs/v5

for the OAUTH field you need to follow the procedure at https://dev.twitch.tv/docs/authentication , so far, the scopes needed for the bot functions are user:edit:broadcast and clips:edit, make sure if you request an access token through this to have these 2 scopes. If you have any questions about this step feel free to message me. In the future I'll make a more detailed guide

if you want song requests with channel points complete the NIGHTBOT_AUTH field as well, otherwise skip it. For this field you'll need a nightbot access token, to get one follow the instructions here https://api-docs.nightbot.tv/#oauth-2

If you did the previous instructions correctly the bot should run after you run `Run.py`.

TO BE ADDED, GUIDE FOR:
- twitch channel points integration
- playsounds
- special playsounds
- commands
- "pastas"







## DISCLAIMER

This bot is part of a personal project I did to practice my knowledge of python. This isn't meant for widespread use, however if you are interested in running the code, feel free to ask me any questions.
