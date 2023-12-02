import os
import re
from pyrogram import Client, filters
import requests
import pytesseract
from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery , ForceReply
import shutil
import pypdfium2 as pdfium


bot = Client(
    "pdfserv5115",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6280972722:AAG3GrropPJhZvfjljtgppKeeXpfpBVZG4Y"
)
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    bot.send_message(message.chat.id, " السلام عليكم , أنا بوت تفريغ المستندات , فقط أرسل بي دي إف",disable_web_page_preview=True)

@bot.on_message(filters.private & filters.incoming & filters.document )
def _telegram_file(client, message):
  try: 
    with open('final.txt', 'r') as fh:
        if os.stat('final.txt').st_size == 0: 
            pass
        else:
            sent_message = message.reply_text('هناك عملية تتم الآن , انتظر فضلاً  ', quote=True)
            return
  except FileNotFoundError: 
    pass  
  sent_message = message.reply_text('جار التفريغ .. ', quote=True)    
  user_id = message.from_user.id 
  file = message.document
  file_path = message.download(file_name="./downloads/")
  filename = os.path.basename(file_path)
  nom,ex = os.path.splitext(filename)
  noim = f"{nom}.txt"
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
  cmd(f'''mv final.txt "{noim}"''')
  with open(noim, 'rb') as f:
         bot.send_document(user_id, f)
  shutil.rmtree('./temp/') 

                
bot.run()
