import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA0Mzk2ODUxMjQ2NjYyMDQ3Nw.Gct7K_.NyviSQLV6cfCSf1C3Asdxf59ItnBy9I-8QOdwA')