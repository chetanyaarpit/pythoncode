from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('BOT')
#bot.set_trainer(ListTrainer)
trainer = ListTrainer(bot)

for files in os.listdir('/home/adventum/Downloads/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    #a.append(files)
    data = open('/home/adventum/Downloads/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    trainer.train(data)
    
while True:
    message = input('YOU:')
    if message.strip() !='Bye':
        reply = bot.get_response(message)
        print('Chatbot: ',reply)
    if message.strip() == 'Bye':
        print('Chatbot: Bye')
        break
        
            