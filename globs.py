import itertools
import ipaddress


def net_to_glob(n):
    """
    Takes a network, returns one or more globs that together completely cover the
    network

    10.8.0.0/16 -> 10.8.*
    10.8.0.0/15 -> 10.8.*, 10.9.*
    10.1.1.1/32 -> 10.1.1.1
    0.0.0.0/0   -> "*"
    """
    if not getattr(n, "prefixlen") or not getattr(n, "subnets"):
        n = ipaddress.IPv4Network(n)

    for i in range(5):
        if n.prefixlen <= i * 8:
            for subnet in n.subnets(new_prefix=i * 8):
                if i * 8 < 32:
                    yield ".".join(
                        itertools.chain(str(subnet).split("/")[0].split(".")[:i], "*")
                    )
                else:
                    yield str(subnet).split("/")[0]
            return


def glob_to_net(g):
    """
    10.8.* -> 10.8.0.0/16
    """
