
def norm(min_number,max_number,old_number):
    
    norm_number = (old_number - min_number) / float(max_number - min_number)
    return norm_number
def norm360data(data_path,result_path):
    data_file = open(data_path)
    lines = data_file.readlines()
    sip_list = []
    total_request_list = []
    avglen_uri_list = []
    avgpara_cookie_list = []
    avgpara_uri_list = []
    get_request_list = []
    post_request_list = []
    for line in lines:
        line = line.split('\t')
        sip = line[0]
        total_request = float(line[1])
        avglen_uri = float(line[2])
        avgpara_cookie = float(line[3])
        avgpara_uri = float(line[4])
        get_request = float(line[5])
        post_request = float(line[6])
        sip_list.append(sip)
        total_request_list.append(total_request)
        avglen_uri_list.append(avglen_uri)
        avgpara_cookie_list.append(avgpara_cookie)
        avgpara_uri_list.append(avgpara_uri)
        get_request_list.append(get_request)
        post_request_list.append(post_request)
    name_list = [total_request_list,avglen_uri_list,avgpara_cookie_list,avgpara_uri_list,get_request_list,post_request_list]
    for name in name_list:
        list_min = min(name)
        list_max = max(name)
        index_number = 0
        for item in name:
            item = norm(list_min,list_max,item)
            name[index_number] = item
            index_number += 1
    num_sample = len(sip_list)
    result_file = open(result_path,'w')
    for i in range(num_sample):
        result_file.write(sip_list[i]+'\t'+str(total_request_list[i])+'\t'+str(avglen_uri_list[i])+'\t'+str(avgpara_cookie_list[i])+'\t'+str(avgpara_uri_list[i])+'\t'+str(get_request_list[i])+'\t'+str(post_request_list[i]))
        result_file.write('\n')
    print  name_list[0]          
    data_file.close()
    result_file.close()
      
        
        
        

if __name__ == '__main__':
    norm360data('final_clustring.txt','final_norm_clustering.txt')
    