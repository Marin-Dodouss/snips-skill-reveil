#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from datetime import datetime
from pytz import timezone

import locale
locale.setlocale(locale.LC_TIME,'')
'French_France.1252'

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def verbalise_hour(i):
	if i == 0:
		return "minuit"
	elif i == 1:
		return "une heure"
	elif i == 12:
		return "midi"
	elif i == 21:
		return "vingt et une heures"
	else:
		return "{0} heures".format(str(i)) 

def verbalise_minute(i):
	if i == 0:
		return ""
	elif i == 1:
		return "une"
	elif i == 21:
		return "vingt et une"
	elif i == 31:
		return "trente et une"
	elif i == 41:
		return "quarante et une"
	elif i == 51:
		return "cinquante et une"
	else:
		return "{0}".format(str(i)) 


def intent_received(hermes, intent_message):

	print()
	print(intent_message.intent.intent_name)
	print ()
	
	if intent_message.intent.intent_name == 'Watson:DeleteReveil':

		now = datetime.now(timezone('Europe/Paris'))
		day=now.strftime(" %A %d")
		month=now.strftime(" %B")
		year=now.strftime(" %Y")
		answer='Le reveil a bien été supprimé '
		print(answer)
		
		print(intent_message.intent.intent_name)
		print(answer)

		hermes.publish_end_session(intent_message.session_id, answer)

	elif intent_message.intent.intent_name == 'Watson:AddReveil':

		hermes.publish_end_session(intent_message.session_id, "De rien!")


with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
