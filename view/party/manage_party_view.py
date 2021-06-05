from view.view import View
from model.store import Store
from view.party.list_party_view import ListPartyView
from view.party.party_view import AddPartyView, DeletePartyView, UpdatePartyView
from view.shell_builder import ShellBuilder


class ManagePartyView(View):
    """
    Interface used by admin to manage parties
    """

    def __init__(self, store: Store):
        self._store = store

    def show(self):
        shell = ShellBuilder(prompt="party") \
            .add_command('list', 'Show parties', ListPartyView(self._store)) \
            .add_command('add', 'Add party', AddPartyView(self._store))\
            .add_command('delete', 'Delete party', DeletePartyView(self._store))\
            .add_command('update', 'Update party', UpdatePartyView(self._store))
        shell.show()
