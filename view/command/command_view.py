from view.view import View
from view.common import Common
from view.party.list_party_view import ListPartyView

from model.store import Store
from model.mapping.customer import Customer
from controller.command_builder import CommandBuilder

from exceptions import InvalidData, Error, ResourceNotFound, NotEnoughParties


class CommandView(View):
    """
    Command creation view. User will be able to add party in the basket and register the command at end.
    He can exit the command, this one will not be register in database.
    """

    def __init__(self, user: Customer, store: Store):
        self._user = user
        self._store = store
        self._common = Common()
        self._command = CommandBuilder(self._user, store)

    def show(self):
        print("Create command")
        self.help()
        while True:
            try:
                command = input('command > ').lower().strip()
                if command == 'exit':
                    # Exit loop
                    break
                elif command == 'help':
                    self.help()
                elif command == 'register':
                    self._command.register()
                    print("Command registered, it will be take in charge by our team !")
                    break
                elif command == 'price':
                    print("Price: %d euros" % self._command.get_price())
                elif command == 'partys':
                    ListPartyView(self._store).show()
                elif command == 'basket':
                    self.show_basket()
                elif command.startswith('add ') or command.startswith('update '):
                    if len(command.split(' ')) != 3:
                        print("Error with arguments")
                    else:
                        action, party_name, number = command.split(' ')
                        # TODO: check number is integer
                        self.add_party(party_name, int(number), update=action == 'update')
                elif command.startswith('del '):
                    if len(command.split(' ')) != 2:
                        print("Error with arguments")
                    else:
                        _, party_name = command.split(' ')
                        self.delete_party(party_name)
                elif command.startswith('search '):
                    if len(command.split(' ')) != 2:
                        print("Error with arguments")
                    else:
                        _, search = command.split(' ')
                        ListPartyView(self._store, search=search).show()
                else:
                    print("Unknown command")
            except InvalidData as e:
                self.error_message(str(e))
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))

    def add_party(self, party_name: str, number: int, update: bool = False):
        try:
            party = self._store.party().get_by_name(party_name)
        except ResourceNotFound:
            print("Party %s not found" % party_name)
            return

        try:
            if update:
                self._command.update_number(party, number)
                print("Party %s updated" % party_name)
            else:
                self._command.add_party(party, number)
                print("Party %s added" % party_name)
        except NotEnoughParties:
            print("/!\\ Not enough party in store")

    def delete_party(self, party_name: str):
        try:
            party = self._store.party().get_by_name(party_name)
        except ResourceNotFound:
            print("Party %s not found" % party_name)
            return
        self._command.remove_party(party)
        print("Party %s deleted" % party_name)

    def show_basket(self):
        basket = self._command.get_basket()
        for item in basket:
            print(" * %d x %s (%s)" % (item.number, item.party.name, item.party.description))

    def help(self):
        print()
        print("  * add <party> <number>: Add party in basket")
        print("  * del <party>: Delete party in basket")
        print("  * update <party> <number>: Update number party items")
        print("  * parties: Show parties")
        print("  * basket: Show basket items")
        print("  * exit: Cancel command")
        print("  * help: show this help")
        print("  * price: Show command price")
        print("  * register: Register command")
        print("  * search <string>: Search parties")
        print()
