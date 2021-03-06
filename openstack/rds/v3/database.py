# -*- coding:utf-8 -*-
# Copyright 2019 Huawei Technologies Co.,Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack.rds import rds_service
from openstack.rds.v3 import rdsresource as _rdsresource
from openstack import resource2 as resource


class Database(_rdsresource.Resource):
    base_path = 'instances/%(instance_id)s/database'
    resources_key = 'databases'
    service = rds_service.RDSServiceV3()

    _query_mapping = resource.QueryParameters('page', 'limit')

    # capabilities
    allow_create = True
    allow_delete = True
    allow_list = True

    # Properties
    # instanceId
    instance_id = resource.URI('instance_id')
    # database name
    name = resource.Body("name")
    # database character_set
    character_set = resource.Body("character_set")


class DatabaseDetail(Database):
    base_path = 'instances/%(instance_id)s/database/detail'

    # capabilities
    allow_create = False
    allow_delete = False
    allow_list = True
