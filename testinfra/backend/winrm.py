from testinfra.backend import base

class WinrmBackend(base.BaseBackend):
    NAME = "winrm"

    def __init__(self, name, *args, **kwargs):
        self.name, self.user = self.parse_containerspec(name)
        super(WinrmBackend, self).__init__(self.name, *args, **kwargs)

    def run(self, command, *args, **kwargs):
        return NotImplemented