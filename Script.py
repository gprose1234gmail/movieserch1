class script(object):
    START_TXT = """Hello {} π¨βπ»,
My Name is <a href='https://t.me/THEMOVIEFILESPROBOT'>ππππΌ πππππ ππππππΏππ</a>
I Can Provide Movies In Telegram Groups. You Can Search Movies Via Inline. I Can Also Add Filters In Telegram Groups.
Just Add Me To Your Group And Enjoy Of All Available Movies On TG.
Made With β€ BY @lunasupportz"""
    HELP_TXT = """Hell'O {}
Here is the Help For My Bot Commands."""
    ABOUT_TXT = """β My Name: [πΌππΌπ ππΌππππ](https://t.me/alpha_romeo_06)
β Developer: @lunasupportz
β Library: Pyrogram
β Language: Python 3
β DataBase: Mongo DB
β Bot Server: Heroku
β Build Status: v1.0.1 [Beta]
β Updates:<a href='https://t.me/lunasupportz'>@lunasupportz</a>
β Support: <a href='https://t.me/+gpX3sKd29WJjMmY9'> @lunasupportz</π>
β BotsList" : <a href='https://t.me/lunasupportz'> @lunasupportz</π>"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://t.me/lunasupportz

<b>DEVS:</b>
- <a href=https://t.me/lunasupportz>Team luna </a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. luna file search should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- luna Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.


<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of luna file search

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specifed user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """βͺ Total Medias: <code>{}</code>
βͺ Total Users: <code>{}</code>
βͺ Total Chats: <code>{}</code>
βͺ Used Storage: <code>{}</code> πΌππ±
βͺ Free Storage: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
