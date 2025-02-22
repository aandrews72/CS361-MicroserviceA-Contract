# CS361-MicroserviceA-Contract

## Requesting Data
The main program must request data from microservice A by using ZeroMQ, setting up a context, connecting to port 2025 via TCP, and sending a string of a random number between 0 and 39 inclusive. 

Once the microservice receives this data, it will parse the received data, gather the associated activity with the value at that element inside of an array, and send back a string of that activity.

The main program should be waiting to receive a string, initialize that to a variable, and complete whatever action it needs to with the data from microservice A. 

## Example Call
The client, or main program, after initializing a ZeroMQ context and socket through port 2025 via TCP, should generate the random number using Python's random library, then send a string of that integer as:

```python
socket.send_string(str(random_number)
```

After sending this random number the client should immediately initialize a variable to store the response, which could be:

```python
response = socket.recv_string()
```

These are just examples of how the client, could send and receive data from microservice A. 
