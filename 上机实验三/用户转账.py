dic={"aaa":["123456",10000],"bbb":["888888",5000],"ccc":["333333",3000]}

username = input()
if dic.get(username) != None:
    tran_money = int(input())
    all_money = dic.get("aaa")[1]
    if all_money < tran_money:
        print("Insufficient Funds")
    else:
        dic["aaa"] = ["123456",all_money - tran_money]
        dic[username] = [dic.get(username)[0],dic.get(username)[1] + tran_money]
        print("Tranfer Success")
        print("aaa:" + str(dic.get("aaa")[1]))
        print(username + ":" + str(dic.get(username)[1]))
else:
    print("Wrong User")