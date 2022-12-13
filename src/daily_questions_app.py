from question_repository import QuestionRepository
from ui.grade_interface import GradeInterface
from ui.interface import Interface
from ui.status_interface import StatusInterface

class DailyQuestionsApp:

    """Ohjelman pääluokka joka vastaa logiikasta.
    
    Attributes: 
        repository: Linkki tietokannan hallintaan
        main_gui: Käyttöliittymän alkunäkymä
        grade_gui: Kysymysten arvioinnin näkymä
        status_gui: Kysymysten vastauksien tarkastelun näkymä
    
    """

    def __init__(self) -> None:
        """Luokan konstruktori joka luo uuden instanssin ohjelmasta."""

        self.repository = QuestionRepository()

    def start_gui(self):
        """Luo ja käynnistää aloitusnäkymän."""

        self.main_gui = Interface(self)
        self.main_gui.activate()

    def new_question(self, question):
        """Välittää tietokannan hallinalle uuden kysymyksen.
        
        Jos kysymys on 0 merkkiä pitkä tai aktiivisia kysymykisä on jo 5, palauttaa False
        
        Muutoin riippuen onnistuuko kysymyksen talletus, palauttaa False tai True
        """

        if len(question) == 0 or len(self.transmit_questions()) == 5:
            return False
        return self.repository.add_question(question)

    def grade_window(self):
        """Luo ja käynnistää kysymysten arviointiin tarvittavan ikkunan."""

        self.main_gui.kill()
        self.grade_gui = GradeInterface(self)
        self.grade_gui.activate()

    def transmit_questions(self):
        """Välittää kysymykset tietokannan hallinnalta."""

        return self.repository.get_questions()

    def transmit_answers(self, question_id):
        """Välittää kysymyksen vastaukset tietokannan hallinnalta.
        
        Args:
            question_id: kysymyksen identifioiva luku
        """

        return self.repository.get_values(question_id)

    def grade_question(self, question_id, grade):
        """Välittää kysymyksen uuden vastauksen tietokannan hallinnalle.
        
        Jos vastaus ei ole luku välillä 1-10, palauttaa False, muutoin True
        
        Args: 
            question_id: kysymyksen identifioiva luku
            grade: uusi vastaus
        """

        if grade in [str(i) for i in range(1, 11)]:
            self.repository.new_grade(question_id, grade)
            return True
        return False

    def archive(self, question_id):
        """Arkistoi aktiivisen kysymyksen.
        
        Args:
            question_id: kysymyksen identifioiva luku
        """

        self.repository.deactive(question_id)

    def status_window(self):
        """Sulkee aloitusikkunan ja avaa tarkastelunäkymän."""

        self.main_gui.kill()
        self.status_gui = StatusInterface(self)

    def kill_status_gui(self):
        """Sulkee tarskastelunäkymän ja avaa aloitusikkunan."""
        self.status_gui.kill()
        self.start_gui()

    def kill_grade_gui(self):
        """Sulkee arvostelunäkymän ja avaa aloitusikkunan."""

        self.grade_gui.kill()
        self.start_gui()

    def empty_database(self):
        """Antaa tietokannan hallinalle käskyn tyhjentää tietokanta."""

        self.repository.initialize_database()
