
import requests
from cryptography import x509
from cryptography.hazmat.primitives import serialization

# Load The CSR content
csr_file = open("CSR.csr", "rb")
csr_content = x509.load_pem_x509_csr(csr_file.read())

# URL of the API endpoint
url = "https://10.1.44.154:10200/sign-csr?sid=53"  # id (53)

# Sending the request with csr_content as form data
response = requests.get(url, data={'csr_content': csr_content.public_bytes(serialization.Encoding.PEM)}, verify=False)

# Check if the request was successful
if response.status_code == 200:
    filename = "signed-server-public-key.pem"
    
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Certificate saved to {filename}")

else:
    print(f"Error with status code: {response.status_code}")
    print(response.text)
