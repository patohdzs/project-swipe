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
        self.matches = 0
        self.rs_given = 0 # ids of agents that were given rs
        self.rs_received = 0 # ids of agents who gave rs

    def swipe(self, partner, t):
        if (partner.θ > self.rule[self.b - 1]):
            self.b -= 1
            if (self.b<0):
                print(f'ouch... something wrong with {self.sex} {self.id} @t={t}')
            self.rs_given += 1
            return True
        return False    
        
    def update(self, ai, aj, t):
        if ai and aj:
            self.matches += 1
            self.observed_ρ = self.matches/(t-self.birth+1)

        if aj:
            self.rs_received += 1
            self.true_ρ = self.rs_received/(t-self.birth+1) 

    def info(self, batch, t):
        return {'batch' : batch,
                'id' : self.id,
                'time' : t, 
                'birth' : self.birth,
                'sex' : self.sex, 
                'attractiveness' : self.θ, 
                'budget' : self.b, 
                'observed_rate' : self.observed_ρ, 
                'true_rate' : self.true_ρ,  
                'matches' : self.matches, 
                'rs_given' : self.rs_given, 
                'rs_received' : self.rs_received}

def kill(agent, platform, t):
    agent.death = t
    platform.remove(agent)


        

