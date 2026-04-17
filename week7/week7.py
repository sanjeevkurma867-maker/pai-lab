# States and observations
states = ['Rainy', 'Sunny']
observations = ['walk', 'shop', 'clean']

# Initial probabilities
start_prob = {'Rainy': 0.6, 'Sunny': 0.4}

# Transition probabilities
transition_prob = {
    'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny': {'Rainy': 0.4, 'Sunny': 0.6}
}

# Emission probabilities
emission_prob = {
    'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}
}

# Observation sequence
obs_sequence = ['walk', 'shop', 'clean']


def forward_algorithm(states, obs, start_p, trans_p, emit_p):
    forward = []

    # Initialization
    f0 = {}
    for s in states:
        f0[s] = start_p[s] * emit_p[s][obs[0]]
    forward.append(f0)

    # Recursion
    for t in range(1, len(obs)):
        ft = {}
        for curr in states:
            total = 0
            for prev in states:
                total += forward[t-1][prev] * trans_p[prev][curr]
            ft[curr] = total * emit_p[curr][obs[t]]
        forward.append(ft)

    # Termination
    return sum(forward[-1].values())


# Run
result = forward_algorithm(states, obs_sequence, start_prob, transition_prob, emission_prob)
print("Probability:", result)
