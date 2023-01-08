from flask import Flask, Response
from flask import request
from revChatGPT.ChatGPT import Chatbot
import os
import json
app = Flask(__name__)


class MockChatBot:
    def ask(self, message, conversation_id=None, parent_id=None):
        return {'message': f'わかりません。すみません。\n\n{message}' }


def create_chatbot():
    chatbot = Chatbot({
        "session_token": os.environ['CHATGPT_TOKEN']
    }, conversation_id=None, parent_id=None)
    return chatbot


chatbot = MockChatBot()
# chatbot = create_chatbot()

requests = []
responses = []
current_module = None

context = {}

@app.route("/messages", methods=['GET'])
def messages():
    print(request.args)
    if request.args.get('idx'):
        idx = int(request.args.get('idx'))
        print(f'Input[{idx}]:\n')
        print(requests[idx])
        print(f'Output[{idx}]:\n')
        print(responses[idx])
        data = {'input':requests[idx], 'output': responses[idx]}
        data = json.dumps(data, ensure_ascii=False)
        return Response(data, content_type="application/json; charset=utf-8")
    else:
        return '404'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.args:
        module = open(request.args['filename']).read()
        for k, v in request.args.items():
            context[k] = v
        print(f'Query[{len(responses)}] :>', context)

        print('\nCall Module:')
        print('-' * 30)
        print(module)

        exec(module)

        print(f'Input[{len(responses)-1}]:\n')
        print('-' * 30)
        print(requests[-1])

        print(f'Output[{len(responses)-1}]:\n')
        print('-' * 30)
        print(responses[-1])
        return '200'
    else:
        return '404'

if __name__ == "__main__":
    app.run(host='localhost', port='43560')
