from .service_utils import Utils
import pytest

def test_cidr_to_netaddress_pass():
    assert Utils.get_cidr_netaddress("10.0.0.0/16") == "10.0.0.0"
    assert Utils.get_cidr_netaddress("192.168.2.0/24") == "192.168.2.0"
    assert Utils.get_cidr_netaddress("240.240.240.240") == "240.240.240.240"

def test_cidr_to_netaddress_fail():
    with pytest.raises(Exception):
        Utils.get_cidr_netaddress("10.0.0.1/16")
        Utils.get_cidr_netaddress("256.0.0.0/16")
        Utils.get_cidr_netaddress("")
        Utils.get_cidr_netaddress("10.0.0.1")
        Utils.get_cidr_netaddress("Rick")

def test_cidr_to_netmask_pass():
    assert Utils.get_cidr_netmask("10.0.0.0/16") == "255.255.0.0"
    assert Utils.get_cidr_netmask("192.168.2.0/24") == "255.255.255.0"
    assert Utils.get_cidr_netmask("240.240.240.240") == "255.255.255.255"

def test_cidr_to_netmask_fail():
    with pytest.raises(Exception):
        Utils.get_cidr_netaddress("10.0.0.0/33")
        Utils.get_cidr_netaddress("256.0.0.0/16")
        Utils.get_cidr_netaddress("")
        Utils.get_cidr_netaddress("24")
        Utils.get_cidr_netaddress("Morty")