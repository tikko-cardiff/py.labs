#listening on local machine(127.0.0.1) port 10805
#decode messages using ASCII format
#count numbers of letter in a messgae
#count number numbers in message
#send processed information back to sender
#output should be printed each time it recieves a messgae
#total number of messages received should be printed each time it recieves a new message


import socket
import time

#server setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 10805))
print('Listening at ' + str(sock.getsockname()))
print()

#intializing for message count
total_so_far = 0


while True:
    data, address = sock.recvfrom(65535) #to decode message recieved from process
    text = data.decode('ascii')
    print("Received a datagram from " + str(address)) 
    numcount = 0
    letcount = 0
    for i in range (len(text)):
         character = text[i]
         if (character.isalpha()):
             letcount = letcount + 1 #counting letters in the text sent from process
         elif (character.isnumeric()):
            numcount = numcount + 1 #counting number sent in text from process
    print("Datagram contained the following text: " + str(text)) #to print message recieved from process
    total_so_far = total_so_far + 1 # to count number of messages sent from process
    print("I have recieved " + str(total_so_far)) 
    print()

    time.sleep(5)

    text = "Your data contains " + str(letcount) + " letters and " + str(numcount) + " numbers."   #to action message from process
    data = text.encode('ascii')
    print("Sending message back to " + str(address) + " saying: " + text) #to show response back to process
    print()
    print()
    sock.sendto(data, address)