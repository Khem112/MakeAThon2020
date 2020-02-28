from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot
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
                logic_adapters=[
                        {
                        "import_path": "chatterbot.logic.BestMatch",
                        "statement_comparison_function": chatterbot.comparisons.levenshtein_distance,
                        "response_selection_method": chatterbot.response_selection.get_first_response,
                        'default_response': 'I am sorry, but I do not understand.',
                        'maximum_similarity_threshold': 0.90,
                        'input_text': 'Help me!',
                        'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
                        }
                ],
                trainer='chatterbot.trainers.ListTrainer',
        )
# trainer = ListTrainer(medical_bot)

while True:
    userText = input()
    response = medical_bot.get_response(userText)
    print('bot : '+str(response)+' with confidence ' + str(response.confidence) + ' \n')
    # appendfile=os.listdir('./saved_conversations')[-1]
    # appendfile= open('./saved_conversations/'+str(filenumber),"a")
    # appendfile.write('user : '+userText+'\n')
    # appendfile.write('bot : '+response+'\n')
    # appendfile.close()
