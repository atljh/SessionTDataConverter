import json
import glob
import time
import asyncio
import subprocess

from telethon import TelegramClient
from telethon.errors import UserDeactivatedBanError, UserBannedInChannelError, UserDeactivatedError
from opentele.td import TDesktop
from opentele.api import UseCurrentSession, TFileNotFound


def run_main_exe():
    try:
        subprocess.run(["dll.exe"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении: {e}")
    except FileNotFoundError:
        print("Файл dll.exe не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        input("Для завершения работы нажмите Enter.")

async def main():
    tdatas = glob.glob('tdatas/*')
    for tdata in tdatas:
        try:
            tdesk = TDesktop(tdata)
            assert tdesk.isLoaded()
            client = await TelegramClient.FromTDesktop(tdesk, flag=UseCurrentSession, timeout=10, receive_updates=True)
            await client.connect()
            me = await client.get_me()
            phone = me.phone
            first_name = me.first_name
            last_name = me.last_name
            username = me.username
            await client.disconnect()
            client = await tdesk.ToTelethon(session=f'sessions/{phone}.session', flag=UseCurrentSession)
            await client.connect()
            session = await client.GetCurrentSession()
            await client.disconnect()

            with open(f'sessions/{phone}.json', 'w', encoding='utf-8') as outfile:
                json.dump({
                    'session_file': phone,
                    'phone': phone,
                    'register_time': round(time.mktime(session.date_created.timetuple())),
                    'app_id': session.api_id,
                    'app_hash': str(me.access_hash),
                    'sdk': session.system_version,
                    'app_version': session.app_version,
                    'device': session.device_model,
                    'last_check_time': round(time.mktime(session.date_active.timetuple())),
                    'first_name': first_name,
                    'last_name': last_name,
                    'username': username,
                    'lang_pack': me.lang_code,
                    'system_lang_pack': 'en-US'
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

def show_menu():
    print("Выберите, что хотите сделать:")
    print("1. Конвертировать Session в Tdata")
    print("2. Конвертировать Tdata в Session")

    choice = input("Введите 1 или 2: ")
    
    if choice == "1":
        run_main_exe()
    elif choice == "2":
        asyncio.run(main())
    else:
        print("Неправильный выбор.")
        input("Для завершения работы нажмите Enter.")

if __name__ == "__main__":
    try:
        show_menu() 
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        input("Для завершения работы нажмите Enter.")
