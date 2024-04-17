# delete_emojis
鯖の絵文字削除大会に使うコード

# 使い方
個人用ですが一応()

1. 鯖に「削除して欲しくない絵文字」を送信するチャンネルを作成
2. 関数send_will_delete_emojisを実行する
 - guild.emojisを利用して、1で作成したチャンネルに送信されていない絵文字を取得し、送信する
3. 手順2で送信されたmessage.idを入力し、関数delete_emojisを実行