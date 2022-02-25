# Model One: Budget-Constrained Swiping
## Setup
### Life, actions, and payoffs
- In essence, the Tinder platform represents to an agent a sequence of suggested partners
- The agent faces an infinite horizon, with time indexed as $t=1,2,...$ and a 'death rate' $(1-\delta)$
    - An agent can 'die' either because Tinder runs out of suggestions for her, or becuase she decides to quit
- EEach suggested partner can be viewed as a Bernoulli-type lottery with some corresponding attractiveness payoff drawn i.i.d from a beta distribution with c.d.f $F$ and a fixed probability of ‘right-swiping back’
    - $\left[\,\theta_t,0\;;\;\rho,(1-\rho)\,\right]$
- For each suggestion, the agent decides whether to 'participate in the lottery'
    - $a_t=\begin{cases}1 & \text{swipe right}\\0 & \text{swipe left}\end{cases}$
- Given the agent participates, expected utility from matching is $U(\theta_t,a_t ) = \rho\, a_tu(\theta_t)$, where $u(\cdot)$ is a v-NM utility function satisfying $u(0)=0$
    - This is important because, if $u(0)<0$, then matching with some (ugly) people is worse than just skipping them


### Costly swiping
- Left swiping is costly as the agent can die the next round, so why not swipe right on everyone?
- Tinder makes right-swiping costly by placing a cap on the total number of right swipes for each user. We refer to this as the agent’s budget $b_t$   
- The budget is evolves dynamically according to the law of motion:
    - $b_{t+1}= b_t  - a_t$
- The starting budget, $b_0$, is determined exogenously 

## The Agent's Problem 
$$
 \begin{aligned} \max_{\{a_t\}^\infty_{t=0}} \quad & \mathbb{E}_{\theta_t}\left[\sum^\infty_{t=0} \delta^{t} U(\theta_t,a_t) \right]\\\\ \textrm{s.t.} \quad &b_{t+1}  = b_t -a_t \\ &b_t\in \{b_0\,\,...,0\} \\ & a_t\in \{0,1\} \\ & \theta_t \sim \text{Beta}(\alpha, \beta)\end{aligned}
$$

## Solving the model

- Define the set of stationary Markov policies $\Pi$ such that $\pi: \Theta \times \mathcal{B} \rightarrow\mathcal{A}$
- The value function for this problem is given by:

$$
V(\theta, b)= \max_{\pi}\;\mathbb{E}_{\pi}\left[\sum^\infty_{t=1} \delta^{t-1}  U(\theta_t, \pi(\theta_t, b_t)) \,|\, \theta_0,b_0=\theta,b\right] 
$$

- Corresponding Bellman equation of the agent's problem (drop time subscript to highlight stationarity):

$$
 V(\theta, b)=\max \, \left \{\,\rho u(\theta) +\delta \,\mathbb{E}_{\theta'}\left[V(\theta, b-1)\right] \,,\;\delta \,\mathbb{E}_{\theta'}\left[\,V(\theta',b )\,\right]\,\right\}
$$

- Optimal policy can be parametarized by a cutoff attractiveness due to the piecewise nature of the value function:

$$
 \pi^*(\theta,b)=\begin{cases}1,\quad \theta\geq\theta^*_b \\ 0, \quad\theta<\theta^*_b  \end{cases}
$$
    
- Cutoff attractiveness  $\theta^*_b$ is naturally defined such that the current period utility of a right-swipe is equal to the discounted loss in expected value from a unit decrease in budget :

$$
 \rho u(\theta^*_b) = \delta \,\mathbb{E}_{\theta'}\left[\,V(\theta',b)-V(\theta',b-1)\,\right]
$$

- We can see how this creates the piecewise nature of value function (graph in notebook) :
    - Note that continuation value $\mathbb{E}_{\theta'}\left[V(\theta', b)\right]$ is a constant for all $b\in\mathcal{B}$

$$
 V(\theta, b)=\begin{cases}\rho u(\theta) +\delta \,\mathbb{E}_{\theta'}\left[V(\theta', b-1)\right],\quad \theta>\theta^*_b \\\\ \delta \,\mathbb{E}_{\theta'}\left[V(\theta', b)\right],\quad \theta\leq\theta^*_b\end{cases}
$$

- The explicit threshold at different budget levels are determined by the two equations below
    - The first equation defines an implicit recursive relation  $\theta^*_b = \varphi(\theta^*_{b-1})$ , and is derived by evaluating $(2)$ and $(3)$
    - The second one can be solved for $\theta^*_1$ to provide an initial condition, and is derived by combining and evaluating $(2)$, $(3)$ and the initial condition $V(\theta,0)=0$

$$
 u(\theta^*_b) = \delta u(\theta^*_b) F(\theta^*_b) \,+\, \delta u(\theta^*_{b-1})\left[1-  F(\theta^*_{b-1})\right]\,+\,\delta\int^{\theta^*_{b-1}}_{\theta^*_b} u(\theta')dF(\theta')
$$

$$
u(\theta^*_1) =\delta u(\theta^*_1)F(\theta^*_1) + \delta \int^1_{\theta^*_1}u(\theta')dF(\theta')
$$