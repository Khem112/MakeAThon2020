from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

try:
	os.remove("db.sqlite3")
	print("Old database removed. Training new database")
except:
	print('No database found. Creating new database.')

medical_bot = ChatBot('Bot')
trainer = ListTrainer(medical_bot)
for file in os.listdir('./NLP-chatbot/data'):
        print('Training using '+file)
        convData = open('./NLP-chatbot/data/' + file).readlines()
        trainer.train(convData)
        print("Training completed for "+file)
    

