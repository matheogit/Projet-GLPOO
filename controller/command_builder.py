from model.mapping.party import Party
from model.mapping.customer import Customer
from model.mapping.command import Command
from model.mapping.command_status_enum import CommandStatusEnum
from model.store import Store
from exceptions import NotEnoughParties, ResourceNotFound, InvalidData


class CommandBuilder:
    """
    Build command for a customer
    Design pattern builder (function register must be call at end)
    """

    def __init__(self, customer: Customer, store: Store):
        self._customer = customer
        self._store = store
        self._basket = {}  # mapping basket items

    def get_basket(self):
        return [self._basket[item] for item in self._basket]

    def add_party(self, party: Party, number: int):
        # check stocks
        if party.number - number < 0:
            raise NotEnoughParties()

        self._basket[party.id] = BasketItem(party, number)

    def remove_party(self, party: Party):
        if party.id in self._basket:
            del(self._basket[party.id])

    def update_number(self, party: Party, number: int):
        if party.id not in self._basket:
            raise ResourceNotFound()
        basket_item = self._basket[party.id]
        if number > basket_item.party.number:
            # check stocks
            raise NotEnoughParties()

        basket_item.number = number

    def get_price(self):
        price = 0
        for _, item in self._basket.items():
            price += item.party.price * item.number

        return price

    def register(self):
        command = Command(status=CommandStatusEnum.PENDING,
                          customer=self._customer)

        if len(self._basket.items()) == 0:
            raise InvalidData()
        for _, item in self._basket.items():
            party = item.party
            command.add_party(party, item.number)
            # update party stocks
            party.number = party.number - item.number

        self._store.command().create(command)

        return command


class BasketItem:
    party = None
    number = None

    def __init__(self, party: Party, number: int):
        self.party = party
        self.number = number
