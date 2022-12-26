#import socket module
from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)
#서버 소켓 준비
serverSocket.bind(('', 12006))
serverSocket.listen(1)
while True:
    print('Ready to serve...')
    #연결 설정
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        #하나의 HTTP 헤더 라인을 소켓으로 전송
        connectionSocket.send('HTTP/1.0 200 OK\r\n\r\n')
        #요청된 파일의 내용을 클라이언트에 전송
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #찾을 수 없는 파일에 대한 응답 메시지
        connectionSocket.send('404 Not Found')
        #클라이언트 소켓 닫기
        connectionSocket.close()
serverSocket.close()
sys.exit()#해당 데이터 전송 후 프로그램 종료