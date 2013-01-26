# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from marvin.integration.lib.base import CloudStackEntity
from marvin.cloudstackAPI import authorizeSecurityGroupEgress
from marvin.cloudstackAPI import revokeSecurityGroupEgress

class SecurityGroupEgress(CloudStackEntity.CloudStackEntity):


    def __init__(self, items):
        self.__dict__.update(items)


    def __init__(self, items):
        self.__dict__.update(items)


    def authorize(self, apiclient, **kwargs):
        cmd = authorizeSecurityGroupEgress.authorizeSecurityGroupEgressCmd()
        [setattr(cmd, key, value) for key,value in kwargs.items]
        securitygroupegress = apiclient.authorizeSecurityGroupEgress(cmd)


    def revoke(self, apiclient, id, **kwargs):
        cmd = revokeSecurityGroupEgress.revokeSecurityGroupEgressCmd()
        cmd.id = id
        [setattr(cmd, key, value) for key,value in kwargs.items]
        securitygroupegress = apiclient.revokeSecurityGroupEgress(cmd)

