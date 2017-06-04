
def propagate_trust(network, trust_scores):
	updated_scores = {}
	for n in network:
		new_trust = 0.0
		neighboors = network[n]
		for u in neighboors:
			u_degree = len(network[u])
			new_trust += trust_scores[u] / float(u_degree)
		updated_scores[n] = new_trust
	return updated_scores

def sybilrank(network,n_iter,trust_nodes,init_trust_score):
	print("*** Initing SybilRank ***")
	print("Total iterations: " + str(n_iter))
	trust_scores = {}
	for n in network: trust_scores[n] = 0.0
	for n in trust_nodes: trust_scores[n] = init_trust_score

	for i in range(n_iter):
		print('Iteration ' + str(i+1))
		trust_scores = propagate_trust(network, trust_scores)

	return trust_scores