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
        print("Soirées:")
        for party in parties:
            print("- %s: %s" % (party.name, party.location))
            print("     prix: %d €" % party.price)
            print("     date: %s" % party.date)
            print("     createur: %s" % party.creator_id)
            print("     places totales: %s" % party.total_place)
            print("     note: %s" % party.grade)
            print("     état: %s" % party.state)
            print("     theme: %s" % party.theme)
