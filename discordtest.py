import discord
import datetime
import glob
import sqlite3
dbname = "URL.db"
game = ""
#test
client = discord.Client()
prefix = "!"
Mprefix = "/!"
filename = "commandhistory.txt"
recordfile = "recordURL.txt"


def ch(a,b,c):
    f=open(filename,"a",encoding="UTF-8")
    print(str(datetime.datetime.now())+"/"+a)
    f.write(str(datetime.datetime.now())+","+a+","+b+","+c+"\n")
    f.close

def recordURL(URL):
    f = open(recordfile,"a",encoding="UTF-8")
    f.write(URL+"")

def setdb(game,URL):
    try:
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        cur.execute("INSERT INTO URL VALUES('"+ game +"','"+ URL +"')")
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        message.channel.send(e)

def seturltemp(tempurl):
    dbname = "tempurl.db"
    game = tempurl[:4]
    temp = tempurl[4:]
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("INSERT INTO temp VALUES('"+ temp +"','"+ game +"')")
    conn.commit()
    cur.close()
    conn.close()


@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)


@client.event
async def on_message(message):
    text = str(message.content)
    author = str(message.author)
    channel = str(message.channel)


    if message.author.bot:
        return


    if Mprefix in text:
        await MasterCommands(message)

    if text == "now":
        await message.channel.send("実行中")
        ch(text,channel,author)



    if text == prefix + "time":
        ch(text,channel,author)
        await message.channel.send("https://docs.google.com/spreadsheets/d/14BdrFvGIqqMwhTn1EE-Ot1pMj9qZKk1FI0Kb2VUXuM8/edit#gid=0")



    if "https://" in text :
        try:
            recordURL(text)
            print("1")
            seturltemp(text)
            await message.channel.send(author)
            pass
        except Exception as e:
            await message.channel.send(e)
            raise
        ch(text,channel,author)






async def MasterCommands(message):


        text = str(message.content)
        author = str(message.author)
        channel = str(message.channel)
        if text == Mprefix + "commandstest":
            tempdbname = "test.db"
            conn = sqlite3.connect(tempdbname)
            cur = conn.cursor()
            ch(text,channel,author)
            cur.execute('SELECT * FROM test')
            co = cur.fetchall()
            for i in co:
                await message.channel.send(i)
            cur.close()
            conn.close()

        if text == Mprefix+"test":
            setdb("a","b")
            conn = sqlite3.connect(dbname)
            cur = conn.cursor()
            cur.execute('SELECT * FROM URL')
            co = cur.fetchall()
            cur.close()
            conn.close()

            ch(text,channel,author)


        if text == Mprefix+"checkdb":
            conn = sqlite3.connect(dbname)
            cur = conn.cursor()
            cur.execute('SELECT * FROM URL')
            co = cur.fetchall()
            cur.close()
            conn.close()
            for i in co:
                await message.channel.send(i)
            ch(text,channel,author)

key = "Token"
client.run(key)
