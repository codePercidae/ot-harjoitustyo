# Arkkitehtuuri

## Sovelluslogiikka

```mermaid
classDiagram
	DailyQuestionsApp "1" -> "1" QuestionRepository
	class DailyQuestionsApp{
		repository
		}
	class QuestionRepository{
		connection
		}
```
