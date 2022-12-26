from socket import *
import sys

if len(sys.argv) <= 1:
    print('Usage: "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address of the Proxy Server')
    sys.exit(2)

# 서버 소켓을 생성하고 포트에 바인딩한 다음 수신 대기 시작
tcpSerPort = 8888
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# 서버 소켓 준비
tcpSerSock.bind(('', tcpSerPort))
tcpSerSock.listen(5)

while True:
    # 클라이언트에서 데이터 수신 시작
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from: ', addr)
    message = tcpCliSock.recv(1024)

    # 주어진 메시지에서 파일 이름 추출
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    fileExist = "false"
    filetouse = "/" + filename
    try:
        # 파일이 캐시에 존재하는지 확인
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        print('File Exists!')

        # cache hit 찾기, 응답 메시지 생성
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")

        # 요청된 파일의 내용을 클라이언트에게 전송
        for i in range(0, len(outputdata)):
            tcpCliSock.send(outputdata[i])
        print('Read from cache')

        # 캐시에서 찾을 수 없는 파일에 대한 오류 처리
    except IOError:
        print('File Exist: ', fileExist)
        if fileExist == "false":
            # 프록시 서버에 소켓 만들기
            print('Creating socket on proxyserver')
            c = socket(AF_INET, SOCK_STREAM)

            hostn = filename.replace("www.", "", 1)
            print('Host Name: ', hostn)
            try:
                # 소켓을 포트 80에 연결
                c.connect((hostn, 80))
                print('Socket connected to port 80 of the host')

                # 이 소켓에 임시 파일을 만들고 클라이언트가 요청한 파일에 대해 포트 80에 요청
                fileobj = c.makefile('r', 0)
                fileobj.write("GET " + "http://" + filename + " HTTP/1.0\n\n")

                # 버퍼로 응답 읽기
                buff = fileobj.readlines() 

                # 요청된 파일의 캐시에 새 파일을 만듦.
                # 버퍼의 응답을 클라이언트 소켓과 캐시의 해당 파일로 보냄.
                tmpFile = open("./" + filename, "wb")
                for i in range(0, len(buff)):
                    tmpFile.write(buff[i])
                    tcpCliSock.send(buff[i])

            except:
                print('Illegal request')

        else:
            # 찾을 수 없는 파일에 대한 HTTP 응답 메시지
            print('File Not Found...Stupid Andy')
            a = 2
    # 소켓과 서버 소켓 닫기
    tcpCliSock.close()