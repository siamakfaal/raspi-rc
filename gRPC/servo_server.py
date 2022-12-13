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

class UpdateServos(servo_rpc.SendUpdateSerovsServicer):
    def Start(self, request, context):
        # Show recived request [servo values to be updated]
        logging.info('New servo values =\n%r', request)
        # Send values to the timers
        # If successful send True, else return False
        success = True
        return servo_pb.AckUpdateServos(ack = success)


if __name__ == '__main__':
    import netwrok_config as net

    server = grpc.server(ThreadPoolExecutor())
    servo_rpc.add_SendUpdateSerovsServicer_to_server(UpdateServos(), server)

    address = f'[::]:{net.port}'
    server.add_insecure_port(address)
    server.start()

    logging.info('Server is ready on %s', address)
    server.wait_for_termination(200)
    logging.info('Server stopped on %s', address)

    
