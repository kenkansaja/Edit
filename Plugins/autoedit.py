import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import autocaption
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


# =
usercaption_position = Config.CAPTION_POSITION
caption_position = usercaption_position.lower()
caption_text = Config.CAPTION_TEXT
channel.id = Config.CHANNEL_ID



@autocaption.on_message(filters.channel & (filters.document | filters.video | filters.audio ) & ~filters.edited, group=-1)
async def editing(bot, message):
      try:
          if ( message.document or message.video or message.audio ):
             file_caption = f"**{message.caption}**"
             link = f"https://t.me/{chat_id}"
             markup = InlineKeyboardMarkup([[InlineKeyboardButton("📩 CHANNEL 📩", url=f'https://t.me{link}')]])
      except:
          pass
      try:
          if caption_position == "top":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = caption_text + "\n" + file_caption,
                 parse_mode = "markdown"
                 link = f"https://t.me/{chat_id}"
                 markup = InlineKeyboardMarkup([[InlineKeyboardButton("📩 CHANNEL 📩", url=f'https://t.me{link}')]])
      
             )
          elif caption_position == "bottom":
             await bot.edit_message_caption(
                 chat_id = message.chat.id, 
                 message_id = message.message_id,
                 caption = file_caption + "\n" + caption_text,
                 parse_mode = "markdown"
                 link = f"https://t.me/{chat_id}"
                 markup = InlineKeyboardMarkup([[InlineKeyboardButton("📩 CHANNEL 📩", url=f'https://t.me{link}')]])
      

             )
          elif caption_position == "nil":
             await bot.edit_message_caption(
                 chat_id = message.chat.id,
                 message_id = message.message_id,
                 caption = caption_text, 
                 parse_mode = "markdown"
                 link = f"https://t.me/{chat_id}"
                 markup = InlineKeyboardMarkup([[InlineKeyboardButton("📩 CHANNEL 📩", url=f'https://t.me{link}')]])link = f"https://t.me/{chat_id}"
             
             ) 
      except:
          pass
              
                   
      
