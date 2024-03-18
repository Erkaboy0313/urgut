from aiogram import types
from ...data.config import ADMINS
from ...loader import dp
from ...main import bot
from ...states.admin import NewsState
from aiogram.fsm.context import FSMContext
from aiogram.enums.content_type import ContentType
from ...keyboards.inline.user import confirm,commands
from ....models import News
from django.core.files import File

# from app.models import News

# from app.models import News


@dp.callback_query_handler(lambda call: call.data == 'news',chat_id =ADMINS)
async def start_news(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Yangilik sarlavhasini kiriting\n🇺🇿 Lotinchada",reply_markup=types.ReplyKeyboardRemove())
    await NewsState.titleuz.set()

@dp.message_handler(chat_id =ADMINS,state=NewsState.titleuz)
async def set_title(message:types.Message,state:FSMContext):
    await state.update_data({"titleuz":message.text})
    await message.answer("Yangilik sarlavhasini kiriting\n🇷🇺 Ruschada")
    await NewsState.titleru.set()

@dp.message_handler(chat_id =ADMINS,state=NewsState.titleru)
async def set_title(message:types.Message,state:FSMContext):
    await state.update_data({"titleru":message.text})
    await message.answer("Yangilik matnini kiriting\n🇺🇿 Lotinchada")
    await NewsState.descriptionuz.set()

@dp.message_handler(chat_id =ADMINS,state=NewsState.descriptionuz)
async def set_title(message:types.Message,state:FSMContext):
    await state.update_data({"descriptionuz":message.text})
    await message.answer("Yangilik matnini kiriting\n🇷🇺 Ruschada")
    await NewsState.descriptionru.set()

@dp.message_handler(chat_id =ADMINS,state=NewsState.descriptionru)
async def set_title(message:types.Message,state:FSMContext):
    await state.update_data({"descriptionru":message.text})
    await message.answer('Yangilik uchun rasm yuklang')
    await NewsState.image.set()

@dp.message_handler(chat_id =ADMINS,state=NewsState.image,content_types=ContentType.PHOTO)
@dp.message_handler(chat_id =ADMINS,state=NewsState.image,content_types=ContentType.DOCUMENT)
async def set_image(message:types.Message,state:FSMContext):
    data = await state.get_data()
    text = f"🇺🇿\n{data['titleuz']}\n{data['descriptionuz']}\n\n🇷🇺\n{data['titleru']}\n{data['descriptionru']}"
    if message.photo:
        file_id = message.photo[0].file_id
        await message.answer_photo(file_id,text)
    elif message.document:
        file_id = message.document.file_id        
        await message.answer_document(file_id,text)
    await state.update_data({"photo":file_id})
    await message.answer('Tasdiqlaysimi?',reply_markup=confirm)
    await NewsState.confirm.set()

@dp.callback_query_handler(chat_id =ADMINS,state=NewsState.confirm)
async def confirmation(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    if call.data == 'yes':
        data = await state.get_data()
        image = await bot.get_file(data['photo'])
        file = "app/bot/handlers/users/"+image.file_path.split('/')[-1]
        await bot.download_file(image.file_path,file)
        local_file = open(file, "rb")
        djangofile = File(local_file)
        obj = await News.objects.acreate(image = djangofile)
        await obj.translations.acreate(language_code='uz',title=data['titleuz'],description=data['descriptionuz'])
        await obj.translations.acreate(language_code='ru',title=data['titleru'],description=data['descriptionru'])
        local_file.close()
        await call.message.answer('tasdiqlandi')
    await bot_start(call.message)
    await state.finish()
        

