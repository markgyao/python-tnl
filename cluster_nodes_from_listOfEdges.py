import networkx as nx
import matplotlib.pyplot as plt
def netwkxPlotDic(G,dic0):
    #get keys as list
    #keys=list(dic0.keys())
    #G.add_nodes_from(keys)
    
    for key in dic:
        #G.add_path(dic[key])
        G.add_path(dic[key], weight=key)
    edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
    nx.draw(G, with_labels=True, node_size=600,  edgelist=edges,edge_color=weights,width=2.0)
    plt.draw()
    plt.show()

    
def netwkxPlotLst(G,ls):
    
    for l in ls:
        #G.add_path(dic[key])
        G.add_edge(l[0],l[1])
    
    nx.draw(G, with_labels=True, node_size=600)
    plt.draw()
    plt.show()



ln=0
#ls=[[1,2],[2,3],[9,11],[4,5],[6,9],[7,6],[9,7],[4,3],[2,6]]
ls=[[1,2],[2,3],[9,11],[4,5],[6,9],[7,6],[9,7]]
#ls=[[1,2],[2,3]]

def nln():
    global ln
    ln=ln+1
    return ln

dic=dict()
for l in ls:
    jl=[]
    for key in dic:
        if not dic[key].isdisjoint(l):
            jl.append(key)
    
    if len(jl)>0:
        s=set(l)
        for i in jl:
            s.update(dic[i])
            #print "update s", s
            del dic[i]
        dic[nln()]=s
    else:
        dic[nln()]=set(l)
        
for key in dic:
    print key,dic[key]
    
G=nx.Graph()
netwkxPlotLst(G, ls)
