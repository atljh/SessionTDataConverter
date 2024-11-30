import os
import sys

import time
import glob
import json
import requests
import asyncio
import subprocess

from telethon import TelegramClient
from telethon.errors import UserDeactivatedBanError, UserBannedInChannelError, UserDeactivatedError, SessionPasswordNeededError
from opentele.td import TDesktop
from opentele.api import UseCurrentSession, TFileNotFound, API
from opentele.tl import TelegramClient
from telethon.errors import UserDeactivatedBanError, UserBannedInChannelError, UserDeactivatedError


async def main():
    tdatas = glob.glob('tdatas/*')
    for tdata in tdatas:
        try:
            tdesk = TDesktop(tdata)
            assert tdesk.isLoaded()
            tdesk = TDesktop(tdata)
            client = await TelegramClient.FromTDesktop(tdesk, flag=UseCurrentSession, timeout=10, receive_updates=True)
            await client.connect()
            me = await client.get_me()
            print(me)
            phone = me.phone
            first_name = me.first_name
            last_name = me.last_name
            username = me.username
            is_premiun = me.premium
            await client.disconnect()
            client = await tdesk.ToTelethon(session=f'sessions/{phone}.session', flag=UseCurrentSession)
            await client.connect()
            session = await client.GetCurrentSession()
            await client.disconnect()
            with open(f'sessions/{phone}.json', 'w', encoding='utf-8') as outfile:
                json.dump({
                    'app_id': session.api_id,
                    'app_hash': str(me.access_hash),
                    'device': session.device_model,
                    'sdk': session.system_version,
                    'app_version': session.app_version,
                    'system_lang_pack': 'en',
                    'system_lang_code': 'en',
                    'lang_pack': me.lang_code,
                    'lang_code': "en",
                    "twoFA": None,
                    "role": "",
                    "id": None,
                    "phone": phone,
                    "username": username,
                    "date_of_birth": None,
                    "date_of_birth_integrity": None, 
                    "is_premium": is_premiun,
                    "has_profile_pic": False,
                    "spamblock": None, 
                    "register_time": round(time.mktime(session.date_created.timetuple())),
                    "last_check_time": round(time.mktime(session.date_active.timetuple())),
                    "avatar": None, 
                    "first_name": first_name,
                    "last_name": last_name,
                    "sex": None,
                    "proxy": None,
                    "ipv6": False, 
                    'session_file': ""
                }, outfile, ensure_ascii=False)


            print(f'Аккаунт {tdata} успешно сконвертирован в {phone}')

        except UserDeactivatedBanError:
            print('Аккаунт забанен')
        except UserBannedInChannelError:
            print(f'Аккаунт забанен в канале - {tdata}')
        except UserDeactivatedError:
            print(f'Аккаунт деактивирован - {tdata}')
        except TFileNotFound:
            print(f'Не удалось открыть аккаунт {tdata}')
        except Exception as e:
            print(f'Ошибка конвертации аккаунта {tdata}\n\n{e}')
        finally:
            continue
        
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
    finally:
        input("Для завершения работы нажмите Enter.")

