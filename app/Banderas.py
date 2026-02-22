#Codigo modularizado en este archivo
# Este archivo contiene la función para convertir el nombre de un país a bandera usando https://flagcdn.com/w40/{code}.png 

mapping = {
    # EUROPA
    "Spain": "es",
    "France": "fr",
    "Germany": "de",
    "Portugal": "pt",
    "Italy": "it",
    "Netherlands": "nl",
    "Belgium": "be",
    "England": "gb",
    "Scotland": "gb",
    "Wales": "gb",
    "Ireland": "ie",
    "Northern Ireland": "gb",
    "Greece": "gr",
    "Switzerland": "ch",
    "Austria": "at",
    "Denmark": "dk",
    "Norway": "no",
    "Sweden": "se",
    "Finland": "fi",
    "Poland": "pl",
    "Czech Republic": "cz",
    "Slovakia": "sk",
    "Slovenia": "si",
    "Croatia": "hr",
    "Bosnia and Herzegovina": "ba",
    "Serbia": "rs",
    "Montenegro": "me",
    "Albania": "al",
    "North Macedonia": "mk",
    "Hungary": "hu",
    "Romania": "ro",
    "Bulgaria": "bg",
    "Ukraine": "ua",
    "Russia": "ru",
    "Turkey": "tr",
    "Iceland": "is",

    # AMÉRICA
    "Argentina": "ar",
    "Brazil": "br",
    "Uruguay": "uy",
    "Chile": "cl",
    "Paraguay": "py",
    "Bolivia": "bo",
    "Peru": "pe",
    "Colombia": "co",
    "Venezuela": "ve",
    "Ecuador": "ec",
    "Mexico": "mx",
    "USA": "us",
    "Canada": "ca",
    "Costa Rica": "cr",
    "Honduras": "hn",
    "Panama": "pa",
    "Cuba": "cu",
    "Dominican Republic": "do",
    "Jamaica": "jm",

    # ÁFRICA (muy comunes en LaLiga)
    "Morocco": "ma",
    "Algeria": "dz",
    "Tunisia": "tn",
    "Senegal": "sn",
    "Nigeria": "ng",
    "Ghana": "gh",
    "Ivory Coast": "ci",
    "Cameroon": "cm",
    "Mali": "ml",
    "Guinea": "gn",
    "Angola": "ao",
    "South Africa": "za",

    # ASIA / OCEANÍA
    "Japan": "jp",
    "South Korea": "kr",
    "Australia": "au",
    "Iran": "ir",
    "Saudi Arabia": "sa",
    "Qatar": "qa",
    "United Arab Emirates": "ae",
    "China": "cn",

    # OTROS FRECUENTES
    "Luxembourg": "lu",
    "Georgia": "ge",
    "Armenia": "am",
    "Kosovo": "xk"
}

def country_to_code(country):
    if not country:
        return None

    code = mapping.get(country)

    if not code:
        code = country[:2].lower()

    return code