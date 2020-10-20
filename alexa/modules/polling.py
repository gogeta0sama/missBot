# MADE BY @MissAlexa_Robot
# He has wasted a lot of time of his life to make this so please give proper credits to him 😭

from telethon import *
from telethon.tl import *
from alexa.events import register
from pymongo import MongoClient
from alexa import MONGO_DB_URI
from alexa.events import register
from alexa import tbot


client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client['test']
approved_users = db.approve


#------ THANKS TO LONAMI ------#
async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (await tbot(functions.channels.GetParticipantRequest(chat, user))).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator)
        )
    elif isinstance(chat, types.InputPeerChat):
        ui = await tbot.get_peer_id(user)
        ps = (await tbot(functions.messages.GetFullChatRequest(chat.chat_id))) \
            .full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator)
        )
    else:
        return None

# syntax : /poll am i cool? | False False False yes no
# syntax : /poll am i cool? | True@1 False False yes no
@register(pattern="^/poll (.*)")
async def _(event):
    approved_userss = approved_users.find({})
    for ch in approved_userss: 
        iid = ch['id']
        userss = ch['user']
    if event.is_group:
     if (await is_register_admin(event.input_chat, event.message.sender_id)):
       pass
     elif event.chat_id == iid and event.from_id == userss:  
       pass
     else:
       return
    try: 
      quew= event.pattern_match.group(1)
    except Exception:
       await event.reply("Where is the question ?")
       return
    if "|" in quew:
                quess, options = quew.split("|")
    ques = quess.strip()
    option = options.strip()
    quiz = option.split(' ')[1-1] 
    if "True" in quiz:
       quizy = True
       if "@" in quiz:
          one, two = quiz.split("@")
          rightone = two.strip()
       else:
          await event.reply("You need to select the right answer with question number like True@1, True@3 etc..")
          return          

       quizoptionss = []
       try: 
         ab = option.split(' ')[4-1] 
         cd = option.split(' ')[5-1] 
         quizoptionss.append(types.PollAnswer(ab, b'1'))
         quizoptionss.append(types.PollAnswer(cd, b'2'))
       except Exception:
         await event.reply("At least need two options to create a poll")
         return
       try:
         ef = option.split(' ')[6-1] 
         quizoptionss.append(types.PollAnswer(ef, b'3'))
       except Exception:
         ef = None        
       try:
         gh = option.split(' ')[7-1] 
         quizoptionss.append(types.PollAnswer(gh, b'4'))
       except Exception:
         gh = None  
       try:
         ij = option.split(' ')[8-1] 
         quizoptionss.append(types.PollAnswer(ij, b'5'))
       except Exception:
         ij = None
       try:
         kl = option.split(' ')[9-1] 
         quizoptionss.append(types.PollAnswer(kl, b'6'))
       except Exception:
         kl = None
       try:
         mn = option.split(' ')[10-1] 
         quizoptionss.append(types.PollAnswer(mn, b'7'))
       except Exception:
         mn = None        
       try:
         op = option.split(' ')[11-1] 
         quizoptionss.append(types.PollAnswer(op, b'8'))
       except Exception:
         op = None   
       try:
         qr = option.split(' ')[12-1] 
         quizoptionss.append(types.PollAnswer(qr, b'9'))
       except Exception:
         qr= None   
       try:
         st = option.split(' ')[13-1] 
         quizoptionss.append(types.PollAnswer(st, b'10'))
       except Exception:
         st = None   
         
    elif "False" in quiz:
       quizy = False
    else:
       await event.reply("Wrong arguments provided !")
       return
       
    pvote = option.split(' ')[2-1] 
    if "True" in pvote:
       pvoty = True
    elif "False" in pvote:
       pvoty = False
    else:
       await event.reply("Wrong arguments provided !")
       return
    mchoice = option.split(' ')[3-1] 
    if "True" in mchoice:
       mchoicee = True
    elif "False" in mchoice:
       mchoicee = False
    else:
       await event.reply("Wrong arguments provided !")
       return
    optionss = []
    try: 
      ab = option.split(' ')[4-1] 
      cd = option.split(' ')[5-1] 
      optionss.append(types.PollAnswer(ab, b'xnx'))
      optionss.append(types.PollAnswer(cd, b'xdnxx'))
    except Exception:
      await event.reply("At least need two options to create a poll")
      return
    try:
      ef = option.split(' ')[6-1] 
      optionss.append(types.PollAnswer(ef, b'dnxnx'))
    except Exception:
      ef = None     
    try:
      gh = option.split(' ')[7-1] 
      optionss.append(types.PollAnswer(gh, b'xowpx'))
    except Exception:
      gh = None  
    try:
      ij = option.split(' ')[8-1] 
      optionss.append(types.PollAnswer(ij, b'xppalx'))
    except Exception:
      ij = None
    try:
      kl = option.split(' ')[9-1] 
      optionss.append(types.PollAnswer(kl, b'wppowpx'))
    except Exception:
      kl = None
    try:
      mn = option.split(' ')[10-1] 
      optionss.append(types.PollAnswer(mn, b'owozpx'))
    except Exception:
      mn = None     
    try:
      op = option.split(' ')[11-1] 
      optionss.append(types.PollAnswer(op, b'aoaalx'))
    except Exception:
      op = None   
    try:
      qr = option.split(' ')[12-1] 
      optionss.append(types.PollAnswer(qr, b'owzkkx'))
    except Exception:
      qr= None   
    try:
      st = option.split(' ')[13-1] 
      optionss.append(types.PollAnswer(st, b'wxxvuurpx'))
    except Exception:
      st = None   
  
    if pvoty==False and quizy==False and mchoicee==False:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=[
            optionss
          ],
          quiz=False
            ),           
        ))
      
    if pvoty==True and quizy==False and mchoicee==True:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=[
            optionss
          ],
          quiz=False,
          multiple_choice=True, 
          public_voters=True
            ),           
        ))

    if pvoty==True and quizy==False and mchoicee==True:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=[
            optionss
          ],
          quiz=False,
          multiple_choice=True, 
          public_voters=True
            ),           
        ))

    if pvoty==False and quizy==False and mchoicee==True:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=[
            optionss
          ],
          quiz=False,
          multiple_choice=True, 
          public_voters=False
            ),           
        ))

    if pvoty==False and quizy==True and mchoicee==False:      
     await tbot.send_file(event.chat_id, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=[
            optionss
          ],
          quiz=False,
          multiple_choice=False, 
          public_voters=True
            ),           
        ))

    if pvoty==False and quizy==True and mchoicee==False:
     await tbot.send_file(chat, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=quizoptionss,
        quiz=True
    ),
    correct_answers=[b'{}'.format(rightone)]))
    
    if pvoty==True and quizy==True and mchoicee==False:
     await tbot.send_file(chat, types.InputMediaPoll(
      poll=types.Poll(
        id=12345,
        question=ques,
        answers=quizoptionss,
        quiz=True,
        public_voters=True
    ),
    correct_answers=[b'{}'.format(rightone)]))
    
    if pvoty==True and quizy==True and and mchoicee==True:
       await event.reply("You can't use multiple voting with quiz mode")
       return
       
