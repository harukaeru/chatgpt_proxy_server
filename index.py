from revChatGPT.ChatGPT import Chatbot
import sys

chatbot = Chatbot({
  "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..jmajrlpSYVxFFJwH.cuNJoy4Zm7nppqMEGgceZEzYp0mIyV3c8ogXt7KCZoOigPhvaZcD0WvLGnKv8jSLPeyRZdcpX8frpt19KTWg_UlnET-S0j3qaWtnL0keLJldbSDrqTyWbk-dTAV2TePveh0aDWIW1Tmi1Asi2ezoOUSjbioSUXdP6r_bQDcN-H6bPd0lY13p4ibHJmCFlCEMniy5TJ_Yw_O-026kEwZTSajbk5GGtvfGlejPi6Isl-82Y0jP1PDtLN67mr_YqAZogXhLCiuvrZy207VhV-NZAfl37ZdmUTlm6jYdUFlSnRhy-uZQIQ9_Z6eHMov8h8kVhljDM97OS_G7qOo2gaf7AuwZKOAImSPw6A_YI_D0-0dyqEjElfGNqT3dlzkIKk4vH60j_U1Z4pyR09h_fPKQJ6fSzbnnZtkLcyZ95MQhsR6wsLQG_q72nCUd9VaFz8BIpo5xb7nKe5JdQC2wR2YUHKiIoRYi1mZejd9ElT9okm5DUfdDxBiWgpIbXfjHvzkWJ9dT3F0Zo74TxLBUOEZt3odxlf9lrkTlpcjdSJxAhjSH_nQlYqFZOlrR_CIg3yqVPMq7xRg35zTFEm3YjiKuvkos4U--QDTxcEqd8wIrVJnqMZ-IpNNAGjDnf-HudJSPrnPVeiyWaxkhSrb6pFvM32c_VP-0hs8yhlO_hAptLEBo5PmaUXNknJGxsgjhTi_u5q9MOR0kEZgeMdmer8V0ccb_wmjSa-WdEBkxXbwuv5176u8sh8iwwM0pRh9VycCVoAISM5y615HCKLK-poQhKls4mB3jrx2jNu74ZOZ3pJEBc3KQHQTx8c2-7zy_3vU0_1E3vUWOUYO1dO0eCozdUM3feLYm8Oeskq92QJ0BTDNOIL0xI8haYu9UEfPoOg23gg3IGbyVI8339uOXOIQXOe0atqoQMG2XNh4lzCWIO6F7eQDDV8vA_87DbeWdUPC1rzF2vALAMaPheW_ByHjyy7yGMGr_9OugShN4pa-fkWe1CLPfqv_xKt7y-aJxX4uSfs__qWSIcn5TWnJRs8YGHgEHw_dvP-6sPZlZ8jMxK_BhzZj4L7SxnNqN0t2BQypvmGl-o5eevn8HZhjqpvXdWdqBzgrurEKmH8qowEz_ud8BsQfLLg0QS8EcqHl8wMgjRIS7h24I5tqXomAEw5qAoY4x7oRTdYTbOQ3ayQBnx_W_ru0g6yHdj6_ot3M_9vz7v7EnVD4rto-ypjyT-6SnHvIraWMNFO40Wi7bRDlOfGJWeO82zS3TWtyNwgKdNDmnmMaVO-UYWfBFr34z8uhE14sXwjUwpu7Z4OGOIT0Ai5ozwlvA0dq3t2yKscJXy5dnX-ej9SotkPcWeuSAKLJIXwK1np4kLAuzd8RZHrPBhzPCb6EpCKyl3uNXr_GbtTzYo33RrWeAWEyB4F-oXXapeNviz540MmWbHnOf8adwVPn_x4D0XwDuoRYpAWmXhkYh8oleQsiZC2QnKS3j0u-c-QCG0Udeccv9yZVgkWm1ZFVRWQp_OduGFY1dXTpT0_j5wsHdXOc4RC_LVkBDrfvX8esnjh0uwiCz0DX8_LBbqmbbl1KtFF-ZXANINcxrz1amUimg9ycZnaScUM5DzO2N1BDn71i7UUOZplo2CRqHmF7zkQ_5rY9DMpaV8CsE99PZBtbp4kd-Atdxv_nHOUck6CSUsx26vNWeOe1RQr2W4zXXPZ48EiBAku5KE87AfRXbQBIPHdkDLNRYjBDJb3M7VabNO5oZr_oZLQPiC5D1IA5ilYjHTgT6QyK4bQ5vS2iT-ZxvKdILjl-haEkgNXYgkKgpsTONMfpLJwypHSqazb8Gg73QJ46hl3NJyfXGQYkE_Jdrg4BqCAebIUgBm7N7lYL10gv1sI9OEKg0eadxxSSYFZ3eRYnhzKaCHhYCBS11YQmxgaW_ery3Bfw_HlNhCSxdCjNjiZodMBFMebyK3oH637eg7XNnZL7JHBlfXVQvB6rdjXMvwHuHRI3Ys1Uuh9CWAeau31xKxX47PZ5L1oNfItM96RmlEdBOkGrHphkW4bBG42UzNCJU5qhyPMhCtb5r3GMP2JlWd6fD2ihgdkQB9R-Uhin1_N1vVFe4ibdGDgM0Pc2waO8xG_QGdlpiIGKu-Yl6eIXlSiYeFtutWhK0O-vtjJUJiLccdnKs7zexlf1nzlITd_omlhgFheVqvIfT-9mK_uFEgEzboNqE3lR3ttDaO7gLidGwEjB5-WiaE-sqbjQSYRgNEZlO2xJw7vIn8RnP4dCr71RVUZfAhTSdHTxVzZKcSjzuw-Css5Hrn0UIaiHERu6WXebgZ5JvYhK_s2aEHzaRH3NE9FPR1BWRVlv4R9NpDe-nUBTzu7-r.SaR5ULBqHhJBLyrP7TbysQ"
}, conversation_id=None, parent_id=None)

code = open(sys.argv[1]).read()

DELIMITER = '----------------------------------'
print(DELIMITER)
target_lang = 'Ruby'
python_to_other_lang_command = """???????????????????????????????????????Python?????????????????????{target_lang}??????????????????????????????????????????\n????????????????????????????????????????????????????????????????????????????????????????????????\n\n{code}"""
req = python_to_other_lang_command.format(target_lang=target_lang, code=code)
response = chatbot.ask(req, conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)

# print(response)
print(response['message'])
# {'message': '???????????????????????????????????????', 'conversation_id': 'fb27c4cf-9fa6-4efd-acc8-46d66fc83286', 'parent_id': '12cb3289-9acd-4cd5-986c-890e2e8a8900'}

