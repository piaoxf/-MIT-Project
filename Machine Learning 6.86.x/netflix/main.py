import numpy as np
import kmeans
import common
import naive_em
import em

X = np.loadtxt("toy_data.txt")
# # TODO: Your code here
K = [1, 2, 3, 4]
seed = [0, 1, 2, 3, 4]
<<<<<<< HEAD
=======
# for i in K:
#     result = []
#     for j in seed:
#         GaussianMixture, post = common.init(X=X, K=i, seed=j)
#         mixture, post, cost = kmeans.run(X, GaussianMixture, post)
#         result.append(cost)

#         # cost
#         print("K", i, "seed", j, "cost", cost)
    
#     print("min cost", np.array(result).min())
new_log_likelihood = []
bic_score = []
>>>>>>> a4fe8accdd4aff2974d916767ceebf64458c11aa
for i in K:
    result = []
    for j in seed:
        GaussianMixture, post = common.init(X=X, K=i, seed=j)
<<<<<<< HEAD
        mixture, post, cost = kmeans.run(X, GaussianMixture, post)
        result.append(cost)

        GaussianMixture_em, post_em = common.init(X=X, K=i, seed=j)
        mixture_em, post_em, log_likelihood_em = naive_em.run(X, GaussianMixture_em, post_em)
        result.append(log_likelihood_em)

        # cost
    #     print("K", i, "seed", j, "cost", cost)
    
    # print("min cost", np.array(result).min())

    common.plot(X, mixture, post, title="KMeans")
    common.plot(X, mixture_em, post_em, title="Gausian Mixture")

# for i in K:
#     result = []
#     for j in seed:
#         GaussianMixture, post = common.init(X=X, K=i, seed=j)
#         mixture, post, log_likelihood = naive_em.run(X, GaussianMixture, post)
#         result.append(log_likelihood)

#         # log likelihood
#         print("K", i, "seed", j, "log_likelihood", log_likelihood)
    
#     # print("min log_likelihood", np.array(result).min())
# common.plot(X, mixture, post, title="Gausian Mixture")
=======
        mixture, post, log_likelihood = naive_em.run(X, GaussianMixture, post)
        result.append(log_likelihood)
        new_log_likelihood.append(log_likelihood)
        # log likelihood
        # print("K", i, "seed", j, "log_likelihood", log_likelihood)
        bic_score.append(common.bic(X=X, mixture=mixture, log_likelihood=log_likelihood))
        # print("bic: ", bic_score)
    # print("min log_likelihood", np.array(result).min())
# common.plot(X, mixture, post, title="Gausian Mixture")

print(np.array(new_log_likelihood))
print(np.array(bic_score))
print(np.array(new_log_likelihood).max(), np.array(bic_score).max())
>>>>>>> a4fe8accdd4aff2974d916767ceebf64458c11aa
