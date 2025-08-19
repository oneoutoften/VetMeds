from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from app.services.drug_service import drug_service

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        'VetMeds поможет найти информацию о ветеринарных препаратах.\n'
        'Просто напишите название препарата или активного вещества.'
    )

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Help info fill later')

@router.message(F.text)
async def handle_drug_search(message: Message):
    search_term = message.text.strip()

    status_msg = await message.answer('Ищу информацию...')

    try:
        drugs = await drug_service.search_drug(search_term)
        response = await drug_service.format_drug_response(drugs)
        await message.answer(response, parse_mode='HTML')
    except Exception as e:
        await message.answer('Произошла ошибка при поиске. Попробуйте позже.')

    await status_msg.delete()