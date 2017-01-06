# coding: utf-8
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import unicode_literals
from __future__ import absolute_import
from testinfra.modules.base import Module


class WindowsRemotePort(Module):

    def __init__(self, remote_server, remote_port):
        self.server = remote_server
        self.port = remote_port
        super(WindowsRemotePort, self).__init__()

    @property
    def is_listening(self):
        find_remote = self.slurp('windows_remote_port.ps1')
        find_remote = "%s\r\n IsRemotePortListening -hostname %s -port %s -timeout 30" % (
            find_remote, self.server, self.port)
        result = self.check_output(find_remote)
        return result == 'True'




