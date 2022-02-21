# Optimality conditions
def equilibrium_condsG(x):
    """
    Takes in 1x(Bm+Bw) vector
    Male cutoffs first
    """
    # Compute z's
    def zm(b): 
        if b==Bm:
            return (1-2*δ*Fw.cdf(x[Bm-1]))
        z=1
        for i in range(1, Bm-b+1): 
            z *= δ*(1-Fw.cdf(x[Bm-i]))/(1-2*δ*Fw.cdf(x[Bm-i-1]))
        return z
    
    def zw(b): 
        if b==Bw:
            return (1-2*δ*Fm.cdf(x[Bm+Bw-1]))
        z=1
        for i in range(1, Bw-b+1): 
            z *= δ*(1-Fm.cdf(x[Bm+Bw-i]))/(1-2*δ*Fm.cdf(x[Bm+Bw-i-1]))
        return z 
    
    # Computing steady-state masses
    Nm = λm*((zm(Bm) - δ*zm(1)*(1-Fw.cdf(x[0])))/((1-δ)*zm(Bm)))
    Nw = λw*((zw(Bw) - δ*zw(1)*(1-Fm.cdf(x[Bm])))/((1-δ)*zw(Bw)))  
    # Computing tightness and alpha
    if Nw>Nm:
        τm = 1
    else:
        τm = Nw/Nm 
        
    τw = τm *(Nm/Nw) 
    αm = (τm*δ)/(1-δ*(1-τm))
    αw = (τw*δ)/(1-δ*(1-τw)) 
    
    # Computing ex-ante expected utilities
    Um = lambda θ : u(θ)*(sum([intg.quad(lambda t: u(t) * Fw.pdf(t), x[0], 1)[0]
                               for b in range()]))
    Uw = lambda θ : u(θ)*(sum([intg.quad(lambda t: u(t) * Fw.pdf(t), x[0], 1)[0]
                               for b in range()]))
    
    # Initialysing system of equilibrium equations
    S = np.empty(Bm+Bw)
    
    # Initial conditions 
    S[0] = (u(x[0]) 
            - αm * u(x[0]) * Fw.cdf(x[0]) 
            - αm * intg.quad(lambda t: u(t) * Fw.pdf(t), x[0], 1)[0])
    
    S[Bm] = (u(x[Bm]) 
            - αw * u(x[Bm]) * Fm.cdf(x[Bm]) 
            - αw * intg.quad(lambda t: u(t) * Fm.pdf(t), x[Bm], 1)[0])
    
    # Optimality conditions for men
    for b in range(1,Bm):
        S[b] = (u(x[b]) 
                - αm * u(x[b]) * Fw.cdf(x[b]) 
                - αm * u(x[b-1])*(1-Fw.cdf(x[b-1])) 
                - αm * intg.quad(lambda t : u(t) * Fw.pdf(t), x[b], x[b-1])[0])
    
    # Optimality conditions for women
    for b in range(1,Bw):
        S[Bm+b] = (u(x[Bm+b]) 
                - αw * u(x[Bm+b]) * Fm.cdf(x[Bm+b]) 
                - αw * u(x[Bm+b-1])*(1-Fm.cdf(x[Bm+b-1])) 
                - αw * intg.quad(lambda t : u(t) * Fm.pdf(t), x[Bm+b], x[Bm+b-1])[0])
            
    return S 