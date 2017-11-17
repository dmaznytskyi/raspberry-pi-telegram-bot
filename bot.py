from subprocess import call
import json
import subprocess
import requests

url = "https://api.telegram.org"
token = "/bot000000000:000000000000000000000000000000-0000"
action = "/sendMessage"
where = "?chat_id=000000000"
text = "&text="

cmd = "ifconfig | grep \"inet \" | grep -v 127 | sed 's/:/ /g' | cut -d ' ' -f 13"

last_upd_id = 0
user_id_self = 000000000
response = ""

while 1:
    response = requests.get(url + token + "/getUpdates", {"offset":"-1"})
    response_json = json.loads(response.text)
    print response.text + '\n'
    print response_json
    try:
        print response_json['result'][0]['text']
    finally:
        print "unknown error"
    new_upd_id = response_json['result'][0]['update_id']
    if new_upd_id > last_upd_id:
        last_upd_id = new_upd_id
        print last_upd_id
        if response_json['result'][0]['text'] == "/reboot" and response_json['result'][0]['id'] == user_id_self:
            response = requests.get(url + token + action + where + text + "Bot rebooting")
            call(["reboot"])
        elif response_json['result'][0]['text'] == "/reboot router" and response_json['result'][0]['id'] == user_id_self:
            response = requests.get(url + token + action + where + text + "Router rebooting")
            call(["expect", "rrrebot"])
    call(["sleep", "10"])
