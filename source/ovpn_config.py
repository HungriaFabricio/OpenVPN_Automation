import textwrap

openvpn_config = """#!/bin/bash 

# 1 argument = Client_identifier
cat <(echo -e 'client') \\
<(echo -e 'proto udp') \\
<(echo -e 'dev tun') \\
<(echo -e 'remote 127.0.0.1 1194') \\
<(echo -e 'resolv-retry infinite') \\
<(echo -e 'nobind') \\
<(echo -e 'persist-key') \\
<(echo -e 'persist-tun') \\
<(echo -e 'remote-cert-tls server') \\
<(echo -e 'cipher AES-256-GCM') \\
<(echo -e '#user nobody') \\
<(echo -e '#group nobody') \\
<(echo -e 'verb 3') \\
    <(echo -e '<ca>') \\
    ca.crt \\
    <(echo -e '</ca>\\n<cert>') \\
    ${1}.crt \\
    <(echo -e '</cert>\\n<key>') \\
    ${1}.key \\
    <(echo -e '</key>\\n<tls-crypt-v2>') \\
    ${1}.pem \\
    <(echo -e '</tls-crypt-v2>') \\
    > ${1}.ovpn
"""