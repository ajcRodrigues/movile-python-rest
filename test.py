# -*- coding: utf-8 -*-

import movile

user_name = "USER_NAME"
token = "API_TOKEN"

cellphone = ''
msg = 'Teste de envio'


if __name__ == "__main__":
    api = movile.config(token=token, user_name=user_name)
    srv = movile.SmsService()
    ret = srv.send(cellphone, msg)
    print(ret)

