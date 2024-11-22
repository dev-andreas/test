def ip_to_int(ip: str) -> int:
    octets = ip.split(".")
    return (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])

def calculate_range(base_ip: str, cidr_prefix: int):
    base_ip_int = ip_to_int(base_ip)
    mask = (1 << 32) - (1 << (32 - cidr_prefix))
    network_start = base_ip_int & mask
    network_end = network_start | ~mask & 0xFFFFFFFF
    return network_start, network_end

def is_ip_in_range(ip: str, ip_range: str) -> bool:
    try:
        base_ip, cidr_prefix = ip_range.split("/")
        cidr_prefix = int(cidr_prefix)

        ip_int = ip_to_int(ip)
        network_start, network_end = calculate_range(base_ip, cidr_prefix)
        
        return network_start <= ip_int <= network_end
    except Exception as e:
        print(f"Error: {e}")
        return False
    
def is_ip_in_ranges(ip: str, ip_ranges: list) -> bool:
    for range in ip_ranges:
        if is_ip_in_range(ip, range):
            return True
    return False

print(is_ip_in_ranges('128.40.0.1', ['128.30.0.0/15', '128.40.0.0/15']))