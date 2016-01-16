if __name__ == '__main__':
    file_path = 'http_sip_method.txt'
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
    
    sum_file = open('sum_file.txt','w')
    
    for every_sip in sipdirc.keys():
        #print every_sip
        sip_length = len(sipdirc[every_sip])       
        sum_list = []
        if sip_length == 1:
            sum_list = sipdirc[every_sip][0]
        elif sip_length == 2:            
            sum_list = [x+y for x, y in zip(sipdirc[every_sip][0], sipdirc[every_sip][1])]
        elif sip_length == 3:            
            sum_list = [x+y+z for x, y,z in zip(sipdirc[every_sip][0], sipdirc[every_sip][1],sipdirc[every_sip][2])]
        elif sip_length == 4:            
            sum_list = [x+y+z+w for x, y, z, w in zip(sipdirc[every_sip][0], sipdirc[every_sip][1],sipdirc[every_sip][2],sipdirc[every_sip][3])]
        elif sip_length == 5:            
            sum_list = [x+y+z+w+b for x, y, z, w,b in zip(sipdirc[every_sip][0], sipdirc[every_sip][1],sipdirc[every_sip][2],sipdirc[every_sip][3],sipdirc[every_sip][4])]
        elif sip_length == 6:            
            sum_list = [x+y+z+w+b+s for x, y, z, w,b,s in zip(sipdirc[every_sip][0], sipdirc[every_sip][1],sipdirc[every_sip][2],sipdirc[every_sip][3],sipdirc[every_sip][4],sipdirc[every_sip][5])]
        elif sip_length == 7:            
            sum_list = [x+y+z+w+b+s+q for x, y, z, w,b,s,q in zip(sipdirc[every_sip][0], sipdirc[every_sip][1],sipdirc[every_sip][2],sipdirc[every_sip][3],sipdirc[every_sip][4],sipdirc[every_sip][5],sipdirc[every_sip][6])]
        elif sip_length == 8:            
            sum_list = [x+y+z+w+b+s+q+e for x, y, z, w,b,s,q,e in zip(sipdirc[every_sip][0], sipdirc[every_sip][1],sipdirc[every_sip][2],sipdirc[every_sip][3],sipdirc[every_sip][4],sipdirc[every_sip][5],sipdirc[every_sip][6],sipdirc[every_sip][7])]
        elif sip_length == 9:            
            sum_list = [x+y+z+w+b+s+q+e+r for x, y, z, w,b,s,q,e,r in zip(sipdirc[every_sip][0], sipdirc[every_sip][1],sipdirc[every_sip][2],sipdirc[every_sip][3],sipdirc[every_sip][4],sipdirc[every_sip][5],sipdirc[every_sip][6],sipdirc[every_sip][7],sipdirc[every_sip][8])]
        
        #print every_sip
        #print sum_list
        sum_file.write(every_sip +'\t'+str(sum_list[0])+'\t'+str(sum_list[1])+'\t'+str(sum_list[2])+'\t'+str(sum_list[3]))
        sum_file.write('\n')
        #sipdirc[sip]
        
    sum_file.close()
    data_file.close()