# CSC317
'''
Assignment: recreate HTTP protocol in python using socket library

Description:
You are required to write a client and server program in python to emulate the HTTP request and response. Here are some pointers: 
1. Client is going to send a HTTP request message to the server via TCP socket. 
2. Server upon receiving the HTTP request message, should separate the header part from the entity-body part of the message. 
3. Server then processes to get the method, URL, and HTTP version. 
4. Method: if it is not one of the methods specified in the HTTP response should be bad request. 
5. URL: your program should check if the URL exists or not (except for put). 
6. HTTP version: if HTTP version is less than 1.0 response message should be 505. 
7. your program on the server-side should create a map of header fields and values associated with the header field. 
8. Based on the header processing, server should create a HTTP response message should be created and sent to the client.


'''
