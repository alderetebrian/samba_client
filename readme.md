# SMB Client Wrapper

A Python module providing a straightforward and intuitive interface for interacting with SMB shares, wrapping around the `smb.SMBConnection` class.

![SMB Logo](link-to-smb-logo-if-you-have-one.png)

## 🚀 Features

- 🧩 Object-oriented interface for SMB connections.
- 🛡 Context manager support ensuring proper resource management.
- 📁 Utility methods for listing, uploading, and downloading files from/to SMB shares.

## 📋 Requirements

- Python 3.x
- `pysmb` library

## 🖥 Installation

```bash
pip install pysmb
```

## 💡 Usage

### Initialization

Import the `SMBClient` class and initialize it:
```python
from smb_client import SMBClient

client = SMBClient(server_name='YOUR_SERVER_NAME',
                   share_name='YOUR_SHARE_NAME',
                   username='YOUR_USERNAME',
                   password='YOUR_PASSWORD',
                   domain_name='YOUR_DOMAIN_NAME')
### Listing Files

```python
files = client.list_files(remote_dir='/path/on/server/')
for file in files:
    print(file.filename)
```

### Uploading a File

```python
client.upload_file(
    local_filepath='/path/on/local/machine/file.txt',
    remote_filepath='/path/on/server/file.txt'
)
```

### Downloading a File

```python
client.download_file(
    remote_filepath='/path/on/server/file.txt',
    local_filepath='/path/on/local/machine/file.txt'
)
```

### Using as a Context Manager

```python
with SMBClient(server_name='YOUR_SERVER_NAME', ...) as client:
    files = client.list_files(remote_dir='/path/on/server/')
```
