from globs import net_to_glob
import ipaddress

def test_net_to_glob_1():
    output = list(net_to_glob(ipaddress.IPv4Network('10.8.0.0/16')))
    assert output == ['10.8.*']
