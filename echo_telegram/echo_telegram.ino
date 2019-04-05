/*******************************************************************
*  An example of bot that echos back any messages received         *
*                                                                  *
*  written by Giacarlo Bacchio (Gianbacchio on Github)             *
*  adapted by Brian Lough                                          *
*******************************************************************/
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>
#include <sys/time.h>
#include <stdio.h>
#include <stdbool.h>

// Initialize Wifi connection to the router
char ssid[] = "X";     // your network SSID (name)
char password[] = "X"; // your network key

// Initialize Telegram BOT
#define BOTtoken "702870578:AAHnheWkGq7g9lDHfOCeWqKdwtGDcDaZnm4"  // your Bot Token (Get from Botfather)

WiFiClientSecure client;
UniversalTelegramBot bot(BOTtoken, client);

int Bot_mtbs = 1000; //mean time between scan messages
long Bot_lasttime;   //last time messages' scan has been done

void setup() {
  Serial.begin(9600);

  // Set WiFi to station mode and disconnect from an AP if it was Previously
  // connected
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);

  // Attempt to connect to Wifi network:
  Serial.print("Connecting Wifi: ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (millis() > Bot_lasttime + Bot_mtbs)  {
    int numNewMessages = bot.getUpdates(bot.last_message_received + 1);
    struct timeval tv;
    time_t t_start = 0, curr_time = 0;
    time_t time_elapsed;
    bool vacancy = true;
    
    Serial.println(numNewMessages);

    while(numNewMessages) {      
      for (int i=0; i<numNewMessages; i++) {
        // bot.sendMessage(bot.messages[i].chat_id, bot.messages[i].text, "");

        gettimeofday(&tv, NULL); 
        curr_time=tv.tv_sec;

        // if there is a vacancy
        if (vacancy)
        {
          // if /start button is hit
          if (strcmp(bot.messages[i].text.c_str(), "/start") == 0)
          {
            //Serial.println(bot.messages[i].name);
            // Serial.println(bot.messages[i].username);
            char response[50];
            sprintf(response, "%s %s!", "Welcome User ", bot.messages[i].chat_id.c_str());
            bot.sendMessage(bot.messages[i].chat_id, bot.messages[i].from_name, "");
            bot.sendMessage(bot.messages[i].chat_id,"To chope a table, type /chope", "");
            Serial.println("New user!");
          }
  
          // if /chope is entered
          else if (strcmp(bot.messages[i].text.c_str(), "/chope") == 0)
          {
            bot.sendMessage(bot.messages[i].chat_id,"Seat choped for 15mins, type /here to disarm system and claim chope.", "");
  
            // start the timer
            gettimeofday(&tv, NULL); 
            t_start=tv.tv_sec;
            Serial.println("SEAT IS CHOPED!");
            vacancy = false;
          }
  
          // if /here is entered
          else if (strcmp(bot.messages[i].text.c_str(), "/here") == 0)
          { 
             bot.sendMessage(bot.messages[i].chat_id,"Session has started. It will last for 45mins, type /end to end session", "");
             Serial.println("Session has started!");
          }
  
          // if user choses to end
          else if (strcmp(bot.messages[i].text.c_str(), "/end") == 0)
          {
            curr_time = (t_start + (45 * 3600));
            Serial.print("ENDEED!!!!\n\n\n\n");
          }

          // if time is up
          if (curr_time >= (t_start + (45 * 3600)))
          {
            Serial.print("IN!!!!\n\n\n\n");
            bot.sendMessage(bot.messages[i].chat_id,"Time is Up!", "");
            vacancy = true;
          }
        }

        else
        {
          bot.sendMessage(bot.messages[i].chat_id,"The seat is choped! Try again later!", "");
        }
        
      }
      numNewMessages = bot.getUpdates(bot.last_message_received + 1); 
        
    }

    Bot_lasttime = millis();
  }
}
