mac2id=dict()                                                           # mac2id
onlinetimes=[]

f=open(r'D:\Workplace\sklearnML\3.聚类\3.2DBscan\TestData.txt',encoding='utf-8')
for line in f:
    mac=line.split(',')[2]                                              # 读取mac地址
    onlinetime=int(line.split(',')[6])                                  # 读取上网时长
    starttime=int(line.split(',')[4].split(' ')[1].split(':')[0])       # 读取开始上网时间
    print(mac, onlinetime, starttime)
    if mac not in mac2id:
        mac2id[mac]=len(onlinetimes)                      # key是mac地址，value是对应mac地址的上网时长以及开始上网时间  
        onlinetimes.append((starttime,onlinetime))
        #print("not")
        #print(mac,mac2id[mac],onlinetimes)
    else:
        onlinetimes[mac2id[mac]]=[(starttime,onlinetime)]
        #print("else")
        #print(mac,mac2id[mac],onlinetimes)

for item in mac2id.items():
    print(item)

for i in range(len(onlinetimes)):
    print("序号：%s   值：%s" % (i + 1, onlinetimes[i]))
