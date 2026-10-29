import shutil
import winreg, os
from pathlib import Path

# Список папок для копирования
EFFECTS_TO_DEPLOY = [
    "Random_Pack",
]

# Спрашиваем у Windows реальный путь к Документам текущего пользователя
with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders") as key:
    docs_path = Path(os.path.expandvars(winreg.QueryValueEx(key, "Personal")[0]))

DEST_ROOT = docs_path / "WhirlwindFX" / "Effects"
SOURCE_ROOT = Path(__file__).parent / "Effects"


def deploy():
    print("=" * 50)
    print("СИНХРОНИЗАЦИЯ ЭФФЕКТОВ В SIGNALRGB")
    print("=" * 50)

    for folder in EFFECTS_TO_DEPLOY:
        src = SOURCE_ROOT / folder
        dst = DEST_ROOT / folder

        if not src.exists():
            print(f"[!] Ошибка: Папка не найдена в проекте: {src}")
            continue

        print(f"[+] Копирование: {folder} -> SignalRGB...")

        # Создаем папку назначения, если её ещё нет (не трогая атрибуты OneDrive)
        dst.mkdir(parents=True, exist_ok=True)

        try:
            # Копируем только файлы внутри, не ломая системные флаги OneDrive
            for item in src.rglob("*"):
                relative_path = item.relative_to(src)
                target_path = dst / relative_path

                if item.is_dir():
                    target_path.mkdir(exist_ok=True)
                else:
                    # shutil.copy копирует только данные без перезаписи служебных метаданных OneDrive
                    shutil.copy(item, target_path)

            print(f"[OK] Успешно синхронизировано: {dst}")
        except Exception as e:
            print(f"[!] Ошибка копирования: {e}")

    print("-" * 50)
    print("Готово!")


if __name__ == "__main__":
    deploy()