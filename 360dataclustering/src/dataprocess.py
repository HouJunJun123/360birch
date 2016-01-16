



def data2sum(file_path):
    sipdirc = {}
    sip_sumdirc = {}
    data_file = open(file_path)
    lines = data_file.readlines()
    for line in lines:
        curlist = []
        line = line.split('\t')
        sip = line[0]
        request_method =line[1]
        request_number = float(line[2])
        avglen_uri = float(line[3])
        avgpara_cookie= float(line[4])
        avgpara_uri = float(line[5])
        curlist = [request_number,avglen_uri,avgpara_cookie,avgpara_uri]
        #[x+y for x, y in zip(list1, list2)]
        if sip not in sipdirc.keys():
            sipdirc[sip] = []
            sipdirc[sip].append(curlist)
        else:
            #sipdirc[sip] += curlist
            sipdirc[sip].append(curlist)
    
    sum_file = open('sum_file','w')
    
    for every_sip in sipdirc.keys():
        sip_length = len(sipdirc[every_sip])
        if sip_length == 1:
            sum_list = sipdirc[every_sip][0]
        elif sip_length == 2:            
            sum_list = [x+y for x, y in zip(sipdirc[every_sip][0], sipdirc[every_sip][1])]
        elif sip_length == 3:            
            sum_list == [x+y+z for x, y, z in zip(sipdirc[every_sip][0], sipdirc[every_sip][1],sipdirc[every_sip][2])]
        elif sip_length == 4:            
            sum_list = [x+y+z+w for x, y, z, w in zip(sipdirc[every_sip][0], sipdirc[every_sip][1],sipdirc[every_sip][2],sipdirc[every_sip][3])]
        sum_file.write(every_sip +'\t'+str(sum_list[0])+'\t'+str(sum_list[1])+'\t'+str(sum_list[2])+'\t'+str(sum_list[3]))
        sum_file.write('\n')
        #sipdirc[sip]
    sum_file.close()
    data_file.close()

#def sum2clusteringdata(file_path):

if __name__ == '__main__':
    sip_path = 'http_sip_method.txt'
    sum_path = 'sum_file.txt'
    final_path = 'final_clustring.txt'
    
    sip_file = open(sip_path)
    sum_file = open(sum_path)
    final_file = open(final_path,'w')
    
    sipdirc = {}
    lines = sum_file.readlines()
    for line in lines:
        curlist = []
        line = line.split('\t')
        sip = line[0]
        #request_method =line[1]
        request_number = float(line[1])
        avglen_uri = float(line[2])
        avgpara_cookie= float(line[3])
        avgpara_uri = float(line[4])
        curlist = [request_number,avglen_uri,avgpara_cookie,avgpara_uri]
        if sip not in sipdirc.keys():
            sipdirc[sip] = curlist
            
    lines = sip_file.readlines()
    cursip = '192.168.0.0'
    curlist = []
    get_number = 0.0
    post_number = 0.0
    
    
    for line in lines:
        line = line.split('\t')
        sip = line[0]
        if cursip != sip:
            curlist = [get_number,post_number]
            sipdirc[cursip] += curlist
            get_number = 0.0
            post_number = 0.0
            curlist = []
            cursip = sip
        request_method =line[1]
        request_number = float(line[2])
        if request_method == 'get':
            get_number += request_number     
        elif request_method == 'post':
            post_number += request_number
        else:
            continue
   
    for every_sip in sipdirc.keys():
        print len(sipdirc[every_sip])
        if not len(sipdirc[every_sip]) == 6:
            continue
        final_file.write(every_sip +'\t'+str(sipdirc[every_sip][0])+'\t'+str(sipdirc[every_sip][1])+'\t'+str(sipdirc[every_sip][2])+'\t'+str(sipdirc[every_sip][3])+'\t'+str(sipdirc[every_sip][4])+'\t'+str(sipdirc[every_sip][5]))
        final_file.write('\n')
    final_file.close()
    sip_file.close()
    sip_file.close
    
    
    