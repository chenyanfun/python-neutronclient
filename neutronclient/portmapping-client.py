# Copyright 2012 OpenStack Foundation.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
import  argparse
import  six

from neutronclient.common import exceptions
from neutronclient.common import utils
from neutronclient.i18n import _

class Listportmappings(neutronv20.ListCommand):
    """List portmappingtable"""

    resoure = "portmappings"
    shadow_resource = "eayun_portmappings"
    list_columns = ['status','router_id','destination_ip','protocol','name','admin_state_up','tenant_id','destination_port','router_port','id']
    pagination_support = True
    sorting_support = True

class Showportmappings(neutronv20.ShowCommand):
    """show information of given portmappings"""

    resource = "portmappings"
    shadow_resource = "eayun_portmappings"
    allow_names = True
    ids_only = ['portmappings']

    def format_output_data(self,data):
        if self.resource in data:
            for k,v in six.iteritems(data[self.resource]):
                if k in self.ids_only and isinstance(v,list):
                    data[self.resource][k] = [item['id'] for item in v]

        super(Showportmappings,self).format_output_data(data)

class Createportmappings(neutronv20.CreateCommand):
    """Create a portmappings"""

    resource = "portmappings"
    shadow_resource = "eayun_portmappings"
    ids_only = ['portmappings']

    def format_output_data(self,data):
        if self.resource in data:
            for k,v in six.iteritems(data[self.resource]):
                if k in self.ids_only and isinstance(v,list):
                    data[self.resource][k] = [item['id'] for item in v]
        super(Createportmappings,self).format_output_data(data)

    def add_know_arguments(self,parser):
        #parser.add_argument(
        #    'id',metavar = 'id',
        #    help=_('')
        #)
        #parser.add_argument(
        #    'status',metavar = 'status',
        #    help=_('')
        #)
        parser.add_argument(
            'router_id',metavar = 'router-id',
            help=_('this router to mapping')
        )
        parser.add_argument(
            'router_port',metavar = 'router-port',
            help=_('this router-port')
        )
        parser.add_argument(
            'protocol',metavar = 'protocol',
            help=_('this portmapping match protocol')
        )
        parser.add_argument(
            'destination_ip',
            help=_('really destination ip')
        )
        parser.add_argument(
            'name',
            help=_('this portmapping name')
        )
        #parser.add_argument(
        #    'admin_state_up',metavar = 'admin_state_up',
        #    help=_('')
        #)
        #parser.add_argument(
        #    'tenant_id',metavar = 'tenant_id',
        #    help=_('')
        #)
        parser.add_argument(
            'destination_port',
            help=_('portmapping destination port')
        )



    def args2body(self,parsed_args):
        body = {
            'portmapping':{
                'router_id':parsed_args.router_id,
                #'destination_ip':parsed_args.destination_ip,
                'protocol':parsed_args.protocol,
                #'destination_port':parsed_args.destination_port,
                'router_port':parsed_args.router_port,
            }
        }
        if parsed_args.name:
            body['portmapping'].update({'name':parsed_args.name})
        if parsed_args.destination_ip:
            body['portmapping'].update({'destination_ip':parsed_args.destination_ip})
        #if parsed_args.protocol:
        #    body['portmapping'].update({'protocol':parsed_args.protocol})
        if parsed_args.destination_port:
            body['portmapping'].update({'destination_port':parsed_args.destination_port})
        #if parsed_args.router_port:
        #    body['portmapping'].update({'router_port':parsed_args.router_port})
        return body

class Updateportmapping(neutronV20.UpdateCommand):
    """Update a given portmappings"""

    resource = "portmappings"
    shadow_resource = "eayun-portmappings"

    def add_know_arguments(self,parser):
        parser.add_argument(
            'name',
            help=_('name of portmapping')
        )
        parser.add_argument(
            'destination_ip',
            help=_('destination ip')
        )
        parser.add_argument(
            'protocol',
            help=_('this router to match protocol')
        )
        parser.add_argument(
            'destination_port',
            help=_('this router to mapping instance port')
        )
        parser.add_argument(
            'router_port',
            help=_('this router to mapping itself port')
        )

    def args2body(self,parsed_args):
        body = {'portmapping':{}}

        if parsed_args.name:
            body['portmapping'].update({'name':parsed_args.name})
        if parsed_args.destination_ip:
            body['portmapping'].update({'destination_ip':parsed_args.name})
        #if parsed_args.protocol:
        #    body['portmapping'].update({'protocol':parsed_args.protocol})
        if parsed_args.destination_port:
            body['portmapping'].update({'destination_port':parsed_args.destination_port})
        #if parsed_args.router_port:
        #    body['portmapping'].update({'router_port':parsed_args.router_port})
        return body

class Deleteportmappings(neutronV20.DeleteCommand):
    """Delete a given portmappings"""

    resource = "portmappings"
    shadow_resource = "eayun_portmappings"

class Unbindportmappings(Updateportmapping):
    """Unbind a router to mapping port"""

    def args2body(self,parsed_args):
        return {'portmapping':{'router-id':None}}
