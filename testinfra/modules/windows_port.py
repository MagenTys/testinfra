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


class WindowsPort(Module):

    def __init__(self, port, protocol = "tcp"):
        self.port = port
        self.protocol = protocol
        super(WindowsPort, self).__init__()

    @property
    def is_listening(self):
        is_port_listening_function = self.slurp('windows_port.ps1')
        is_port_listening_function  = "%s\r\n IsPortListening -portNumber %s -protocol %s" % (is_port_listening_function , self.port, self.protocol)
        out = self.check_output(is_port_listening_function)
        return out == "True"




