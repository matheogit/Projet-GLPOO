from view.view import View
from model.store import Store

from controller.party_controller import PartyController
from view.common import Common
from exceptions import Conflict, ResourceNotFound
from model.mapping.party import Party


class PartyView(View):
    """
    Creation party view
    """

    def __init__(self, store: Store):
        self._common = Common()
        self._store = store

    def show(self):
        raise NotImplementedError()

    def ask_party(self):
        name = self._common.ask_name(key_name="name")
        try:
            party = self._store.party().get_by_name(name)
            return party
        except ResourceNotFound:
            print("Party %s introuvable")
            return None

    def formular(self, party: Party = None):
        # Show subscription formular
        party_controller = PartyController(self._store)
        if party:
            print("Update party")
            party_controller.from_party(party)

        while True:
            name = self._common.ask_name(key_name="name", default=party_controller.get_name())
            try:
                party_controller.set_name(name)
                break
            except Conflict as e:
                print("/!\\ %s" % str(e))
        location = self._common.ask(key_name="location", default=party_controller.get_location())
        party_controller.set_location(location)
        default_value = None
        if party_controller.get_price() is not None:
            default_value = str(party_controller.get_price())
        price = self._common.ask(key_name="price", default=default_value)
        party_controller.set_price(float(price))
        default_value = None
        if party_controller.get_number() is not None:
            default_value = str(party_controller.get_number())
        number = self._common.ask(key_name="number", regex="^\d+$",
                                  default=default_value)
        party_controller.set_number(int(number))
        party_type = self._common.ask_name(key_name="party_type",
                                             default=party_controller.get_party_type())
        party_controller.set_party_type(party_type=party_type)

        party_controller.register()


class AddPartyView(PartyView):

    def show(self):
        print("Add new party")
        print()
        self.formular()


class UpdatePartyView(PartyView):

    def show(self):
        print("Update party")
        party = self.ask_party()
        if party is None:
            return
        self.formular(party=party)


class DeletePartyView(PartyView):

    def show(self):
        print("Delete party")
        party = self.ask_party()
        if party is None:
            return
        party_name = party.name
        self._store.party().delete(party)
        print("-> Party %s deleted" % party_name)
