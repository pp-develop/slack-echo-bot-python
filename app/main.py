import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# アプリを初期化します。botトークンと署名シークレットを使用
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.event("app_mention")
def handle_mention(event, say, client):
    channel_id = event['channel']
    thread_ts = event.get('thread_ts')  # スレッド内のメンションの場合はthread_tsが存在する

    # スレッド内でメンションされた場合
    if thread_ts:
        # 親スレッドのメッセージを取得
        result = client.conversations_replies(
            channel=channel_id,
            ts=thread_ts
        )

        if result['ok']:
            parent_message = result['messages'][0]['text']  # 親スレッドのメッセージ
            
            # TODO:: 親スレッドのメッセージを作成した関数に適宜投げる？
            say(text=f"親スレッドのメッセージ: {parent_message}", thread_ts=thread_ts)
    else:
        # スレッド外でメンションされた場合
        # TODO:: 送信されたテキストを作成した関数に適宜投げる？
        say(text=f"エコー: {event['text']}")

# 下記イベントの処理がないと不要なログが出るため
@app.event("message")
def handle_message_events(body, logger):
    pass

if __name__ == "__main__":
    # アプリを開始
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    handler.start()
