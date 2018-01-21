# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

responses = raw_input("Ask me a question \n\n[+] ")

chatbot = ChatBot("Billy")
conversation = [
	"Hello",
	"Hi there",
	"How are you doing?",
	"I'm doing great",
	"That is good to hear",
	"Thank you",
	"You're welcome",
	
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

response = chatbot.get_response("%s" % responses)
print(response)
