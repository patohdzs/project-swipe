# Setup
## The Stage Interaction
- Consider the search market formed by the Tinder platform with both male and female agents, indexed $m$ and $w$ respectively, looking for potential partners.
- For ease of exposition, we assume that this market is heteronormative such that male agents search for female agents only and vice-versa.
- Time is discrete and indexed $t=0,1,...$ over an infinite horizon
- At every time period, agents from each sex are simultaneously presented a suggested partner from the opposite sex. 
- Each agent has an attractiveness type $\theta_i,\, i=m,w$ that is unknown to them but observable to their suggestion
- Agents then choose whether to swipe left or right on their suggestion, thus $\mathcal{A}_m=\mathcal{A}_w=\{ \text{left},\; \text{right}\}$
    - If both agents swipe right, they are said to have *matched*
    - If either agent swipes left, neither earns any payoff and they continue searching
    - Notice that the suggested partner’s action is only *observable* if one swipes right
- Upon matching, agents earn a payoff $u(\theta_{-i}),\, i=m,w$
    - We assume $u(\cdot)$ is strictly increasing, bounded, and satisfies $u(0)=0$ 
## Life, Death, and the Tinder Market
- The masses of men and women on Tinder at any given time period $t$ are denoted by $N^t_{m}$ and $N^t_{w}$, respectively.
- Each period, $\lambda_m$ new men and $\lambda_w$ new women arrive
    - The attractiveness of new male and female users is drawn i.i.d from exogenous distributions with c.d.f’s $F_m$ and $F_w$ respectively
- Agents leave the platform exogenously (ie. they ‘die’) at a rate of $(1-\delta)$ 
- Given sample spaces $\Theta_{m}\times \mathcal{B}_{m}$ and $\Theta_{w}\times \mathcal{B}_{w}$, let $\mathbb{P}_{m}$ and $\mathbb{P}_{w}$ be the probability measures over the their corresponding $\sigma$-algebras
    - Let $M^t,W^t:\Theta_{m,w}\times\mathcal{B}_{m,w}\rightarrow[0,1]$ be the endogenous mixed distributions over agents (male and female, respectively) in the platform defined as:
        
        $$
        M^t(\theta,b)=\mathbb{P}_m(\theta_m\leq\theta,b_m\leq b),\quad W^t(\theta,b)=\mathbb{P}_w(\theta_w\leq\theta,b_w\leq b)
        $$
        
    - These are endogenously determined since the flow of agents into lower budget levels and eventually out of the market depends on their swiping decisions, determined endogenously through a search process
    - Define $M^t_\theta(\theta),W^t_\theta(\theta)$ as the marginal c.d.f’s over male and female attractiveness:
        
$$
M^t(\theta,b)=\mathbb{P}_m(\theta_m\leq\theta,b_m\leq b),\quad W^t(\theta,b)=\mathbb{P}_w(\theta_w\leq\theta,b_w\leq b)
$$
    - Define $M^t_b(b),W^t_b(b)$ as the marginal c.d.f’s over male and female budgets:
        
$$
M_b^t(\theta)=\mathbb{P}(b_m\leq b), \quad W_b^t(\theta)=\mathbb{P}(b_w\leq b)
$$
        
- The Tinder market at $t$ is thus defined as $\Psi^t=(N^t_m,N^t_w,M^t,W^t)$ 

## Budgeted Swiping
- Left swiping is costly as the agent can die the next round, so why not swipe right on everyone?
- Tinder makes right-swiping costly by placing a cap on the total number of right swipes for each user. We refer to this as the agent’s budget $b_t$
- The budget is evolves dynamically according to the law of motion:
    
    $$
    b_{t+1}= b_{t}- a_{t}
    $$
    
- The starting budgets for each sex, $B_{m}$ and $B_{w}$, are determined exogenously
- Given this, an agent’s decision on any given time period depends fundamentally on the attractiveness of the suggested partner and their own budget
- We only consider stationary Markov strategies, defines for men as functions $\mu:\Theta_w \times\mathcal{B}_m\rightarrow \Delta\mathcal{A}_m$ and for women as $\omega:\Theta_m \times\mathcal{B}_w\rightarrow \Delta\mathcal{A}_w$
    

# The Steady State Market

- When talking steady state we omit time subscripts to denote stationarity
- Denote by $M(\cdot\,;\mu,\omega)$, $W(\cdot\,;\mu,\omega)$ be the endogenous steady-state joint c.d.f’s for men and women that arise given the strategies $\mu$ and $\omega$
- $N_m(\mu,\omega),N_w(\mu,\omega)$ are defined analogously

