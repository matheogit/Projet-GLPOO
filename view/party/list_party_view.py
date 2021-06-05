from model.store import Store
from view.view import View


class ListPartyView(View):
    """
    Show parties
    """

    def __init__(self, store: Store, search: str = None):
        self._store = store
        self._search = search

    def show(self):
        if self._search is not None:
            parties = self._store.party().search(self._search)
        else:
            parties = self._store.party().get_all()
        print("Articles:")
        for party in parties:
            print("- %s: %s" % (party.name, party.location))
            print("     price: %d" % party.price)
            print("     date: %d" % party.date)
