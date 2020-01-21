import asyncio
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("온라인이에요!")

@client.event
async def on_message(message):
    if message.content  ==  '관리원 백화점정보':
        embed = discord.Embed(title="즐거운 아파트 백화점 입점 정보", color=0xff00)
        embed.add_field(name="마인문고", value="이슷님의 `마인문고`", inline=True)
        embed.add_field(name="H.A.dessert", value="주신아님의 `H.A.dessert`", inline=True)
        embed.add_field(name="스카이팀 전자아울렛", value="스카이팀님의 `스카이팀 전자아울렛`", inline=True)
        embed.add_field(name="썸띵데이베이커리", value="SomethingDay님의 `썸띵베이커리`", inline=True)
        embed.add_field(name="룰루랄라 키즈카페", value="SUUT님의 `룰루랄라 키즈카페`", inline=True)
        embed.add_field(name="아디닭스", value="HEALING님의 `아디닭스`", inline=True)
        embed.add_field(name="봇 가게", value="키키님의 `봇 가게`", inline=True)
        embed.add_field(name="지나이키", value="♥G999♥님의 `지나이키`", inline=True)
        embed.add_field(name="ART HOUSE", value="SYEONG님의 `ART HOUSE`", inline=True)
        embed.add_field(name="GUCHICKEN", value="RIDEE님의 `GUCHICKEN`", inline=True)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
    
    if message.content  ==  '관리사무소 호출':
        await message.channel.send("무엇을 도와드릴까요?")
    
    if message.content  ==  '관리원 상점정보 마인문고':
        embed = discord.Embed(title="백화점 상점 정보", color=0xff00)
        embed.add_field(name="마인문고 정보", value=":books:  마인문고 :books:\n\n:white_check_mark:  마인문고에서는 책이나 문구류를 구매하실 수 있습니다. (추후 보상 시스템 개발 예정)\n\n:white_check_mark:  마인문고에서는 책 정리 알바를 모집하고 있습니다. (추후 보상 시스템 개발 예정)", inline=True)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content  ==  '관리원 상점정보 H.A.dessert':
        embed = discord.Embed(title="백화점 상점 정보", color=0xff00)
        embed.add_field(name="H.A.dessert 정보", value="H.A.dessert 는 Happy Apart dessert의 약자이고 말 그대로 디저트카페입니다.\n파는 것은 음료류와 디저트류 등을 팝니다.", inline=True)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game("시범 운영중입니다.")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(f'{len(client.users)}명의 입주자분들이 즐거운 아파트에 거주하고 있어요!')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
client.loop.create_task(my_background_task())

access_token = voice.environ["BOT_TOKEN"]
client.run('access_token')