import os
import re
from pyrogram import Client, filters
import requests
import pytesseract
from os import system as cmd
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery , ForceReply
from pdf2image import convert_from_path
import shutil
bot = Client(
    "pdfserv5115",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="6448510263:AAFDxuNH03euMQmtxyiD_ZTKcIxzjIcDbmM"
)
@bot.on_message(filters.private & filters.incoming & filters.document )
def _telegram_file(client, message):
  user_id = message.from_user.id 
  file = message.document
  file_path = message.download(file_name="./downloads/")
  filename = os.path.basename(file_path)
  nom,ex = os.path.splitext(filename)
  final = f"{nom}.txt"
  cmd('mkdir temp')
  pdf_images = convert_from_path(file_path)
  for idx in range(len(pdf_images)):
    pdf_images[idx].save('./temp/pdf_page_'+ str(idx+1) +'.png', 'PNG')
  shutil.rmtree('./downloads/') 
  count = 0
  for path in os.listdir("./temp/"):
                if os.path.isfile(os.path.join("./temp/", path)):
                            count += 1
                            numbofitems=count
  coca=1
  final = numbofitems 
  while (coca < final): 
    cmd(f'''sh textcleaner -g "./temp/pdf_page_{coca}.png" temp.png ''')
    lang_code = "ara"
    data_url = f"https://github.com/tesseract-ocr/tessdata/raw/main/{lang_code}.traineddata"
    dirs = r"/usr/share/tesseract-ocr/4.00/tessdata"
    path = os.path.join(dirs, f"{lang_code}.traineddata")
    data = requests.get(data_url, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0'})
    open(path, 'wb').write(data.content)
    text = pytesseract.image_to_string(f"temp.png" , lang=f"{lang_code}")
    textspaced = re.sub(r'\r\n|\r|\n', ' ', text)
    with open(final,'a') as f:
      f.write(f'''{textspaced} \n''')
    coca +=1
  with open(final, 'rb') as f:
         bot.send_document(user_id, f)
  shutil.rmtree('./temp/') 

                
bot.run()
