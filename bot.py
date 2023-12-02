import os ,re
from pyrogram import Client, filters
import requests
import pytesseract
from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery , ForceReply
import shutil
import pypdfium2 as pdfium
bot = Client(
    "audiobot",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5998058674:AAEXlnSyDM3Cz-q9AAqOdHWzBYxFzxv3EPE"
)

CHOOSE_UR_AUDIO_MODE = "اختر العملية  التي تريد "
CHOOSE_UR_AUDIO_MODE_BUTTONS = [
    [InlineKeyboardButton("تضخيم صوتية / فيديو ",callback_data="amplifyaud")],[InlineKeyboardButton("قص صوتية / فيديو ",callback_data="trim")],
    [InlineKeyboardButton("تسريع صوتية / فيديو ",callback_data="speedy")],[InlineKeyboardButton("تحويل صوتية / فيديو ",callback_data="conv")], 
     [InlineKeyboardButton("كتم صوت الفيديو",callback_data="mute")], [InlineKeyboardButton("ضغط الصوتية ",callback_data="comp")],[InlineKeyboardButton("تقسيم الصوتية ",callback_data="splitty")],
    [InlineKeyboardButton("دمج صوتيات ",callback_data="audmerge")], [InlineKeyboardButton("تغيير الصوت",callback_data="voicy")],[InlineKeyboardButton("إبدال صوت الفيديو ",callback_data="subs")], [InlineKeyboardButton("منتجة فيديو ",callback_data="imagetovid")],  [InlineKeyboardButton("تفريغ صوتية",callback_data="transcribe")],[InlineKeyboardButton("إعادة التسمية ",callback_data="renm")], [InlineKeyboardButton("OCR صور",callback_data="OCR")],[InlineKeyboardButton("تفريغ pdf",callback_data="pdfOCR")],[InlineKeyboardButton("titled",callback_data="titled")]
]

CHOOSE_UR_AMPLE_MODE = "اختر نمط التضخيم "
CHOOSE_UR_AMPLE_MODE_BUTTONS = [
    [InlineKeyboardButton("5db",callback_data="mod1")],
     [InlineKeyboardButton("10db",callback_data="mod2")],
     [InlineKeyboardButton("15db",callback_data="mod3")],
     [InlineKeyboardButton("20db",callback_data="mod4")],
     [InlineKeyboardButton("25db",callback_data="mod5")]
]

CHOOSE_UR_COMP_MODE = " اختر نمط الضغط \n كلما قل الرقم زاد الضغط و قل حجم الصوتية "
CHOOSE_UR_COMP_MODE_BUTTONS = [
    [InlineKeyboardButton("10k",callback_data="compmod1")],
     [InlineKeyboardButton("20k",callback_data="compmod2")],
     [InlineKeyboardButton("30k",callback_data="compmod3")],
     [InlineKeyboardButton("40k",callback_data="compmod4")],
     [InlineKeyboardButton("50k",callback_data="compmod5")]
]

CHOOSE_UR_FILE_MODE = "اختر نوع ملفك "
CHOOSE_UR_FILE_MODE_BUTTONS = [
    [InlineKeyboardButton("صوتية",callback_data="aud")],
     [InlineKeyboardButton("فيديو ",callback_data="vid")]
]

CHOOSE_UR_FILETRIM_MODE = "اختر نوع ملفك "
CHOOSE_UR_FILETRIM_MODE_BUTTONS = [
    [InlineKeyboardButton("صوتية",callback_data="audtrim")],
     [InlineKeyboardButton("فيديو ",callback_data="vidtrim")]
     ]
CHOOSE_UR_FILERENM_MODE = "اختر نوع ملفك "
CHOOSE_UR_FILERENM_MODE_BUTTONS = [
    [InlineKeyboardButton("صوتية",callback_data="audrenm")],
     [InlineKeyboardButton("فيديو ",callback_data="vidrenm")],
     [InlineKeyboardButton("وثيقة",callback_data="docrenm")]
]
CHOOSE_UR_FILESPED_MODE = "اختر نوع ملفك "
CHOOSE_UR_FILESPED_MODE_BUTTONS = [
    [InlineKeyboardButton("صوتية",callback_data="speedfileaud")],
     [InlineKeyboardButton("فيديو ",callback_data="speedfilevid")]
]

