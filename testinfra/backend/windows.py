from testinfra.backend import base
from ConfigParser import SafeConfigParser
from winrm.protocol import Protocol
from winrm import Session
import base64


class WinrmBackend(base.BaseBackend):
    NAME = "winrm"

    def __init__(self, name, winrm_config=None, *args, **kwargs):
        self.name, self.user = self.parse_containerspec(name)
        self.winrm_config = winrm_config
        self._client = None
        super(WinrmBackend, self).__init__(self.name, *args, **kwargs)

    @property
    def client(self):
         if self._client is None:
             parser = SafeConfigParser()
             parser.read(self.winrm_config)
             username = parser.get('winrm', 'username')
             password = parser.get('winrm', 'password')
             transport = parser.get('winrm', 'transport')
             secure_transport = 'ssl' if parser.get('winrm', 'secure_transport') == "true" else transport
             host = Session._build_url(self.hostname, secure_transport)
             self._client = Protocol(endpoint=host, username=username, password=password, transport=transport, server_cert_validation='ignore')
         return self._client


    def run(self, command, *args, **kwargs):
        shell_id = self.client.open_shell()
        encoded_script = base64.b64encode(command.encode("utf_16_le"))
        command_id = self._client.run_command(shell_id, "powershell -encodedcommand %s" % encoded_script)
        stdout, stderr, rc = self._client.get_command_output(shell_id, command_id)
        self._client.cleanup_command(shell_id, command_id)
        self._client.close_shell(shell_id)

        return self.result(rc, self.encode(command), stdout, stderr)

