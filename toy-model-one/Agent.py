

class Agent():
    def __init__(self, id, t, θ, b0, δ, u, rule):
        self.id = id
        self.birth = t
        self.θ = θ
        self.b = b0
        self.δ = δ
        self.u = u
        self.ρ = 0.5
        self.rule = rule
        self.matches = []
        self.rs_given = []
        self.rs_received = []
        self.gs_matches = []

    def swipe(self, partner):
        if partner.θ > self.rule[self.b - 1]:
            self.b = self.b - 1
            self.rs_given.append((partner.id, partner.birth, partner.θ))
            return True
        return False    


    def update(self, ai, aj, partner):
        if ai and aj:
            self.matches.append((partner.id, partner.birth, partner.θ))
            self.ρ = len(self.matches)/len(self.rs_given)
        elif aj:
            self.rs_received.append((partner.id, partner.birth, partner.θ))


    def kill(self, t):
        self.death = t
        

