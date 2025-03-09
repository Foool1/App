# App

## Opis
App to wszechstronna aplikacja oferująca zestaw przydatnych narzędzi codziennego użytku, takich jak generator haseł, minutnik, narzędzie do kodowania QR, prognoza pogody oraz OCR. 

## Funkcje

- **Password Generator**: Prosty generator haseł.
- **Timer**: Minutnik oraz stoper.
- **QRCoder**: Encoder i decoder kodów QR.
- **Weather**: Aktualna pogoda w danym mieście.
- **OCR**: Wycinanie tekstu ze zdjęcia.

## Wymagania

- Docker

## Instalacja

1. **Klonowanie repozytorium**:

   ```bash
   git clone https://github.com/Foool1/App.git
   cd App/
   ```

2. Użycie Dockera:

Uruchomienie aplikacji w kontenerze Docker:

```bash
docker-compose up --build
```

Aplikacja udostępnia interaktywną dokumentację API za pomocą Swaggera. Aby zapoznać się z pełną dokumentacją, otwórz w przeglądarce.
```bash
http://127.0.0.1:8000/
```
