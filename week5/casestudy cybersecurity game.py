import math

# Possible attack actions
attacks = {
    "phishing": -20,
    "malware": -30,
    "ddos": -25,
    "password_attack": -15
}

# Possible defense actions
defenses = {
    "firewall_update": +20,
    "patch_system": +25,
    "enable_mfa": +15,
    "intrusion_detection": +18
}

# Evaluate system security score
def evaluate(score):
    return score


def minimax(score, depth, alpha, beta, isAttacker):

    # Stop condition
    if depth == 0 or score <= -100 or score >= 100:
        return evaluate(score)

    # Attacker turn (maximize damage)
    if isAttacker:
        best = -math.inf

        for attack in attacks:
            new_score = score + attacks[attack]

            value = minimax(new_score, depth-1, alpha, beta, False)

            best = max(best, value)
            alpha = max(alpha, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best

    # Defender turn (minimize damage)
    else:
        best = math.inf

        for defense in defenses:
            new_score = score + defenses[defense]

            value = minimax(new_score, depth-1, alpha, beta, True)

            best = min(best, value)
            beta = min(beta, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best


def best_attack_move(score, depth):

    best_value = -math.inf
    best_move = None

    for attack in attacks:
        new_score = score + attacks[attack]

        value = minimax(new_score, depth-1, -math.inf, math.inf, False)

        if value > best_value:
            best_value = value
            best_move = attack

    return best_move


# Simulation start
security_score = 50
depth = 3

print("Initial Security Score:", security_score)

attack = best_attack_move(security_score, depth)

print("Best attack chosen by attacker:", attack)
print("Security score after attack:", security_score + attacks[attack])











