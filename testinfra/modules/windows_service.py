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
import json

class WindowsService(Module):

    def __init__(self, name):
        self.name = name
        self._service = None
        super(WindowsService, self).__init__()

    @property
    def service(self):
        if self._service is None:
            find_service = self.slurp('windows_service.ps1')
            find_service = "%s\r\n FindService %s" % (
                find_service, self.name)
            result = self.check_output(find_service)
            self._service = json.loads(result)

        return self._service

    @property
    def is_installed(self):
        return self.service["Name"] == self.name

    @property
    def is_running(self):
        return self.service["State"] == "Running"





