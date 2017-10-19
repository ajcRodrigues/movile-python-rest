# Movile Rest API
## Python library for Movile Messaging API

###### Usage

```py
import movile
api = movile.config(token=MOVILE_API_TOKEN, user_name=MOVILE_USER_NAME)
sms_id = movile.SmsService().send('cellphone_number', 'message')
```


## Instalation

Clone the repository source:

    $ git clone https://github.com/ajcRodrigues/movile-python-rest.git

Execute the setup script using pip:

    $ cd movile-python-rest
    $ pip3 install -r requirements.txt


## Author

[Antônio José da Cunha Rodrigues](https://github.com/ajcRodrigues).
