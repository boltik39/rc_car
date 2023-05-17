import socket
from utils.UDPDataWorker import UDPDataWorker
from utils.ConfigData import ConfigData


class UDPServer:
    __LOCAL_IP = ConfigData().get_from_config('local_ip')
    __PORT = int(ConfigData().get_from_config('port'))
    __BUFFER = int(ConfigData().get_from_config('buffer_size'))

    def __init__(self, local_ip: str = __LOCAL_IP, local_port: int = __PORT, buffer: int = __BUFFER):
        self._server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self._server.bind((local_ip, local_port))
        print(f"UDP server up and listening on port {local_port}")
        self._buffer = buffer

    def start_listening(self):
        data_worker = UDPDataWorker()
        while True:
            message = self._server.recvfrom(self._buffer)[0]
            data_worker.work_with_data(message.decode('utf-8'))