CHOOSE_UR_SPEED_MODE = "اختر نمط التسريع "
CHOOSE_UR_SPEED_MODE_BUTTONS = [
    [InlineKeyboardButton("x1.25",callback_data="spd1")],
     [InlineKeyboardButton("x1.5 ",callback_data="spd2")],
     [InlineKeyboardButton("x1.75",callback_data="spd3")],
      [InlineKeyboardButton("x2",callback_data="spd4")]
]

CHOOSE_UR_MERGE = "أرسل الصوتية التالية  \n تنبيه / بعد الانتهاء من إرسال الصوتيات اضغط دمج الآن "
CHOOSE_UR_MERGE_BUTTONS = [
    [InlineKeyboardButton("دمج الآن ",callback_data="mergenow")] ]

CHOOSE_UR_CONV_MODE = "اختر نمط التحويل"
CHOOSE_UR_CONV_MODE_BUTTONS = [
    [InlineKeyboardButton("تحويل صوتية/ فيديو إلى mp3",callback_data="audconv")],
     [InlineKeyboardButton("تحويل صوتية/ فيديو إلى m4a",callback_data="audconvm4a")],
    [InlineKeyboardButton("تحويل فيديو إلى mp4 ",callback_data="vidconv")]
]
CHOOSE_UR_SUBS_MODE = '''اختر ما يناسب'''
CHOOSE_UR_SUBS_MODE_BUTTONS = [
    [InlineKeyboardButton("هذا الفيديو",callback_data="thisisvid")], [InlineKeyboardButton("إبدال الآن",callback_data="subsnow")]]
CHOOSE_UR_MON_MODE = '''اختر ما يناسب'''
CHOOSE_UR_MON_MODE_BUTTONS = [
    [InlineKeyboardButton("هذه الصورة",callback_data="thisisimage")], [InlineKeyboardButton("منتجة الآن",callback_data="montagnow")]]

@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم أنا بوت متعدد الاستعمالات , فقط أرسل الفيديو أو الصوتية هنا\n\n  لبقية البوتات هنا \n\n https://t.me/sunnay6626/2 ",disable_web_page_preview=True)
@bot.on_message(filters.command('clear') & filters.private)
def command2(bot,message):
    cmd('''rm list.txt ''')
    
@bot.on_message(filters.private & filters.incoming & filters.voice | filters.audio | filters.video | filters.document | filters.photo )
def _telegram_file(client, message):
  global user_id
  user_id = message.from_user.id
  global file
  file = message
  global file_path
  file_path = message.download(file_name="./downloads/")
  global filename
  filename = os.path.basename(file_path)
  global nom
  global ex
  nom,ex = os.path.splitext(filename)
  global mp4file
  mp4file = f"{nom}.mp4"
  global mp3file
  mp3file = f"{nom}.mp3"
  global m4afile
  m4afile = f"{nom}.m4a"
  global spdrateaud
  global mergdir
  global trimdir
  mergdir = f"./mergy/{mp3file}"
  trimdir = f"./trimmo/{mp3file}"
  global result
  result = f"{nom}.txt"



  message.reply(
             text = CHOOSE_UR_AUDIO_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_AUDIO_MODE_BUTTONS)

        )




