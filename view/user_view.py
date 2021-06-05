from model.mapping.user import User
from model.store import Store
from view.common import Common
from view.view import View
from view.article.list_article_view import ListArticleView
from view.shell_builder import ShellBuilder
from view.command.command_view import CommandView
from view.command.list_commands_view import ListCommandsView


class UserView(View):
    """
    User View
    User interface
    """

    def __init__(self, user: User, store: Store):
        self._common = Common()
        self._user = user
        self._store = store

    def show(self):
        shell = ShellBuilder() \
            .add_command('articles', 'Show articles', ListArticleView(self._store)) \
            .add_command('command', 'Create command', CommandView(self._user, self._store))\
            .add_command('commands', 'List historic commands', ListCommandsView(self._store, self._user))\
            .add_command('profile', 'Show user profile', View())
        shell.show()
