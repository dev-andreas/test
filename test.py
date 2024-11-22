def ipv4_to_int(ip: str) -> int:
    octets = ip.split(".")
    return (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])

def calculate_ipv4_range(base_ip: str, cidr_prefix: int):
    base_ip_int = ipv4_to_int(base_ip)
    mask = (1 << 32) - (1 << (32 - cidr_prefix))
    network_start = base_ip_int & mask
    network_end = network_start | ~mask & 0xFFFFFFFF
    return network_start, network_end

def is_ipv4_in_range(ip: str, ip_range: str) -> bool:
    try:
        base_ip, cidr_prefix = ip_range.split("/")
        cidr_prefix = int(cidr_prefix)

        ip_int = ipv4_to_int(ip)
        network_start, network_end = calculate_ipv4_range(base_ip, cidr_prefix)
        
        return network_start <= ip_int <= network_end
    except Exception as e:
        print(f"Error: {e}")
        return False
    
def is_ip_in_ranges(ip: str, ip_ranges: list) -> bool:
    for range in ip_ranges:
        if is_ipv4_in_range(ip, range):
            return True
    return False

def ipv6_to_int(ip: str) -> int:
    expanded_ip = expand_ipv6(ip)
    groups = expanded_ip.split(":")
    ip_int = 0
    for group in groups:
        ip_int = (ip_int << 16) + int(group, 16)
    return ip_int

def expand_ipv6(ip: str) -> str:
    if "::" in ip:
        left, _, right = ip.partition("::")
        left_groups = left.split(":") if left else []
        right_groups = right.split(":") if right else []
        num_zero_groups = 8 - (len(left_groups) + len(right_groups))
        ip = ":".join(left_groups + ["0"] * num_zero_groups + right_groups)
    return ":".join(group.zfill(4) for group in ip.split(":"))

def calculate_ipv6_range(base_ip: str, cidr_prefix: int) -> (int, int):
    base_ip_int = ipv6_to_int(base_ip)
    mask = (1 << 128) - (1 << (128 - cidr_prefix))
    network_start = base_ip_int & mask
    network_end = network_start | ~mask & ((1 << 128) - 1)
    return network_start, network_end

def is_ipv6_in_range(ip: str, ip_range: str) -> bool:
    try:
        base_ip, cidr_prefix = ip_range.split("/")
        cidr_prefix = int(cidr_prefix)
        
        ip_int = ipv6_to_int(ip)
        network_start, network_end = calculate_ipv6_range(base_ip, cidr_prefix)
        
        return network_start <= ip_int <= network_end
    except Exception as e:
        print(f"Error: {e}")
        return False
    
def get_ip_version(ip: str) -> str:
    if '.' in ip:
        return 'v4'
    elif ':' in ip:
        return 'v6'
    else:
        return None
    
def is_ip_in_range(ip: str, ip_range: str) -> bool:
    version = get_ip_version(ip)
    if version == 'v4':
        return is_ipv4_in_range(ip, ip_range)
    elif version == 'v6':
        return is_ipv6_in_range(ip, ip_range)
    return False

ip_ranges = ['128.30.0.0/15',
            '128.30.32.0/24',
            '128.30.52.0/24',
            '128.52.0.0/16',
            '18.0.0.0/16',
            '18.10.0.0/16',
            '18.1.0.0/16',
            '18.11.0.0/16',
            '18.1.1.0/24',
            '18.12.0.0/16',
            '18.13.0.0/16',
            '18.1.37.0/24',
            '18.14.0.0/16',
            '18.15.0.0/16',
            '18.16.0.0/16',
            '18.17.0.0/16',
            '18.1.7.0/24',
            '18.18.0.0/16',
            '18.22.0.0/16',
            '18.22.55.0/24',
            '18.23.0.0/16',
            '18.25.0.0/16',
            '18.25.170.0/24',
            '18.26.0.0/16',
            '18.27.0.0/16',
            '18.29.0.0/16',
            '18.3.0.0/16',
            '18.31.0.0/16',
            '18.3.10.0/24',
            '18.3.102.0/24',
            '18.3.1.0/24',
            '18.3.103.0/24',
            '18.3.104.0/24',
            '18.3.105.0/24',
            '18.3.106.0/24',
            '18.3.107.0/24',
            '18.3.108.0/24',
            '18.3.109.0/24',
            '18.3.11.0/24',
            '18.3.111.0/24',
            '18.3.115.0/24',
            '18.3.12.0/24',
            '18.3.122.0/24',
            '18.3.13.0/24',
            '18.3.14.0/24',
            '18.3.15.0/24',
            '18.3.151.0/24',
            '18.3.152.0/24',
            '18.3.153.0/24',
            '18.3.154.0/24',
            '18.3.155.0/24',
            '18.3.156.0/24',
            '18.3.16.0/24',
            '18.3.17.0/24',
            '18.3.18.0/24',
            '18.3.19.0/24',
            '18.3.20.0/24',
            '18.3.2.0/24',
            '18.3.21.0/24',
            '18.3.22.0/24',
            '18.3.23.0/24',
            '18.3.24.0/24',
            '18.3.28.0/24',
            '18.3.3.0/24',
            '18.3.4.0/24',
            '18.3.5.0/24',
            '18.3.6.0/24',
            '18.3.67.0/24',
            '18.3.69.0/24',
            '18.3.7.0/24',
            '18.3.8.0/24',
            '18.3.90.0/24',
            '18.3.9.0/24',
            '18.4.0.0/16',
            '18.4.38.0/24',
            '18.4.70.0/24',
            '18.4.81.0/24',
            '18.4.93.0/24',
            '18.5.0.0/16',
            '18.6.0.0/16',
            '18.7.0.0/16',
            '18.7.10.0/24',
            '18.7.101.0/24',
            '18.7.102.0/24',
            '18.7.108.0/24',
            '18.7.116.0/24',
            '18.7.117.0/24',
            '18.7.118.0/24',
            '18.7.119.0/24',
            '18.7.120.0/24',
            '18.7.130.0/24',
            '18.7.131.0/24',
            '18.7.21.0/24',
            '18.7.23.0/24',
            '18.7.32.0/24',
            '18.7.34.0/24',
            '18.7.39.0/24',
            '18.7.40.0/24',
            '18.7.45.0/24',
            '18.7.54.0/24',
            '18.7.68.0/24',
            '18.7.71.0/24',
            '18.7.80.0/24',
            '18.7.82.0/24',
            '18.7.84.0/24',
            '18.8.0.0/16',
            '18.9.0.0/16',
            '18.9.0.0/24',
            '18.9.1.0/24',
            '18.9.21.0/24',
            '18.9.22.0/24',
            '18.9.25.0/24',
            '18.9.37.0/24',
            '18.9.46.0/24',
            '18.9.47.0/24',
            '18.9.49.0/24',
            '18.9.60.0/24',
            '18.9.62.0/24',
            '18.9.90.0/24',
            '192.52.61.0/24',
            '192.52.62.0/24',
            '192.52.63.0/24',
            '192.52.64.0/24',
            '192.52.65.0/24',
            '2603:4000::/32',
            '2603:4001::/32',
            '2603:4007::/32',
            '2603:4008::/32',
            '2603:4009::/32',
            '2603:400a::/32',
            '2603:4010::/32',
            '2603:4011::/32']
