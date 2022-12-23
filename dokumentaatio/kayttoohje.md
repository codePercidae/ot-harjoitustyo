# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/ohjelmistotekniikka-hy/python-todo-app/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Konfigurointi
Tallennukseen käytettävän tiedoston nimeä voi konfiguroida .env tiedostossa jonka rakenne on seuraava:
```
DATABASE_FILE=database.sqlite
```

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Aloitusnäkymä
Sovellus aukeaa näkymään jossa käyttäjä voi lisätä uuden kysymyksen.
Uuden kysymyksen saa tallennettua painamalla _add question_ painiketta.
Toistaiseksi aktiivisten kysymysten määrä on rajattu viiteen kysymykseen.

Käyttäjä voi siirtyä arvioimaan kysymyksiä painamalla _start grading_ (ks arviointinäkymä)

Käyttäjä voi siirtyä katsomaan aikaisempia vastauksia painamalla _question status_ (ks Aikaisempien vastausten katselu)

Aloitusnäkymän _Settings_ menusta on mahdollista tyhjentää kaikki kysymykset ja vastaukset painamalla _empty data_ 

## Arviointinäkymä
Arvioinnin saa aloitettua painamalla _start_. Jokaiselle kysymykselle tulee antaa arvosana väliltä 1-10  ja kun
käyttäjä painaa _Submit grade_ vastaus tallentuu ja käyttäjä saa seuraavan kysymyksen arvioitavaksi.

Kun kaikki kysymykset on arvioitu, paina _exit_ palataksesi aloitusnäkymään.

## Aikaisempien vastausten katselu
Käyttäjä näkee kysymykset ja viimeiset 7 niille annettua vastausta.

Käyttäjä voi arkistoida kunkin kysymyksen painamalla _archive question_ kysymyksen alapuolella.

Aloitusnäkymään pääsee painamalla _return to main screen_.
