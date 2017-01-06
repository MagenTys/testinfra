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


class WindowsFeature(Module):

    def __init__(self, name):
        self.name = name
        super(WindowsFeature, self).__init__()

    @property
    def is_installed(self):
        find_feature = self.slurp('windows_feature.ps1')
        find_feature = "%s\r\n Exit-Json (ListWindowsFeatures -feature %s -provider powershell)" % (
            find_feature, self.name)
        result = self.check_output(find_feature)
        feature = json.loads(result)
        return feature["Installed"] == True




