from sklearn.cluster import Birch
from numpy import source

def data2birch(file_path):
    data_list = []
    data_dirc = {}
    data_file = open(file_path)
    lines = data_file.readlines()
    for line in lines:
        curlist = []
        line = line.split('\t')
        sip = line[0]
        total_request = float(line[1])
        avglen_uri = float(line[2])
        avgpara_cookie = float(line[3])
        avgpara_uri = float(line[4])
        get_request = float(line[5])
        post_request = float(line[6])
        curlist = [total_request,avglen_uri,avgpara_cookie,avgpara_uri,get_request,post_request]
        data_list.append(curlist)
        data_dirc[sip] = curlist
    return data_list,data_dirc

def birchclustering(datalist):
    brc = Birch(branching_factor=50, n_clusters=None, threshold=0.17,compute_labels=True)
    brc.fit(datalist)
    return brc
    #print brc.predict(datalist)
def centerdirc(data_dirc,brc):
    cluster_dirc = {}
    for sip in data_dirc.keys():
        curresult = brc.predict(data_dirc[sip])
        curresult = curresult.tolist()[0]
        if curresult not in cluster_dirc:
            cluster_dirc[curresult] = []
            cluster_dirc[curresult].append(sip)
        else:
            cluster_dirc[curresult].append(sip)
    return cluster_dirc
def centermean(cluster_dirc,source_data_dirc):
    mean_dirc = {}
    len_list = []
    for every_cluster in cluster_dirc.keys():
        mena_index_list= []
        cluster_sips = cluster_dirc[every_cluster]
        num_cluster_sips = len(cluster_sips)
        print 'cluster: ' +str(every_cluster) +'has : '+str(num_cluster_sips) +' member'
        cluster_list = [0.0,0.0,0.0,0.0,0.0,0.0]
        for sip in cluster_sips:
            cluster_list = [x+y for x, y in zip(source_data_dirc[sip],cluster_list)]
        for i in range(6):
            mean_number = cluster_list[i]/ float(num_cluster_sips)
            mena_index_list.append(mean_number)
        mean_dirc[every_cluster] = mena_index_list
    for item in mean_dirc.keys():
        print 'cluster '+str(item)+' mean is : ' + str(mean_dirc[item])
    
    
    
if __name__ == '__main__':
    norm_file_path = 'final_norm_clustering.txt'
    source_file_path = 'final_clustring.txt'
    norm_data_list,norm_data_dirc = data2birch(norm_file_path)
    source_data_list,source_data_dirc = data2birch(source_file_path)
    brc = birchclustering(norm_data_list)
    cluster_dirc = centerdirc(norm_data_dirc,brc)
    centermean(cluster_dirc,source_data_dirc)
    
    