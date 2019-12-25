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
line_bot_api = LineBotApi(
    'LM+HNOmvCDGyG0YMpHJa6L3nGDpLsvKQvTMYXeSB5aWO57VsgSQow8G+ZG1LKx/C/zW7qV6EJf2gYrLLIckTXLKXEhR/K6vr4n91PpMVTM702cEWIVrGZMy3uRjLWoE3LiVEQaP/CUPnlxmq8SUeHQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('b8e0d1ad6910bf350e6fb78fab3bc622')


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
    if "呼叫機器人" in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(event.source)))
    else:
        pass


if __name__ == '__main__':
    app.run()
