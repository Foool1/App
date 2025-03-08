import pytesseract
from PIL import Image
import os

def ocr_image(image_path):
    try:
        # Sprawdzenie czy plik istnieje
        if not os.path.exists(image_path):
            return "Plik nie istnieje!"

        # Otwarcie obrazu
        img = Image.open(image_path)

        # Konwersja obrazu na tekst
        text = pytesseract.image_to_string(img)

        return text

    except Exception as e:
        return f"Wystąpił błąd: {str(e)}"

def main():
    # Ścieżka do obrazu - zmień na swoją
    image_path = "input.png"

    # Wykonanie OCR
    result = ocr_image(image_path)

    # Wyświetlenie wyniku
    print("Rozpoznany tekst:")
    print(result)

    # Opcjonalnie zapis do pliku
    with open("wynik_ocr.txt", "w", encoding="utf-8") as file:
        file.write(result)

if __name__ == "__main__":
    main()