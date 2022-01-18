# -*- mode: python; python-indent: 4 -*-
import ncs
import ipaddress
from ncs.application import NanoService

class ServiceCallbacks(NanoService):
    @NanoService.create
    def cb_nano_create(self, tctx, root, service, plan, component, state, proplist, component_proplist):
        self.log.info('NanoService create(service=', service._path, ')')

        ip_prefix = root.prefix_allocations[service.name].ip_prefix
        self.log.debug(f'Value of ip-prefix leaf is {ip_prefix}')
        net = ipaddress.IPv4Network(ip_prefix)
        ip_address = next(net.hosts())

        vars = ncs.template.Variables()
        vars.add('IP_ADDRESS', ip_address)
        template = ncs.template.Template(service)
        template.apply('loopback-template', vars)


# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Loopback(ncs.application.Application):
    def setup(self):
        # The application class sets up logging for us. It is accessible
        # through 'self.log' and is a ncs.log.Log instance.
        self.log.info('Loopback RUNNING')

        # Service callbacks require a registration for a 'service point',
        # as specified in the corresponding data model.
        #
        self.register_nano_service('loopback', 'loopback:loopback', 'loopback:loopback-configured', ServiceCallbacks)
