import redis

r = redis.Redis(host='10.1.69.134', port = 6379, db = 0)
r.ping()

r.hset("8484","Kaio","1")
r.hset("8484","Alex","")

while(True):
    dados = r.hgetall("8484")
    p1 = dados["Kaio".encode()].decode()
    p2 = dados["Alex".encode()].decode()
    if p1 != "" and p2 != "":
        print(p1, p2)
        exit()

