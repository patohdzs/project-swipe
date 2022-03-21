class Agent():
    def __init__(self, id, t, sex, θ, B, rule):
        self.id = id
        self.birth = t
        self.sex = sex
        self.θ = θ
        self.b = B 
        self.observed_ρ = 1
        self.true_ρ = 1
        self.rule = rule
        self.matches = []
        self.rs_given = [] # ids of agents that were given rs
        self.rs_received = [] # ids of agents who gave rs

    def swipe(self, partner):
        if partner.θ > self.rule[self.b - 1]:
            self.b = self.b - 1
            self.rs_given.append(partner.id)
            return True
        return False    
        
    def update(self, ai, aj, partner, t):
        if ai and aj:
            self.matches.append(partner.id)
            self.observed_ρ = len(self.matches)/(t-self.birth+1)

        if aj:
            self.rs_received.append(partner.id)
            self.true_ρ = len(self.rs_received)/(t-self.birth+1) 

    def info(self, t):
        return {'id':self.id,
                'time':t, 
                'birth':self.birth,
                'sex':self.sex, 
                'attractiveness':self.θ, 
                'budget':self.b, 
                'observed_rate':self.observed_ρ, 
                'true_rate':self.true_ρ,  
                'matches':self.matches.copy(), 
                'rs_given':self.rs_given.copy(), 
                'rs_received':self.rs_received.copy()}

def kill(agent, platform, t):
    agent.death = t
    platform.remove(agent)


        

