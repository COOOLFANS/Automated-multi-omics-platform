import threading
import queue
import time
import socket
import json
def parse_http_request(request_bytes):
 
    request_str = request_bytes.decode('utf-8')
 
    headers, body = request_str.split('\r\n\r\n', 1)
    
    request_line, *header_lines = headers.split('\r\n')
  
    method, path, http_version = request_line.split(' ')
 
    headers = {}
    for line in header_lines:
        key, value = line.split(': ', 1)
        headers[key] = value

    return str(body)

def producer(ot2_ip,port,ot_in_queue,ot_out_queue):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ot2_ip, port))
    server.listen(5)
    print(f"Listening on {ot2_ip}:{port}")

    while True:
 
        client_socket, addr = server.accept()
        movemode=client_socket.recv(1024)
        movemode=parse_http_request(movemode)
        print('ReceiveMoveMode',movemode)
        print(type(movemode))
             
        if movemode=='1' or movemode=='2' or movemode=='3' or movemode=='4' or movemode=='5' or movemode=='6' or movemode=='7'or movemode=='8' or movemode=='9' or movemode=='10' or movemode=='11' or movemode=='12' or movemode=='13' or movemode=='14' or movemode=='15' or movemode=='16' or movemode=='17' or movemode=='18' or movemode=='19' or movemode=='20':
            ot_out_queue.put(movemode)
            response_body=ot_in_queue.get()
        else:
            response_body='Error'
        response_body=str(response_body)
        byt_response_body=bytes(response_body.encode('utf-8'))
        response_headers = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: " + str(len(response_body)).encode() + b"\r\n\r\n"
        response = response_headers + byt_response_body

        client_socket.sendall(response)
   
def consumer(arm_ip,port,arm_in_queue,arm_out_queue):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   
    host = '192.168.0.100'

   
    port = 80

    server_socket.bind((host, port))

    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")
  
    while True:
   
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")

        data = client_socket.recv(1024)  
        print('DATA',str(data))
        if str(data.decode('utf-8'))!='END':

            print('END1')
            response = arm_in_queue.get()
         
        if str(data.decode('utf-8'))=='END':
            response = '0'
            arm_out_queue.put('END')
            print('END0')
        response=str(response)
        byt_response=bytes(response.encode('utf-8'))
        client_socket.send(byt_response)

def main_thread(ot_in_queue,ot_out_queue,arm_in_queue,arm_out_queue):
    while True:
       MoveMode=ot_out_queue.get()
       arm_in_queue.put(MoveMode)
       EndSingal=arm_out_queue.get()
       ot_in_queue.put(EndSingal)
       
if __name__ == '__main__':
    ot_in_queue = queue.Queue()
    ot_out_queue = queue.Queue()
    arm_in_queue =queue.Queue()
    arm_out_queue =queue.Queue()
    ot2_ip='169.254.229.211'
    arm_ip='192.168.0.100'
    port=80

    producer_thread = threading.Thread(target=producer, args=(ot2_ip,port,ot_in_queue,ot_out_queue))
    producer_thread.start()

    consumer_thread = threading.Thread(target=consumer, args=(arm_ip,port,arm_in_queue,arm_out_queue))
    consumer_thread.start()

    main_thread(ot_in_queue,ot_out_queue,arm_in_queue,arm_out_queue)

    producer_thread.join()
    consumer_thread.join()
    print('程序结束')