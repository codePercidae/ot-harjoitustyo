#Daily Questions -sovellus

Sovelluksen avulla käyttäjä pystyy pitämään kirjaa omista elämäntapamuutoksistaan ja arvioimaan niiden edistymistä.

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/codePercidae/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/codePercidae/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/codePercidae/ot-harjoitustyo/blob/main/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

