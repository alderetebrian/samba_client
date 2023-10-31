import socket
from smb.SMBConnection import SMBConnection

class SMBClient:
    def _init_(self, server_name, share_name, username, password, domain_name, client_name='smb_client'):
        self.server_name = server_name
        self.server_ip = self._resolve_ip(server_name)
        self.share_name = share_name
        self.username = username
        self.password = password
        self.domain_name = domain_name
        self.client_name = client_name
        self.conn = None

    def _resolve_ip(self, server_name):
        try:
            return socket.gethostbyname(server_name)
        except socket.gaierror:
            raise ConnectionError(f"Failed to resolve {server_name} to an IP address")

    def _enter_(self):
        self.conn = self._connect()
        return self

    def _exit_(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

    def _connect(self):
        conn = SMBConnection(self.username, self.password, self.client_name, self.server_name, domain=self.domain_name, use_ntlm_v2=True)
        if not conn.connect(self.server_ip, 139):
            raise ConnectionError(f"Failed to connect to {self.server_ip}")
        return conn

    def list_files(self, remote_dir):
        return self.conn.listPath(self.share_name, remote_dir)

    def upload_file(self, local_filepath, remote_filepath):
        with open(local_filepath, 'rb') as file:
            self.conn.storeFile(self.share_name, remote_filepath, file)

    def download_file(self, remote_filepath, local_filepath):
        with open(local_filepath, 'wb') as file:
            self.conn.retrieveFile(self.share_name, remote_filepath, file)
