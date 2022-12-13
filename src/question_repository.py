from datetime import date
from sqlite3 import OperationalError
from database_connection import get_database_connection
from initialize_database import init_database


class QuestionRepository:

    """Luokka tietokannan hallinnoinnille.
    
    Attributes:
        connection: connection olento jolla ollaan yhteydessä tietokantaan
    """

    def __init__(self) -> None:
        """Luokan konstruktori, joka määrittelee luokalle connection olion."""

        self.connection = get_database_connection()

    def add_question(self, question):
        """Lisää kysymyksen tietokantaan, jos lisäys onnistuu palauttaa True, muutoin False.
        
        Kysymyksen lisääminen tapahtuu ensiksi lisäämällä kysymys Questions tauluun, jossa sille
        määritellään yksilöllinen id. Tämän jälkeen luodaan uusi taulu nimellä Question_'id', jossa id on
        Questions taulun määrittelemä yksilöivä luku.

        Questions_id taululla on rivit:
            id: rivin yksilöivä luku
            date: päivä jona vastaus on annettu
            grade: arvosana jonka käyttäjä on antanut
        """

        cursor = self.connection.cursor()
        try:
            cursor.execute(
                f"INSERT INTO Questions (question, active) VALUES ('{question}', TRUE)")
            self.connection.commit()
            question_id = cursor.execute(
                f"SELECT * FROM Questions WHERE question='{question}'").fetchone()[0]
            cursor.execute(
                f"""CREATE TABLE Question_{question_id}
                (id INTEGER PRIMARY KEY, date DATE, grade INTEGER)""")
            self.connection.commit()
            return True
        except OperationalError:
            return False

    def get_questions(self):
        """Luo tupleista koostuvan listan aktiivisista kysymyksistä ja palauttaa sen.
        
        Lista on muotoa [(id, question)]
        """

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Questions where active=TRUE")
        rows = cursor.fetchall()
        return [(row["id"], row["question"]) for row in rows]

    def deactive(self, question_id):
        """Arkistoi kysymyksen, eli muuttaa Questions taulusta kysymyksen active sarakkeen tilaan False.
        
        Args:
            question_id: kysymyksen yskilöivä luku
        """

        cursor = self.connection.cursor()
        cursor.execute(
            f"UPDATE Questions SET active=FALSE WHERE id = {question_id}")
        self.connection.commit()

    def new_grade(self, question_id, grade):
        """Luo uuden rivin kysymykseen yhdistettyyn tauluun ja asettaa sinne nykyisen päivämäärän,
        sekä käyttäjän antaman arvosanan.
        
        Args:
            question_id: kysymyksen yksilöivä luku
            grade:käyttäjän antama arvosana
        """

        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO Question_{question_id} (date, grade) VALUES ({date.today()}, {grade})")
        self.connection.commit()

    def get_values(self, question_id):
        """Palauttaa kysymykseen yhdistetystä taululsta 7 viimeisintä arvosanaa listana.
        
        Args:
            question_id: kysymyksen yksilöivä luku
        """

        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM Question_{question_id}")
        rows = cursor.fetchmany(7)
        return [row["grade"] for row in rows]

    def initialize_database(self):
        """Tyhjentää ja alustaa tietokannan"""
        
        init_database()
