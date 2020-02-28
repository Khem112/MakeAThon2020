from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# filenumber=int(os.listdir('./saved_conversations')[-1])
# filenumber=filenumber+1
# file= open('./saved_conversations/'+str(filenumber),"w+")
# file.write('bot : Hi There! I am a medical chatbot. You can begin conversation by typing in a message and pressing enter.\n')
# file.close()

medical_bot = ChatBot('Bot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            ogic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch'
                },
            ],
            trainer='chatterbot.trainers.ListTrainer')
# trainer = ListTrainer(medical_bot)
while True:
    userText = input()
    response = str(medical_bot.get_response(userText))
    print('bot : '+response+'\n')
    # appendfile=os.listdir('./saved_conversations')[-1]
    # appendfile= open('./saved_conversations/'+str(filenumber),"a")
    # appendfile.write('user : '+userText+'\n')
    # appendfile.write('bot : '+response+'\n')
    # appendfile.close()
