

class Agent():
    def __init__(self, t, θ, b0, δ, u, ρ, α, β):
        self.birth = t
        self.θ = θ
        self.b = b0
        self.δ = δ
        self.u = u
        self.ρ = ρ
        self.α = α
        self.β = β
        self.matches = []
        self.rs_given = []
        self.rs_received = []
        
    def update(self, Agent):
        pass

    def kill(self):
        pass

