from concurrent.futures import ThreadPoolExecutor

import grpc
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s - %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S',
)

import servos_pb2 as servo_pb
import servos_pb2_grpc as servo_rpc

class Client:
    def __init__(self, address):
        self.channel = grpc.insecure_channel(address)
        self.stub = servo_rpc.SendUpdateSerovsStub(self.channel)
        logging.info('Connect to %s', address)

    def close(self):
        self.channel.close()

    def update_servo_values(self, values):
        request = servo_pb.UpdateServos(servo_values = values)
        logging.info('Servo update request initiated with:\n%s', request)
        response = self.stub.Start(request)
        return response


if __name__ == '__main__':
    import netwrok_config as net
    address = f'{net.host}:{net.port}'
    client = Client(address)

    # get servo values from UI
    servo_values = [0, 0, 9, 1]

    client.update_servo_values(values = servo_values)
