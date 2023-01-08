def module():
    code = context['code']
    target_lang = context.get('target_lang', 'Ruby')
    python_to_other_lang_command = """以下に書かれているコードはPythonのコードです。{target_lang}のコードに変換してください。\n自然言語などでの説明は不要なので、コードだけを出力してください。\n\n{code}"""
    req = python_to_other_lang_command.format(target_lang=target_lang, code=code)
    requests.append(req)
    res = chatbot.ask(req, conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)

    response = res['message']
    # response = req
    return response

responses.append(module())
