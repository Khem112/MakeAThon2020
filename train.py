from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import chatterbot
import os

try:
	os.remove("db.sqlite3")
	print("Old database removed. Training new database")
except:
	print('No database found. Creating new database.')

medical_bot = ChatBot('Bot',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters=[
                        {
                        "import_path": "chatterbot.logic.BestMatch",
                        "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
                        "response_selection_method": "chatterbot.response_selection.get_first_response",
                        'default_response': 'I am sorry, but I do not understand.',
                        'maximum_similarity_threshold': 0.90,
                        'input_text': 'Help me!',
                        'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
                        }
                ],
                trainer='chatterbot.trainers.ListTrainer',
        )
trainer = ListTrainer(medical_bot)
for file in os.listdir('./data'):
        print('Training using '+file)
        convData = open('./data/' + file).readlines()
        print(convData)
        trainer.train(convData)
        print("Training completed for "+file)

trainer.export_for_training('./my_export.json')