@bot.on_callback_query()
def callback_query(CLIENT,CallbackQuery):
  global amplemode 
  if CallbackQuery.data == "amplifyaud":
     CallbackQuery.edit_message_text(
             text = CHOOSE_UR_AMPLE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_AMPLE_MODE_BUTTONS)

        )

  elif CallbackQuery.data == "comp":
   CallbackQuery.edit_message_text(
             text = CHOOSE_UR_COMP_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_COMP_MODE_BUTTONS) )
  elif  CallbackQuery.data == "compmod1":
    CallbackQuery.edit_message_text("جار الضغط ") 
    aid = user_id
    cmd(f''' ffmpeg -i "{file_path}" -b:a 10k "{mp3file}" -y ''' )
    with open(mp3file, 'rb') as f:
         bot.send_audio(aid, f)
    cmd(f'''unlink "{mp3file}" ''')
    shutil.rmtree('./downloads/') 
  elif  CallbackQuery.data == "titled":
      cmd(f'''mv "{file_path}" "{filename}"''')
      with open(filename, 'rb') as f:
         bot.send_document(user_id, f)
      CallbackQuery.edit_message_text("تم الإرسال  ") 
      cmd(f'''rm "{filename}"''')

  elif  CallbackQuery.data == "voicy":   
    CallbackQuery.edit_message_text("جار تغيير الصوت ") 
    bid = user_id
    cmd(f'''ffmpeg -i "{file_path}" -af asetrate=44100*0.9,aresample=44100,atempo=1/0.9 "{mp3file}"''')
    with open(mp3file, 'rb') as f:
         bot.send_audio(bid, f)
    cmd(f'''unlink "{mp3file}" ''')
    shutil.rmtree('./downloads/') 

  elif  CallbackQuery.data == "thisisvid":
     cmd(f'''mv "{file_path}" "./downloads/subsvid.mp4" ''')
     CallbackQuery.edit_message_text("الآن أرسل الصوت الجديد ثم اختر إبدال الآن") 
  elif  CallbackQuery.data == "thisisimage":
     cmd(f'''mv "{file_path}" "./downloads/imagetovid.jpg" ''')
     CallbackQuery.edit_message_text("الآن أرسل الصوت  ثم اختر منتجة الآن") 

  elif  CallbackQuery.data == "subs":
     CallbackQuery.edit_message_text(
             text = CHOOSE_UR_SUBS_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SUBS_MODE_BUTTONS)

        )
  elif  CallbackQuery.data == "imagetovid":
     CallbackQuery.edit_message_text(
             text = CHOOSE_UR_MON_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_MON_MODE_BUTTONS)

        )
  elif  CallbackQuery.data == "subsnow":
      CallbackQuery.edit_message_text("جار الإبدال ") 
      cid = user_id
      cmd(f'''ffmpeg -i "./downloads/subsvid.mp4" -i "{file_path}" -c:v copy -map 0:v:0 -map 1:a:0 "{mp4file}"''')
      with open(mp4file, 'rb') as f:
         bot.send_video(cid, f)
      cmd(f''' unlink "{mp4file}"''')
      shutil.rmtree('./downloads/') 

  elif  CallbackQuery.data == "montagnow":
      CallbackQuery.edit_message_text("جار المنتجة ") 
      did = user_id
      cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "./downloads/temp{mp3file}" -y ''')
      cmd(f'''ffmpeg -r 1 -loop 1 -y -i  "./downloads/imagetovid.jpg" -i "./downloads/temp{mp3file}" -c:v libx264 -tune stillimage -c:a copy -shortest -vf scale=1920:1080 "{mp4file}"''')
      with open(mp4file, 'rb') as f:
         bot.send_video(did, f)
      cmd(f''' unlink "{mp4file}"''')
      shutil.rmtree('./downloads/') 
  elif  CallbackQuery.data == "compmod2":
    CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 20k "{mp3file}" -y ''' )
    eid = user_id
    with open(mp3file, 'rb') as f:
         bot.send_audio(eid, f)
    cmd(f'''unlink "{mp3file}" ''')
    shutil.rmtree('./downloads/') 

  elif  CallbackQuery.data == "compmod3":
    fid = user_id
    CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 30k "{mp3file}" -y ''' )
    with open(mp3file, 'rb') as f:
         bot.send_audio(fid, f)
    cmd(f'''unlink "{mp3file}" ''')
    shutil.rmtree('./downloads/') 

  elif  CallbackQuery.data == "compmod4":
    CallbackQuery.edit_message_text("جار الضغط ") 
    gid = user_id
    cmd(f''' ffmpeg -i "{file_path}" -b:a 40k "{mp3file}" -y ''' )
    with open(mp3file, 'rb') as f:
         bot.send_audio(gid, f)
    cmd(f''' unlink "{mp3file}" ''')
    shutil.rmtree('./downloads/') 

  elif  CallbackQuery.data == "compmod5":
    hid = user_id
    CallbackQuery.edit_message_text("جار الضغط ") 
    cmd(f''' ffmpeg -i "{file_path}" -b:a 50k "{mp3file}" -y ''' )
    with open(mp3file, 'rb') as f:
         bot.send_audio(hid, f)
    cmd(f'''unlink "{mp3file}" ''')
    shutil.rmtree('./downloads/') 

  elif CallbackQuery.data == "conv" :
    CallbackQuery.edit_message_text(
             text = CHOOSE_UR_CONV_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_CONV_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "audconv" :
   CallbackQuery.edit_message_text("جار التحويل ") 
   iid = user_id
   cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mp3file}" -y ''')
   with open(mp3file, 'rb') as f:
        bot.send_audio(iid, f)
   cmd(f'''unlink "{mp3file}" ''')
   shutil.rmtree('./downloads/') 
  elif CallbackQuery.data == "audconvm4a" :
   CallbackQuery.edit_message_text("جار التحويل ") 
   lamid = user_id
   cmd(f'''ffmpeg -i "{file_path}" -c:a aac -b:a 192k "{m4afile}" -y ''')
   with open(m4afile, 'rb') as f:
        bot.send_document(lamid, f)
   cmd(f'''unlink "{m4afile}" ''')
   shutil.rmtree('./downloads/') 

  elif CallbackQuery.data == "vidconv" :
   CallbackQuery.edit_message_text(
      
      "جار التحويل "
   ) 
   jid = user_id
   cmd(f'''ffmpeg -i "{file_path}" -codec copy "{mp4file}" -y ''')
   with open(mp4file, 'rb') as f:
        bot.send_video(jid, f)
   cmd(f'''unlink "{mp4file}" ''')
   shutil.rmtree('./downloads/') 

  elif CallbackQuery.data == "trim" :
   file.reply_text("الآن أرسل نقطة البداية والنهاية بهذه الصورة \n\n hh:mm:ss/hh:mm:ss",reply_markup=ForceReply(True))
   CallbackQuery.edit_message_text(
      
      "👇"
   ) 
  elif CallbackQuery.data == "mod1":
      amplemode = 5
      CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "mod2":
      amplemode = 10
      CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "mod3":
      amplemode = 15
      CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "mod4" :
      amplemode = 20
      CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS)

        )
  elif CallbackQuery.data == "mod5":
      amplemode = 25
      CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILE_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILE_MODE_BUTTONS)

        )

  elif CallbackQuery.data == "aud":
    CallbackQuery.edit_message_text(
     "جار التضخيم "
      )
    kid = user_id
    cmd(f'''ffmpeg -i "{file_path}" -filter:a volume={amplemode}dB "{filename}"''')
    with open(filename, 'rb') as f:
        bot.send_audio(kid, f)
    cmd(f'''unlink "{filename}" ''')
    shutil.rmtree('./downloads/') 

  elif CallbackQuery.data == "vid":
    CallbackQuery.edit_message_text(
     "جار التضخيم "
      )
    lid = user_id
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "./downloads/{mp3file}" -y ''')
    cmd(f'''ffmpeg -i "./downloads/{mp3file}" -filter:a volume={amplemode}dB "{mp3file}"''')
    cmd(f'''ffmpeg -i "{file_path}" -i "{mp3file}" -c:v copy -map 0:v:0 -map 1:a:0 "{filename}"''')
    with open(filename, 'rb') as f:
        bot.send_video(lid, f)
    cmd(f'''unlink "{filename}" ''')    
    shutil.rmtree('./downloads/') 

  elif CallbackQuery.data == "audtrim":
    CallbackQuery.edit_message_text(
     "جار القص"
      )  
    qid = user_id
    cmd(f'''mkdir trimmo''')  
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{trimdir}" -y ''')
    cmd(f'''ffmpeg -i "{trimdir}" -ss {strt_point} -to {end_point} -c copy "{mp3file}" -y ''')
    with open(mp3file, 'rb') as f:
            bot.send_audio(qid, f)
    cmd(f'''unlink "{mp3file}"''')
    shutil.rmtree('./downloads/') 
    shutil.rmtree('./trimmo/') 
      
  elif CallbackQuery.data == "vidtrim":
    CallbackQuery.edit_message_text(
     "جار القص"
      )  
    rid = user_id
    cmd(f'''ffmpeg -i "{file_path}" -ss {strt_point} -strict -2 -to {end_point} -c:a aac -codec:v h264 -b:v 1000k "{mp4file}" -y ''')
    with open(mp4file, 'rb') as f:
            bot.send_video(rid, f)
    cmd(f'''unlink "{mp4file}" ''')
    shutil.rmtree('./downloads/') 
  elif CallbackQuery.data == "renm":
    file.reply_text("الآن أدخل الاسم الجديد ",reply_markup=ForceReply(True))
    CallbackQuery.edit_message_text(
      
      "👇"
   ) 

  elif CallbackQuery.data == "audrenm":
    CallbackQuery.edit_message_text("👇")
    aid = user_id
    with open(newfile, 'rb') as f:
             bot.send_audio(aid, f)
    cmd(f'''unlink "{newfile}" ''')
  elif CallbackQuery.data == "vidrenm":
    CallbackQuery.edit_message_text("👇")
    aid = user_id
    with open(newfile, 'rb') as f:
             bot.send_video(aid, f)
    cmd(f'''unlink "{newfile}" ''')
  elif CallbackQuery.data == "docrenm":
    CallbackQuery.edit_message_text("👇")
    aid = user_id
    with open(newfile, 'rb') as f:
             bot.send_document(aid, f)
    cmd(f'''unlink "{newfile}" ''')
  elif CallbackQuery.data == "transcribe":
    try: 
      with open('transcription.txt', 'r') as fh:
        if os.stat('transcription.txt').st_size == 0: 
            pass
        else:
            CallbackQuery.edit_message_text("هناك عملية تفريغ تتم الآن")
            return
    except FileNotFoundError: 
      pass  
    CallbackQuery.edit_message_text("جار التفريغ")
    finalid = user_id
    finalnom = result
    finalmp3 = mp3file
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mp3file}" -y ''')  
    cmd(f'''python3 speech.py RK3ETXWBJQSMO262RXPAIXFSG6NH3QRH "{finalmp3}" "transcription.txt" ''')
    cmd(f'''mv transcription.txt "{finalnom}"''')
    with open(finalnom, 'rb') as f:
        bot.send_document(finalid, f)
    CallbackQuery.edit_message_text("تم التفريغ ✅  ")   
    cmd(f'''rm "{finalnom}" "{finalmp3}"''')
    shutil.rmtree('./downloads/')

    
  elif CallbackQuery.data == "mute":
    CallbackQuery.edit_message_text("جار الكتم")
    aid = user_id
    cmd(f'''ffmpeg -i "{file_path}" -c copy -an "{mp4file}"''')
    with open(mp4file, 'rb') as f:
             bot.send_document(aid, f)
    cmd(f'''unlink "{mp4file}" ''')
    shutil.rmtree('./downloads/') 

  elif CallbackQuery.data == "speedy":
     CallbackQuery.edit_message_text(
             text = CHOOSE_UR_SPEED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_SPEED_MODE_BUTTONS)
        )

  elif CallbackQuery.data == "spd1":
    global spdratevid
    spdratevid = 0.8
    global spdrateaud
    spdrateaud = 1.25
    CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILESPED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS)
        )
  elif CallbackQuery.data == "spd2":
    spdratevid = 0.66666666666
    spdrateaud = 1.5
    CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILESPED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS)
        )
  elif CallbackQuery.data == "spd3":
    spdratevid = 0.57142857142
    spdrateaud = 1.75
    CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILESPED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS)
        )
  elif CallbackQuery.data == "spd4":
    spdratevid = 0.5
    spdrateaud = 2
    CallbackQuery.edit_message_text(
             text = CHOOSE_UR_FILESPED_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILESPED_MODE_BUTTONS)
        )
  elif CallbackQuery.data == "speedfileaud":
    CallbackQuery.edit_message_text("جار التسريع")
    aid = user_id
    cmd(f'''ffmpeg -i {file_path} -filter:a "atempo={spdrateaud}" -vn {mp3file} -y ''')
    with open(mp3file, 'rb') as f:
             bot.send_audio(aid, f)
    cmd(f'''unlink "{mp3file}" ''')
    shutil.rmtree('./downloads/') 

  elif CallbackQuery.data == "speedfilevid":
    CallbackQuery.edit_message_text("جار التسريع")
    aid = user_id
    cmd(f'''ffmpeg -i {file_path} -filter_complex "[0:v]setpts={spdratevid}*PTS[v];[0:a]atempo={spdrateaud}[a]" -map "[v]" -map "[a]" {mp4file} -y ''')
    with open(mp4file, 'rb') as f:
             bot.send_video(aid, f)
    cmd(f'''unlink "{mp4file}" ''')
    shutil.rmtree('./downloads/') 

  elif CallbackQuery.data == "audmerge":
    cmd(f'''mkdir mergy''')
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a "{mergdir}" -y ''')
    shutil.rmtree('./downloads/') 
    with open('list.txt','a') as f:
      f.write(f'''file '{mergdir}' \n''')
    CallbackQuery.edit_message_text(
             text = CHOOSE_UR_MERGE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_MERGE_BUTTONS))
  elif CallbackQuery.data == "mergenow":
    CallbackQuery.edit_message_text("جار الدمج") 
    aid = user_id  
    cmd(f'''ffmpeg -f concat -safe 0 -i list.txt "{mp3file}" -y ''')
    with open(mp3file, 'rb') as f:
         bot.send_audio(aid, f)
    cmd(f'''rm list.txt "{mp3file}" ''')
    shutil.rmtree('./downloads/')
    shutil.rmtree('./mergy/') 
  elif CallbackQuery.data == "splitty":
    CallbackQuery.edit_message_text("جار التقسيم") 
    aid = user_id 
    cmd(f'''ffmpeg -i "{file_path}" -q:a 0 -map a mod.mp3 -y''')
    cmd(f'mkdir parts')
    cmd(f'''ffmpeg -i "mod.mp3" -f segment -segment_time 300 -c copy "./parts/{nom}%09d.wav" -y''')
    dir_path = "./parts/"
    count = 0
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
                            count += 1
                            numbofitems=count
    if numbofitems<10 :
        
     coca=0
     while (coca < numbofitems): 
             pathy=f"./parts/{nom}00000000{coca}.wav"
             reso = f"{nom}00000000{coca}.mp3"
             cmd(f'''ffmpeg -i "{pathy}" -q:a 0 -map a "{reso}" -y''')
             with open(reso, 'rb') as f:
               bot.send_audio(aid, f)
             cmd(f'''rm "{reso}"''') 
             coca += 1 
    else :
     coca=0 
     while (coca < 10): 
             pathy=f"./parts/{nom}00000000{coca}.wav"
             reso = f"{nom}00000000{coca}.mp3"
             cmd(f'''ffmpeg -i "{pathy}" -q:a 0 -map a "{reso}" -y''')
             with open(reso, 'rb') as f:
               bot.send_audio(aid, f)
             cmd(f'''rm "{reso}"''') 
             coca += 1        
     coca=10
     while (coca < numbofitems ): 
             pathy=f"./parts/{nom}0000000{coca}.wav"
             reso = f"{nom}00000000{coca}.mp3"
             cmd(f'''ffmpeg -i "{pathy}" -q:a 0 -map a "{reso}" -y''')
             with open(reso, 'rb') as f:
               bot.send_audio(aid, f)
             cmd(f'''rm "{reso}"''') 
             coca += 1                                      
    shutil.rmtree('./downloads/')
    shutil.rmtree('./parts/') 
    cmd(f'''rm mod.mp3''')
    
  elif CallbackQuery.data == "OCR":
    try: 
      with open('final.txt', 'r') as fh:
        if os.stat('final.txt').st_size == 0: 
            pass
        else:
            CallbackQuery.edit_message_text("هناك تفريغ يتم الآن ") 
            return
    except FileNotFoundError: 
     pass  
    aid = user_id
    CallbackQuery.edit_message_text("جار التفريغ")
    lang_code = "ara"
    data_url = f"https://github.com/tesseract-ocr/tessdata/raw/main/{lang_code}.traineddata"
    dirs = r"/usr/share/tesseract-ocr/4.00/tessdata"
    path = os.path.join(dirs, f"{lang_code}.traineddata")
    data = requests.get(data_url, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
    open(path, 'wb').write(data.content)
    text = pytesseract.image_to_string(file_path, lang=f"{lang_code}")
    textspaced = re.sub(r'\r\n|\r|\n', ' ', text)
    file.reply(textspaced[:-1], quote=True, disable_web_page_preview=True)
    shutil.rmtree('./downloads/') 
  elif CallbackQuery.data == "pdfOCR":
    aid = user_id
    CallbackQuery.edit_message_text("جار التفريغ")
    cmd('mkdir temp')
    pdf = pdfium.PdfDocument(file_path)
    n_pages = len(pdf)
    for page_number in range(n_pages):
     page = pdf.get_page(page_number)
     pil_image = page.render_topil(
        scale=1,
        rotation=0,
        crop=(0, 0, 0, 0),
        colour=(255, 255, 255, 255),
        annotations=True,
        greyscale=False,
        optimise_mode=pdfium.OptimiseMode.NONE,
    )
     pil_image.save(f"./temp/image_{page_number+1}.png")
    shutil.rmtree('./downloads/') 
    count = 0
    for path in os.listdir("./temp/"):
                if os.path.isfile(os.path.join("./temp/", path)):
                            count += 1
                            numbofitems=count
    coca=1
    final = numbofitems 
    while (coca < final): 
     cmd(f'''sh textcleaner -g "./temp/image_{coca}.png" temp.png ''')
     lang_code = "ara"
     data_url = f"https://github.com/tesseract-ocr/tessdata/raw/main/{lang_code}.traineddata"
     dirs = r"/usr/share/tesseract-ocr/4.00/tessdata"
     path = os.path.join(dirs, f"{lang_code}.traineddata")
     data = requests.get(data_url, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
     open(path, 'wb').write(data.content)
     text = pytesseract.image_to_string(f"temp.png" , lang=f"{lang_code}")
     textspaced = re.sub(r'\r\n|\r|\n', ' ', text)
     with open("final.txt",'a') as f:
      f.write(f'''{textspaced} \n''')
     coca +=1
    cmd(f'''mv final.txt "{result}"''')
  with open(result, 'rb') as f:
         bot.send_document(aid, f)
  shutil.rmtree('./temp/') 
  cmd(f'''rm "{result}"''')








@bot.on_message(filters.private & filters.reply & filters.regex('/'))
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          endstart = message.text ;await message.delete()
          global strt_point
          global end_point
          strt, end = os.path.split(endstart);strt_point=strt 
          end_point = end
          await message.reply(
             text = CHOOSE_UR_FILETRIM_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILETRIM_MODE_BUTTONS)

        )
@bot.on_message(filters.private & filters.reply )
async def refunc(client,message):
   if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply)  :
          newname = message.text ;await message.delete()
          global newfile
          newfile = f"{newname}{ex}"
          cmd(f'''mv "{file_path}" "{newfile}"''')
          await message.reply(
             text = CHOOSE_UR_FILERENM_MODE,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_FILERENM_MODE_BUTTONS)

           )
        
bot.run()
