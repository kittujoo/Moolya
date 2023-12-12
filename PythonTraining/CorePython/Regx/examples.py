def matching_url():
    import re

    text = "Visit our website at https://www.exa9mple.com.ib for more information."

    # Find all URLs in the text
    pattern = re.compile(r'https://\S+')
    urls = pattern.findall(text)

    print("URLs:", urls)


def matching_ipv4_address():
    import re

    text = "IP addresses: 192.168.1.1, 10.0.0.1, 172.16.0.1"

    # Find all IPv4 addresses in the text
    pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    ip_addresses = pattern.findall(text)

    print("IPv4 Addresses:", ip_addresses)


if __name__ == '__main__':
    # matching_url()
    matching_ipv4_address()