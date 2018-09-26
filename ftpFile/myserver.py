s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

def shoudao(c):
    data = c.recv(1024)
    if 






while True:
    try:
        c,addr = s.connect()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        sys.exit()


pid = os.fork()

if pid == 0:
    s.close()
    shoudao(c)
else:
    c.close()
    continue##