### Theorem 1: Steady State Characterisation

- Fix some strategies $\mu, \omega$ and let the expected probabilities of a right swipe be:

$$
\rho^m_b=\int_{\Theta_w}  \mu(\theta',b)\,dW_\theta(\theta';\mu,\omega), \quad \rho^w_b=\int_{\Theta_m} \omega(\theta',b)\,dM_\theta(\theta';\mu,\omega) 
$$

- Furthermore, let:

$$
\begin{aligned} z^m_b &=\prod^{B-b}_{i=1}\frac{\delta\rho^m_{B-i+1}}{\Big(1-\delta (1-\rho^m_{B-i}) \Big)}, \quad \forall b=1,...,B_m-1\\z^w_b&=\prod^{B-b}_{i=1}\frac{\delta\rho^w_{B-i+1}}{\Big(1-\delta (1-\rho^w_{B-i}) \Big)} , \quad \forall b=1,...,B_w-1\\\\ z^m_B&=\Big(1-\delta (1-\rho^m_B) \Big),\quad z^w_B=\Big(1-\delta (1-\rho^w_B) \Big) \end{aligned}
$$

- Then the steady state is given by:

$$
\begin{aligned}N_m(\mu,\omega)&=\lambda_m\left(\frac{z^m_B-\delta z^m_1\rho^m_1}{(1-\delta)z^m_B}\right)\\\\N_w(\mu,\omega)&=\lambda_w\left(\frac{z^w_B-\delta z^w_1\rho^w_1}{(1-\delta)z^w_B}\right)\\\\M(\theta,b;\mu,\omega)&=F_m(\theta) \left(\frac{(1-\delta)}{z^m_B-\delta z^m_1\rho^m_1}\right)\sum^b_{i=1} z^m_i\\\\W(\theta,b;\mu,\omega)&=F_w(\theta)\left(\frac{(1-\delta)}{z^w_B-\delta z^w_1\rho^w_1}\right)\sum^b_{i=1} z^w_i \end{aligned}
$$

- Furthermore, for each sex, the agent’s budget and attractiveness are conditionally independent given both swiping strategies


# The Love Search Problem

- We analyse the problem of allocating a man’s limited swipes in a steady state market $\Psi$ against a female strategy $\omega$, and consider these fixed in the remainder of this section
    - With an abuse of notation, this implies that the functions $U_m(\theta;\omega, \Psi),\,V_m(\theta,b;\omega,\Psi), \,\widetilde\mu(\theta, b;\omega,\Psi)$ are writen as $U_m(\theta),\,V_m(\theta,b), \,\widetilde\mu(\theta, b)$
    - Furthermore, arguments for the women's side of the market follow analogously

## The Stage Game

- The *ex-interim* expected utility of swiping left is always zero
- The *ex-interim* expected utility of swiping right is given by:

$$
U_m(\theta,b) =  u(\theta)\left(\sum_{b\in \mathcal{B}}\int_{\Theta_m} \omega(\theta_m,b_w)\,\mathbb{P}_w(b_w|\theta_w=\theta)\,dM_{\theta}(\theta_m|b_m=b)\right)
$$

- Because we’ve shown that an agent’s budget and attractiveness are independent of one another at the steady state, this simplifies to:

$$
\begin{aligned}
U_m(\theta )=  u(\theta)\left(\sum_{b\in \mathcal{B}}\int_{\Theta_m} \omega(\theta',b')\,\mathbb{P}_w(b_w=b')\,dF_m(\theta')\right)\end{aligned}
$$



- Without swiping constraints, it is dominant to swipe right, unless, $\omega(\theta,b)=0,\quad \forall\theta,b\in\Theta_m \times\mathcal{B}_m$, in which case it is weakly dominant. Nevertheless, the agent playing a sequence of these has a superimposed inter-temporal swipe-budgeting problem to solve.

## The Swipe Budgeting Problem

- If there is a sex imbalance, not every agent gets a suggestion in every period
    - Assuming frictionless search, men get suggestions at a rate $\tau=\min\{\frac{N_w}{N_m} ,1\}$
    - This then leads to an effective discount rate $ \alpha=\frac{\tau\delta}{1-\delta(1-\tau)} $

- Agents maximise their expected lifetime sum of discounted payoffs, thus solving the problem:

