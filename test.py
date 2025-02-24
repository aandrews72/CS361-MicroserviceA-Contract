import zmq
import random
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:2025")


def get_num():
    random_number = random.randint(0, 39)
    print(f"Sending number: {random_number}")
    socket.send_string(str(random_number))


def get_response():
    response = socket.recv_string()
    print("Received response, sleeping for two seconds.")
    time.sleep(2)
    print(f"Here is the response: {response}")


def main():
    get_num()
    get_response()


main()
socket.close()
context.term()
