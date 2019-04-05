import sys
import time
import telepot
from pprint import pprint
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

question = "What would you like to?"
TOKEN = '702870578:AAHnheWkGq7g9lDHfOCeWqKdwtGDcDaZnm4'

"""
def on_chat_message(msg):
    username = msg['from']['username']
    content_type, chat_type, chat_id = telepot.glance(msg)

    # if it is from client
    if username != "arduino":
        # send menu page
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
                       [InlineKeyboardButton(text='Turn On', callback_data='on')],
                       [InlineKeyboardButton(text='Turn Off', callback_data='off')]
                   ])

        bot.sendMessage(chat_id, question, reply_markup=keyboard)

    # if it is from arduino
    else:
        print ("Arduino")
        bot.sendMessage(chat_id, "There is an intrusion!")

# pop up
def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    #  print('Callback Query:', query_id, from_id, query_data)

    response = "\'" + query_data + "\' is pressed"
    bot.answerCallbackQuery(query_id, text=response)

    if (query_data == 'on'):
        print ("Client " + str(from_id) + " : Turn on")
    else:
        print ("Client " + str(from_id) + " : Turn off")

def handle(msg):
    username = msg['from']['username']
    content_type, chat_type, chat_id = telepot.glance(msg)

    # print (msg)
    #  print (telepot.flavor(msg))
   
    # if it is from client
    #  if content_type == 'text':
        #  bot.sendMessage(chat_id, msg['text'])
    if username != "arduino":
        
        # turn on the arduino
        if msg['text'] == '/start':
            
            # login
            bot.sendMessage(chat_id, "Please enter your username: ")
            
            
            clientID = chat_id 
            print ("Arduino is on")
            # menu(chat_id)

        # print out options
        else:
            print()
            # menu(chat_id)

        # if it is from ardiono
    else:
        # if there is an intrusion
        bot.sendMessage(clientID, "There is an intrusion!")

        bot = telepot.Bot('747252402:AAHtA50tSP2IPe8_jtz1JD9lLvRvYRESbWw')

    MessageLoop(bot, handle).run_as_thread()
    #  MessageLoop(bot, {'chat': on_chat_message,
    #                    'callback_query': on_callback_query}).run_as_thread()
    print ('Listening ...')

    # Keep the program running.
    while 1:
        time.sleep(10)

"""

FoodCourt = {'FoodRepublic':[0,0,0], 'Koufu':[0], 'Foogle':[0,0,0]}
reservation = []

class Booking:
    def __init__ (self, userID, tableNo, time, date):
        self.userID = userID
        self.tableNo = tableNo
        self.time = time
        self.data = date

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Yes', callback_data='Yes')],
                   [InlineKeyboardButton(text='No', callback_data='No')],
               ])

    bot.sendMessage(chat_id, 'Do you want to make a reservation?', reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    # if user chooses to reserve
    if (query_data == "Yes"):
        # if reservation is empty
        if not reservation:
            reservation.append(from_id)
            print ("You have just reserved a seat!")

        else:
            # checks if a reservation has been made
            exists = from_id in reservation

            if (exists == True):
                print ("A reservation has been made!")
            else:
                reservation.append(from_id)
                print ("You have just reserved a seat!")

        bot.answerCallbackQuery(query_id, query_data)
    
    # else
    else:
        print ("Back to Main Menu")
        bot.answerCallbackQuery(query_id, "Back to Main Menu")
    

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)