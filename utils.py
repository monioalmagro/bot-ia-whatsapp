import services
from type_message import Message

def process_message(body):
    entry = body['entry'][0]
    changes = entry['changes'][0]
    value = changes['value']
    message = value['messages'][0]
    contacts = value['contacts'][0]
    data = {
        "number":54111536102558,#services.replace_start(message['from'])
        "messageId":message['id'],
        "contacts":value['contacts'][0],
        "name":contacts['profile']['name'],
        "text":services.obtener_Mensaje_whatsapp(message),
    }
    return Message(**data)
