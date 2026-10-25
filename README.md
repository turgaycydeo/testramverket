# Läslistan – testautomatisering

Examination i kursen Testautomatisering och testverktyg (TAP VT26D).

Projektet testar webbsidan [Läslistan](https://tap-vt26-testautomatisering.github.io/exam/) med Python, pytest, behave och Playwright.

## Vad har testats?

### Backend (TDD, pytest)
Python-klasser som hanterar listan med böcker, i `src/`:

- `book_store.py` – `BookStore` med `addBook(author, title)` och `toggleFavorite(book_id)`
- `fav_books.py` – `FavoriteBooks` med `add(book)` och `remove(book)`

| Testtyp | Mapp | Vad testas |
|---|---|---|
| Enhetstest | `tests/unit/` | Varje klass för sig. I testerna av `BookStore` är `FavoriteBooks` utbytt mot en mock (pytest-mock). |
| Integrationstest | `tests/integration/` | `BookStore` och `FavoriteBooks` tillsammans, utan mockning. |

Exempel på vad som testas: att nya böcker får id = högsta id + 1, att titel och författare måste anges, att favoritmarkering växlar vid varje klick och att favoritlistan alltid stämmer med de markerade böckerna.

### Frontend (BDD, behave + Playwright)
User stories finns i [STORIES.md](STORIES.md). Varje story har en feature-fil i `src/features/`:

| Feature | Vad testas |
|---|---|
| `navigation.feature` | Navigering mellan alla vyer, vald vy är inaktiv, rätt innehåll visas |
| `catalog.feature` | Katalogens böcker, hjärtmarkera, ta bort markering, klicka flera gånger |
| `add_book.feature` | Formulärets knapp aktiv/inaktiv, formuläret töms, ny bok visas i katalogen |
| `favorites.feature` | Mina böcker: tomt meddelande, listan följer markeringarna |
| `statistics.feature` | Antal böcker och antal hjärtmarkerade böcker |

Testerna använder designmönstret **Page Object** (`src/features/pages/`), **Scenario Outline** och appens `data-testid`-attribut.

## Projektstruktur

```text
├─ .github/workflows/python_ci.yml   CI: flake8, pytest och behave vid push till main
├─ src/
│  ├─ book.py, book_store.py, fav_books.py, initial_books.py
│  └─ features/
│     ├─ *.feature                   en feature-fil per user story
│     ├─ environment.py              startar Playwright (headless)
│     ├─ pages/                      Page Object för varje vy
│     └─ steps/                      step-filer
├─ tests/
│  ├─ unit/
│  └─ integration/
├─ conftest.py                       gemensamma fixtures
├─ pytest.ini                        markers: unit, integration
├─ behave.ini
├─ setup.cfg                         inställningar för flake8
├─ README.md, STORIES.md, ANSWERS.md
└─ requirements.txt
```

## Starta projektet

Kräver Python 3.13 eller senare.

1. Klona repot. PyCharm: File → Project from Version Control.
2. Skapa ett virtual environment och installera paketen (i PyCharm sker detta automatiskt från `requirements.txt`):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # macOS/Linux
   pip install -r requirements.txt
   ```
3. Första gången: installera webbläsaren för Playwright:
   ```bash
   playwright install chromium
   ```

## Köra testerna

Alla kommandon körs i projektets rotmapp.

```bash
pytest                    # alla enhets- och integrationstester
pytest -m unit            # bara enhetstester
pytest -m integration     # bara integrationstester
behave                    # alla E2E-tester (headless)
behave -D headless=false  # E2E-tester med synlig webbläsare
flake8 src tests conftest.py
```

## CI

GitHub Actions kör flake8, enhetstester, integrationstester och E2E-tester (headless Chromium) vid varje push och pull request till `main`.
