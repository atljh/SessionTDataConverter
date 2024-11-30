import subprocess


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

if __name__ == "__main__":
    try:
        run_main_exe()
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        input("Для завершения работы нажмите Enter.")