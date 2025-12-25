import subprocess
import sys
import os


def main():
    print("=== ДОБАВЛЕНИЕ КЛИНИЧЕСКОЙ РЕКОМЕНДАЦИИ ===")
    link = input(
        "Вставьте ссылку на клиническую рекомендацию (например, https://cr.minzdrav.gov.ru/view-cr/123_1):\n> "
    ).strip()

    if not link.startswith("https://cr.minzdrav.gov.ru/view-cr/"):
        print(
            "⚠️  Неверный формат ссылки!"
        )
        return

    try:
        result = subprocess.run(
            [sys.executable, "adtocsv2.py"], input=link, text=True, capture_output=True
        )
        if result.returncode == 0:
            print("\n✅ Рекомендация успешно добавлена в data/out.csv!")
            print(
                "Теперь перезапустите веб-приложение."
            )
        else:
            print("\n❌ Ошибка при добавлении:")
            print(result.stderr)
            if "not in dictionary" in result.stderr:
                print("\n❗ Найдены неизвестные коды МКБ-10.")
                print("Вы можете добавить их вручную — запустите: python massdict.py")
    except Exception as e:
        print(f"\n💥 Критическая ошибка: {e}")


if __name__ == "__main__":
    main()
