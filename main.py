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


async def delete_emojis():
  # :a: :b: の様に削除予定のemojiの名前が羅列したメッセージを取得
  message = await channel.fetch_message(MESSAGE_ID)
  for x in message.content.split(" "):
    try:
      emoji_id = int(x.split(":")[2][:-1]))
      emoji = guild.get_emoji(emoji_id)
      await emoji.delete(reason="第n回 絵文字大整理大会")
    except ValueError:
      print(f"intにできなかった：{emoji_id}")
    except discord.HTTPException:
      print(f"消せなかったお：{emoji_id}")
    except:
      print(f"不明なエラーだお：{emoji_id}")

  await channel.send("指定された絵文字を削除しました")


# 削除予定の絵文字を出力する
async def send_will_delete_emojis():
  will_not_delete = []
  async for message in channel.history(limit=None):
    # ここまでメッセージを読み込む
    # 説明文のメッセージとかで切ってもろて
    if message.id == MESSAGE_ID:
      break

    text = message.content.split(":")
    # ここでは絵文字のnameを取得したいので、IDとかは除外
    if len(text) >= 16 or "<" in text or ">" in text:
      continue

    will_not_delete += text

  # 削除する：True
  # 削除しない：False
  emoji_dict = {}
  will_delete = []

  for emoji in guild.emojis:
    if emoji.name in will_not_delete:
      emoji_dict[emoji.name] = False
    else:
      emoji_dict[emoji.name] = True
      will_delete.append(emoji)

  # 削除予定の絵文字を送信する
  body = " ".join(will_delete)
  await channel.send(body)



# ログいっぱいだとウザいのでWARNING以上にしてます。
bot.run(TOKEN)