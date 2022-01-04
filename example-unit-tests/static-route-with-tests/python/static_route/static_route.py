# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.application import Service
from .service_utils import Utils

class ServiceCallbacks(Service):

    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        self.log.info(f"Service create(service='{service._path}')")

        for route in service.route:          
            net = ipaddress.ip_network(route.ip_prefix)
            network_address = get_cidr_netaddress(route.ip_prefix)
            netmask = get_cidr_netmask(route.ip_prefix)

            tvars = ncs.template.Variables()
            tvars.add('DEVICE', service.device)
            tvars.add('NETWORK-ADDRESS', network_address)
            tvars.add('NETMASK', netmask)
            tvars.add('NEXT-HOP', route.next_hop)
            tvars.add('IP-PREFIX', route.ip_prefix)

            template = ncs.template.Template(service)
            template.apply('static-route-template', tvars)

# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class StaticRoute(ncs.application.Application):
    def setup(self):
        self.log.info('StaticRoute RUNNING')
        self.register_service('static-route-servicepoint', ServiceCallbacks)

    def teardown(self):
        self.log.info('StaticRoute FINISHED')