import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import euclidean



def gen_data_2d(n, mu=np.array([0, 0]), cov=np.array([[1, 0], [0, 1]])):
    ''' 
    sample from a 2D gaussian
    '''
    val = np.random.multivariate_normal(mu, cov, size=n)
    return val


def gen_clusters(n, k):
    '''
    create k sample clusters
    '''
    mu_lst = np.random.randint(20, size = 2*k).reshape(k,2)
    lst = []
    for i in range(len(mu_lst)):
        val = gen_data_2d(n // k, mu=mu_lst[i])
        lst += list(val)
    return np.array(lst)


def cluster_data(mu_lst, data):
    '''
    '''
    cluster_lst = [[] for val in range(len(mu_lst))]

    prelist = []
    for i in range(len(mu_lst)):
        com_diff = []
        for j in range(len(data)):
            com_diff.append(euclidean(data[j], mu_lst[i]))
        while True:
            k = np.argmin(com_diff)
            if k not in prelist:
                prelist.append(k)
                cluster_lst[i].append(data[k])
                break
            else:
                com_diff[k] = float('inf')

    left_data = np.delete(data, prelist, 0)
    for row in left_data:
        tmp_diff = []
        for mu in mu_lst:
            tmp_diff.append(euclidean(row, mu))
        tmp_diff = np.array(tmp_diff)
        ind = np.argmin(tmp_diff)
        cluster_lst[ind].append(row)

    return cluster_lst






def cluster_mean(cluster_lst):
    rtn_ctrs = []
    for cluster in cluster_lst:
        tmp_mean = np.mean(np.array(cluster), axis=0)
        rtn_ctrs.append(tmp_mean)

    return np.array(rtn_ctrs)


def cluster_mean_diff(prior_cluster, current_cluster):
    dist = []
    for row1, row2 in zip(prior_cluster, current_cluster):
        dist.append(euclidean(row1, row2))
    return sum(dist)


def k_means(num_clusters, data):
    '''
    '''
    minx = np.min(data[:, 0])
    maxx = np.max(data[:, 0])
    miny = np.min(data[:, 1])
    maxy = np.max(data[:, 1])

    # initial centroids
    x_ini = np.random.uniform(low=minx, high=maxx, size=num_clusters)
    y_ini = np.random.uniform(low=miny, high=maxy, size=num_clusters)
    mu_initial = np.array([list(x_ini), list(y_ini)]).transpose()

    # idx = np.random.randint(len(data), size = num_clusters)
    # mu_initial = data[idx, :]
    cluster_prior = mu_initial
    cluster_means = mu_initial + 1

    i = 0
    centroid_diff = 1

    while centroid_diff > 1e-6:
        if i == 0:
            pass
        else:
            cluster_prior = cluster_means
        clusters = cluster_data(cluster_prior, data)
        cluster_means = cluster_mean(clusters)
        # import ipdb
        # ipdb.set_trace()
        centroid_diff = cluster_mean_diff(cluster_prior, cluster_means)
        i = i + 1


    return cluster_means


#    import ipdb
#    ipdb.set_trace()

def loss(data, cluster_means):
    loss_lst = []
    for i in range(len(data)):
        temp = []
        for j in range(len(cluster_means)):
            temp.append(euclidean(data[i], cluster_means[j]))
        loss_lst.append(temp[:])
    res = 0
    for i in range(len(loss_lst)):
        res += min(loss_lst[i])
    return res

def k_loss_draw(k, data):
    loss_lst = []
    k_lst = [i for i in range(1, k + 1)]
    for num_clusters in range(1, k + 1):
        cluster_means = k_means(num_clusters, data)
        loss_one = loss(data, cluster_means)
        loss_lst.append(loss_one)
    return [k_lst, loss_lst]

if __name__ == "__main__":
    print("test")

    n = 60
    init_clusters = 3
    num_clusters = 3
    if num_clusters > n:
        print("Error: cluster number is larger than data points number!")

    data = gen_clusters(n, init_clusters)
    cluster_means = k_means(num_clusters, data)

    # plt.figure()
    # plt.plot(data[:, 0], data[:, 1], 'bx')
    # plt.plot(cluster_means[:, 0], cluster_means[:, 1], 'k*', markersize=20)
    # plt.show()

    '''
    plot the k and loss figure
    '''

    kloss = k_loss_draw(10, data)
    plt.figure()
    plt.plot(kloss[0], kloss[1])
    plt.show()