$$ 
\begin{aligned}V_m(\theta,b)= \max_{\{a_t\}^\infty_{t=0}} \;& \mathbb{E}_{\Psi}\left[\sum^\infty_{t=0} \alpha^{t} U_m(\theta_t,a_t)\;|\; \theta_0,b_0=\theta,b\right] \\\\ \textrm{s.t.}\; & \theta_t \sim F_w,\\ & b_{t+1}  = b_t - a_t \\ &b_t\in \mathcal{B}, \quad a_t\in \mathcal{A} \end{aligned} 
$$

- This problem admits the Bellman equation

$$
\begin{aligned} V_m(\theta,b) \;=\;&\max\left\{\,U_m(\theta) +\alpha \,\mathbb{E}_{\Psi}\Big[V_m(\theta', b-1)\Big]\,,\; \alpha\,\mathbb{E}_\Psi\Big[ V_m(\theta', b)\Big]\,\right\} \end{aligned}
$$

- The optimal policy is parametrised by a cutoff attractiveness due to the piecewise nature of the value function:
    - Agent swipes right when current period reward is greater than the discounted loss in expected value from a unit decrease in budget.

$$
\widetilde\mu(\theta,b)=\begin{cases}1,\quad \theta\geq \widetilde{\mu}_b \\ 0, \quad\theta< \widetilde\mu_b  \end{cases}
$$

- Cutoff attractiveness $\widetilde\mu_b$ is naturally defined such that the current period utility of a right-swipe is equal to the discounted loss in expected value from a unit decrease in budget :

$$
 \begin{equation} u(\widetilde\mu_b) = \alpha \, \mathbb{E}_{\Psi}\Big[\,V(\theta',b)-V(\theta',b-1)\,\Big] \end{equation}
$$

- This ilustrates piecewise nature of value function (graph in notebook) :
    - Note $\mathbb{E}_{\Psi}\left[V(\theta', b)\right]$ is a constant for all $b\in\mathcal{B}$

$$
 \begin{equation}V(\theta, b)=\begin{cases}u(\theta) +\alpha \,\mathbb{E}_{\Psi}\Big[V(\theta', b-1)\Big],\quad \theta> \widetilde \mu_b \\\\ \alpha \,\mathbb{E}_{\Psi}\Big[V(\theta', b)\Big],\quad \theta\leq\widetilde \mu_b\end{cases}  \end{equation}
$$

- After some algebra, it is shown that the explicit thresholds at different budget levels follow the reccurence relations determined by thetwo equations below

$$
 u(\widetilde \mu_b) = \alpha u(\widetilde \mu_b) F_w(\widetilde \mu_b) + \alpha u(\widetilde \mu_{b-1})\Big(1- F_w(\widetilde \mu_{b-1})\Big)+\int^{\widetilde \mu_{b-1}}_{\widetilde \mu_b} \alpha u(\theta')\,dF_w(\theta')
$$

$$
 u(\widetilde \mu_1) = \alpha  u(\widetilde\mu_1) F_w(\widetilde\mu_1) + \int^1_{\widetilde\mu_1} \alpha u(\theta')\,dF_w(\theta')
$$

# Tinder Equilibrium

## Defining a Stationary Markov Ex-Ante Equilibrium

- A pair of strategies $\mu^*,\omega^*$ parametrised by cutoffs $\mu^*_b,\, \forall b \in \mathcal{B}_m$ and $\omega^*_b,\;\forall b \in \mathcal{B}_w$, respectively, along with a steady-state market $\Psi^*$ is a Stationary Markov Equilibrium if:
    1. $\mu^*_b=\widetilde \mu(b;\omega^*, \Psi^*),\quad\forall b\in\mathcal{B}_m$
    2. $\omega^*_b=\widetilde\omega(b;\mu^*, \Psi^*),\quad\forall b\in\mathcal{B}_w$
    3. $\Psi^*= \Psi(\mu^*,\omega^*)$
- What does this mean?
    - (1) means that the male cutoffs at every budget level solve the swipe-budgeting problem for men at market $\Psi^*$ and best-respond to $\omega^*$
    - (2) means that the female cutoffs at every budget level solve the swipe-budgeting problem for women at market $\Psi^*$ and best-respond to $\mu^*$
    - (3) means that market $\Psi^*$ is sustained as a steady-state when agents employ strategies $\mu^*,\omega^*$
    - This means that: agents do not wish to change their strategies as they both best-respond and optimise their lifelong discounted sum of payoffs given a particular market
    - The market does not change given agent’s behaviour

