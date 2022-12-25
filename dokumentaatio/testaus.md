# Testausdokumentti
Sovelluksen testausta on toteutettu automatisoiduilla yksikkötesteillä ja manuaalisella järjestelmätestauksella.

## Yksikkötestit
### Sovelluslogiikka
Sovelluslogiikasta vastaavaa luokkaa DailyQuestionsApp testataan TestDailyQuestionsApp luokalla. Luokalle annetaan testitilannetta varten oma repositorio.

### Repositorio-testit
Tiedon tallennuksesta vastaavaa luokkaa QuestionRepository testataaan TestQuestionRepository luokalla. Testit toteutetaan erillisille testeille
omistetulla tietokantatiedostolle joka on määritelty .env.tests tiedostossa.

