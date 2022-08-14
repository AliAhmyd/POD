# -*- coding: utf-8 -*-
from re import I
import vk_api
import json
import random
import time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

sms = [
"""
подготовка...
""",
"""
подключение к хостингу القاعدة ...
""",
"""
инициализация...
""",
"""
ответ от VK_API...
""",
"""
успешно!запуск...
"""
]
newk = 0
for q in range(5):
    print(sms[newk])
    newk +=1
    if newk == 5:
        newk = 0
    time.sleep(0.5)

print ('𝚁𝙰𝙸𝙳𝙴𝚁 𝙶𝙻𝙰 2.5  ₳Ʉ₮ⱧØⱤ: ₳Ⱡł ₳Ⱨ₥ɎĐ,V₭: ₴ⱧɆłⱧ_₳Ⱡł_₳Ⱨ₥ɎĐ,пригласи HOIC в чат')
print ('𝔸𝕝𝕝𝕒𝕩𝕦 𝔸𝕜𝕓𝕒𝕣')
vk = vk_api.VkApi(token='vk1.a.JAZkpmfCOvMvTYMnpnNfYyfYXStYMJwVRMfyAYnyfIPeaZY3bmgDqO2rn1Bk1v2fBLdNn5Mwe7TIYAkakPzp6NkXdjva4aKPjQmgMiOyHkMgin2N97TZF9NucpTD-ahvyxFw-REtUODUpUThwBnAsYPOOwomM97hHHjjJU0762jKSb9yyvxEx6qZO4Y4AkBB') 
vk._auth_token()
vk.get_api()
def get_random_id():
    return random.randint(0, 100000000000)

group_id = '214432926' 

longpoll = VkBotLongPoll(vk, group_id)
bot_help = '''

'''

print(bot_help)
for event in longpoll.listen():
   if event.type == VkBotEventType.MESSAGE_NEW:
            d1 = event.object.message
            s1 = json.dumps(d1)
            d2 = json.loads(s1)

            json_object = d2
            message = json_object['text']

            message = message.split("alkaida")
            msg_text = event.object.message['text']
            str1 = message[0].split("|")[0]


            str1 = str1.replace("club", "alkaida")
            if group_id == str1:
                message.pop(0)

            message = 'AL-KAIDA'.join(message).lower()

            id = json_object['peer_id']
            try:
                dey = event.message.action['type']
            except:
                dey = ''
            
            print(message)
            print ('выполнено!пушка в чате!')
            g = input ('чтобы взорвать жопу всем в чате нажми enter: ')
            print ('орудие активировано!')
            if dey == 'chat_invite_user':
                while True:
                    keyboard = VkKeyboard()
                    keyboard.add_button('стоп vto.pe аккаунт взломан', VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('сила  vto.pe взломан акк', VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('мощность vto.pe и лучший хакер взломал', VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('ALKAIDA vto.pe акк взломан', VkKeyboardColor.NEGATIVE)
                    keyboard.add_button('мне пизды vto.pe  явзломан', VkKeyboardColor.NEGATIVE)
                    keyboard.get_keyboard()
                    vk.method("messages.send", {"peer_id": id, 'random_id':get_random_id(), "message": f"Аль-Каида!Аллаху Акбар!", "attachment": 'wall-210968544_63',"keyboard": keyboard.get_keyboard()})
  
