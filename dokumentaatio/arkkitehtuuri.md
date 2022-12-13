# Arkkitehtuuri

## Rakenne
Koodin rakenne on seuraava:

![Pakkausrakenne](./kuvat/pakkauskaavio.png)

## Sovelluslogiikka

Sovelluslogiikan muodostaa pitkälti luokat [DailyQuestionsApp](https://github.com/codePercidae/ot-harjoitustyo/blob/main/src/daily_questions_app.py) ja [QuestionRepository](https://github.com/codePercidae/ot-harjoitustyo/blob/main/src/question_repository.py).

```mermaid
classDiagram
	DailyQuestionsApp "1" --> "1" QuestionRepository
	class DailyQuestionsApp{
		repository
		}
	class QuestionRepository{
		connection
		}
```
## Päätoiminnallisuudet
Kuvataan ohjelman päätoiminnallisuuksia sekvenssikaavioiden avulla.

### Uuden kysymyksen luominen

```mermaid
sequenceDiagram
	actor User
	User->>Interface: Insert 'New question'
	Interface->>DailyQuestionApp: new_question('New question')
	DailyQuestionApp->>QuestionRepository: repository.add_question('New question')
	QuestionRepository-->>DailyQuestionApp: True
	DailyQuestionApp-->>Interface: True
	Interface-->>User: "Question added!"

```
