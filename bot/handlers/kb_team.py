import requests
from aiogram import Dispatcher, Router, types
from aiogram.filters import Command

dp = Dispatcher()

router = Router(name='kb-team')


@router.message(Command(commands=['kb-team']))
async def kb_team(message: types.Message):
    await message.answer(
        text='общая инфа, например kb-team list - <b>список</b>',
        parse_mode='html'
    )
    tokens = ['123', 'abc'] # get_tokens()
    msg = f'Актуальный список токенов:\n\n'
    li_items = [f'* {t}' for t in tokens]
    msg += f'{li_items}'
    await message.answer(msg, parse_mode='markdown')


#
# TODO: парсить аргументы
@router.message(Command(commands=['kb-team-list']))
async def kb_team(message: types.Message):
    await message.answer(text='Вас понял, выгружаю, это займет время...', parse_mode='html')
    tokens = get_tokens()
    msg = f'Актуальный список токенов:'
    li_items = [f'<li>{t}</li>' for t in tokens]
    msg += f'{li_items}'
    await message.answer(text=msg, parse_mode='html')


def get_tokens() -> list[str]:
    s = requests.Session()
    s.get('https://kb-team.club/?do=/module&bid=auth&act=submit&login=vlasov_37&password=G51505k5kinoboom')
    response = s.get('https://kb-team.club/?do=/module&bid=auth&act=mymac')
    return parse_html(response.content.decode()).split('\n')



def parse_html(html: str):
    """вытаскиваем html тег из ответа

    view-source:https://kb-team.club/?do=/module&bid=auth&act=mymac
    <textarea cols="22" rows="6" name="macs">
        32dd5dc621e6
        d887652f6e83
        40d0ac94f392
    </textarea>
    """

    s1 = '<textarea cols="22" rows="6" name="macs">'
    s2 = '</textarea>'
    start = html.find(s1)
    html_inner1 = html[start+len(s1):]
    html_inner_itog = html_inner1[:html_inner1.find(s2)]
    return html_inner_itog
