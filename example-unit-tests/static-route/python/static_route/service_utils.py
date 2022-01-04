import ipaddress

class Utils:
    def get_cidr_netaddress(cidr):
        network = ipaddress.ip_network(cidr)
        return str(network.network_address)

    def get_cidr_netmask(cidr):
        network = ipaddress.ip_network(cidr)
        return str(network.netmask)