# (c) 2012-2016, Ansible by Red Hat
#
# This file is part of Ansible Galaxy
#
# Ansible Galaxy is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by
# the Apache Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Ansible Galaxy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Apache License for more details.
#
# You should have received a copy of the Apache License
# along with Galaxy.  If not, see <http://www.apache.org/licenses/>.

#
#  When the application load initialize:
#    - signal/handlers
#    - elasticsearch-dsl default connection

from django.apps import AppConfig
from elasticsearch_dsl import connections
from django.conf import settings


class MainConfig(AppConfig):
    name = 'galaxy.main'
    verbose_name = "Galaxy"

    def ready(self):
        connections.connections.configure(**settings.ELASTICSEARCH)
        import galaxy.main.signals.handlers   # noqa
