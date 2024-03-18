from aiogram import Bot,types,F
from .loader import dp
from .utils.notify_admins import on_startup_notify
from .utils.set_bot_commands import set_default_commands
from aiogram.enums import ParseMode
from .data import config
from aiogram.filters import CommandStart,Filter
from .keyboards.inline.user import confirm,commands
from .data.config import ADMINS
from .states.admin import NewsState
from aiogram.fsm.context import FSMContext
from ..models import News
from django.core.files import File
import os
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)


class AdminFilter(Filter):

    async def __call__(self, message: types.Message) -> bool:
        result = str(message.from_user.id) in ADMINS
        return result


@dp.message(CommandStart(),AdminFilter())
async def bot_start(message: types.Message):
    await message.answer(f"Hush keilib siz",reply_markup=commands)


@dp.callback_query(lambda call: call.data == 'news')
async def start_news(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer("Yangilik sarlavhasini kiriting\n🇺🇿 Lotinchada",reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(NewsState.titleuz)

@dp.message(NewsState.titleuz)
async def set_title(message:types.Message,state:FSMContext):
    await state.update_data({"titleuz":message.text})
    await message.answer("Yangilik sarlavhasini kiriting\n🇷🇺 Ruschada")
    await state.set_state(NewsState.titleru)

@dp.message(AdminFilter(),NewsState.titleru)
async def set_title(message:types.Message,state:FSMContext):
    await state.update_data({"titleru":message.text})
    await message.answer("Yangilik matnini kiriting\n🇺🇿 Lotinchada")
    await state.set_state(NewsState.descriptionuz)

@dp.message(AdminFilter(),NewsState.descriptionuz)
async def set_title(message:types.Message,state:FSMContext):
    await state.update_data({"descriptionuz":message.text})
    await message.answer("Yangilik matnini kiriting\n🇷🇺 Ruschada")
    await state.set_state(NewsState.descriptionru)

@dp.message(AdminFilter(),NewsState.descriptionru)
async def set_title(message:types.Message,state:FSMContext):
    await state.update_data({"descriptionru":message.text})
    await message.answer('Yangilik uchun fayl yuklang (rasm/video)')
    await state.set_state(NewsState.image)

@dp.message(AdminFilter(),NewsState.image,F.photo)
@dp.message(AdminFilter(),NewsState.image,F.document)
@dp.message(AdminFilter(),NewsState.image,F.video)
async def set_image(message:types.Message,state:FSMContext):
    data = await state.get_data()
    text = f"🇺🇿\n{data['titleuz']}\n{data['descriptionuz']}\n\n🇷🇺\n{data['titleru']}\n{data['descriptionru']}"
    if message.photo:
        file_id = message.photo[0].file_id
        await message.answer_photo(file_id,text)
    elif message.document:
        file_id = message.document.file_id        
        await message.answer_document(file_id,text)
    elif message.video:
        file_id = message.video.file_id
        await message.answer_video(file_id,caption=text)
    await state.update_data({"photo":file_id})
    await message.answer('Tasdiqlaysimi?',reply_markup=confirm)
    await state.set_state(NewsState.confirm)

@dp.callback_query(AdminFilter(),NewsState.confirm)
async def confirmation(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    if call.data == 'yes':
        data = await state.get_data()
        image = await bot.get_file(data['photo'])
        file = "app/bot/handlers/users/"+image.file_path.split('/')[-1]
        await bot.download_file(image.file_path,file)
        local_file = open(file, "rb")
        djangofile = File(local_file)
        obj = await News.objects.acreate(video = djangofile)
        await obj.translations.acreate(language_code='uz',title=data['titleuz'],description=data['descriptionuz'])
        await obj.translations.acreate(language_code='ru',title=data['titleru'],description=data['descriptionru'])
        local_file.close()
        os.remove(file)
        await call.message.answer('tasdiqlandi')
    await bot_start(call.message)
    await state.clear()
        



async def on_startup(dispatcher):
    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dispatcher)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dispatcher)


async def start():

    await dp.start_polling(bot, on_startup=on_startup)
