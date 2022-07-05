import ipaddress


def summarizer(prefixes, quota):
    """
    Takes a list of prefixes, finds another (smaller) list of prefixes that includes
    all IPs covered in the original list
    """

    for i in range(32, -1, -1):

        supernets = {}
        for subnet in prefixes:
            subnet = ipaddress.IPv4Network(subnet)
            k = subnet.supernet(new_prefix=i) if subnet.prefixlen > i else subnet
            supernets.setdefault(k, set()).add(subnet)

        tight_supernets = set()
        for supernet, subnets in supernets.items():
            lowest_addr = min((i.network_address for i in subnets))
            highest_addr = max((i.broadcast_address for i in subnets))

            for j in range(32, supernet.prefixlen - 1, -1):
                tight_supernet = ipaddress.IPv4Network((lowest_addr, j), strict=False)
                if highest_addr in tight_supernet:
                    break

            if tight_supernet.prefixlen > supernet.prefixlen:
                tight_supernets.add(tight_supernet)
            else:
                tight_supernets.add(supernet)

        collapsed_tight_supernets = list(ipaddress.collapse_addresses(tight_supernets))

        if len(collapsed_tight_supernets) <= quota:
            return collapsed_tight_supernets
