# SimplePythonLineBot
Simple Python Line Bot Code

想說就只是拿來自己用~~



```
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
# Channel Access Token 
line_bot_api = LineBotApi('')
# Channel Secret
handler = WebhookHandler('')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
# 目前只設計成 "呼叫機器人" 關鍵字，就會秀出發送訊息所需的 userId 與 groupId
    if "呼叫機器人" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(event.source)))
    else:
        pass


if __name__ == '__main__':
    app.run()



```
