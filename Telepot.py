
import telepot
import sys
import time
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

class foodcourt:
    def __init__(self,ID,name,table):
        self.ID = ID
        self.name = name
        self.totalTable = table
        self.vacancy = 0

    def getID(self):
        return ID

    def notEmpty(self):
        return (self.totalTable == self.vacancy)

class Booking:
   def __init__ (self, userID, tableNo):
       self.userID = userID
       self.tableNo = tableNo
       self.time = 0
       self.data = 0
    
def getEmptySeats(foodcourt): #return a list of available seats
    if(foodcourt.notEmpty()==False):
        booking_obj = FoodCourt[foodcourt]
        seats_taken = []
        for obj in booking_obj:
            seats_taken.append(obj.tableNo)

        temp = []
        for i in range(foodcourt.totalTable+1):
            if(i not in seats_taken):
                temp.append(i)
        
        return temp

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, 'Alert!')

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    fd_list = list(FoodCourt.keys())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text=fd_list[0].name, callback_data=fd_list[0].ID)],
                   [InlineKeyboardButton(text=fd_list[1].name, callback_data=fd_list[1].ID)],
                   [InlineKeyboardButton(text=fd_list[2].name, callback_data=fd_list[2].ID)], # change to for loop
               ])
    bot.sendMessage(chat_id, 'Choose available Foodcourt Nearby!', reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    
    # if (query_data == "1"):
      

    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Got it')

# TOKEN = "705383915:AAH91NI5ldgCZeEaGsQ0X4m-BZtuP9ch8_U"
TOKEN = "702870578:AAHnheWkGq7g9lDHfOCeWqKdwtGDcDaZnm4"
bot = telepot.Bot(TOKEN)
bot_data = bot.getMe()

FoodCourt = {}
FR = foodcourt("1","FoodRepublic",20)
KF = foodcourt("2","Koufu",25)
FG = foodcourt("3","Foogle",20)

a = Booking("1",2)
b = Booking("2",10)
c = Booking("3",12)
d = Booking("4",4)
e = Booking("5",9)

FoodCourt = {FR: [a,b], KF:[c,d,e],FG:[]} #dict

MessageLoop(bot, {'chat': on_chat_message,'callback_query': on_callback_query}).run_as_thread()

while 1:
    time.sleep(10)

