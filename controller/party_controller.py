from model.mapping.party import Party
from model.store import Store
from exceptions import ResourceNotFound, Conflict


class PartyController:
    """
    party create / update.
    For update, create PartyController and feed the controller with fom_party function
    example:
        party = store.party().get(...)
        controller = PartyController(store)
        controller.from_party(party)
        controller.set_name("updated_name")
        controller.register()
    """

    def __init__(self, store: Store):
        self._store = store
        self._id = None
        self._name = None
        self._price = None
        self._location = None
        self._date = None
        self._grade = None
        self._theme = None
        self._state = None
        self._total_place = None
        self._creator_id = None

    def from_party(self, party: Party):
        self._id = party.id
        self._name = party.name
        self._price = party.price
        self._location = party.location
        self._theme = party.theme
        self._state = party.state
        self._grade = party.grade
        self._creator_id = party.creator_id
        self._date = party.date
        self._total_place = party.total_place

    def set_name(self, name):
        # check name not exists
        if self._name != name:
            try:
                self._store.party().get_by_name(name)
                raise Conflict("Party %s existe déjà" % name)
            except ResourceNotFound:
                self._name = name
    
    def get_name(self):
        return self._name

    def set_location(self, location):
        self._location = location

    def get_location(self):
        return self._location

    def set_creator_id(self, creator_id):
        self._creator_id = creator_id

    def get_creator_id(self):
        return self._creator_id

    def set_total_place(self, total_place):
        self._total_place = total_place

    def get_total_place(self):
        return self._total_place

    def set_date(self, date):
        self._date = date

    def get_date(self):
        return self._date

    def set_theme(self, theme):
        self._theme = theme

    def get_theme(self):
        return self._theme

    

    def set_price(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_grade(self, grade):
        self._grade = grade

    def get_grade(self):
        return self._grade

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def register(self):
        party = Party(id=self._id,
                          name=self._name,
                          location=self._location,
                          date=self._date,
                          creator_id=self._creator_id,
                          total_place=self._total_place,
                          theme=self._theme,
                          price=self._price,
                          grade=self._grade,
                          state=self._state)
        if self._id is None:
            self._store.party().create(party)
            self._id = party.id
        else:
            self._store.party().update(party)
        return party

