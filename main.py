import os
import discord
from discord.ext import commands
from discord import app_commands



intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
TOKEN = YOR_UNIQUE_TOKEN


guild = bot.get_guild(GUILD_ID)
# 第n会 絵文字削除大会の管理チャンネルid
channel = guild.get_channel(CHANNEL_ID)


@bot.event
async def on_ready():
  custom_activity = discord.Game(f"ゲームバーのメッセージを記入")
  await bot.change_presence(status=discord.Status.online,activity=custom_activity)

  print(f"login as {bot.user.mention}")


async def delete_emojis()
  # :a: :b: の様に削除予定のemojiの名前が羅列したメッセージを取得
  message = await channel.fetch_message(MESSAGE_ID)
  text_l = []
  for x in message.content.split(" "):
    text_l.append(x.split(":")[2][:-1])
  print(text_l)

  for x in text_l:
    emoji = guild.get_emoji(int(x))
    await emoji.delete(reason="第n回 絵文字大整理大会")
  await channel.send("削除しました")

  return

# 削除予定の絵文字を出力する
async def send_will_delete_emojis(message)
  msg = []
  async for message in channel.history(limit=None):
    # ここまでメッセージを読み込む
    # 説明文のメッセージとかで切ってもろて
    if message.id == 1229331189987409940:
      break
    msg += message.content.split(":")

  for x in msg:
    if len(x) >= 16:
      msg.remove(x)
  for x in msg:
    if "<" in x:
      msg.remove(x)
  for x in msg:
    if ">" in x:
      msg.remove(x)

  emoji_name_l = [x.name for x in guild.emojis]
  emoji_dict = {}
  for x in emoji_name_l:
    emoji_dict[x] = False

  for x in msg:
    try:
      emoji_dict[x] = True
    except KeyError:
      print(x)

# 消さない：True
  send_msg = []
  for x in emoji_dict:
    if not emoji_dict[x]:
      send_msg.append(f":{x}:")
  print(len(send_msg))
  body = " ".join(send_msg)
  # 削除予定の絵文字を送信する
  await channel.send(body)


# ログいっぱいだとウザいのでWARNING以上にしてます。
bot.run(TOKEN)