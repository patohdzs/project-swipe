import random

import numpy as np
from scipy.stats import bernoulli, beta, cumfreq


class Agent:
    def __init__(self, id, t, sex, θ, B, rule):
        """
        Constructor method for Agent

        Args:
            id (int): Agent ID
            t (int): Current time period
            sex (string): Agent sex (male or female)
            B (int): Starting swiping budget
            rule (list): Swiping rule to use
        """

        self.id = id
        self.birth = t
        self.sex = sex
        self.θ = θ
        self.b = B
        self.observed_ρ = 1
        self.true_ρ = 1
        self.rule = rule
        self.matches = 0
        self.rs_given = 0  # ids of agents that were given rs
        self.rs_received = 0  # ids of agents who gave rs

    def swipe(self, partner, t):
        """
        Swiping action method

        Args:
            partner (Agent): suggested partner
            t (int): current time period

        Returns:
            bool: Whether or not the agent swipes left (False) or right (True)
        """

        if partner.θ > self.rule[self.b - 1]:
            self.b -= 1
            if self.b < 0:
                print(f"ouch... something wrong with {self.sex} {self.id} @t={t}")
            self.rs_given += 1
            return True
        return False

    def update(self, ai, aj, t):
        if ai and aj:
            self.matches += 1
            self.observed_ρ = self.matches / (t - self.birth + 1)

        if aj:
            self.rs_received += 1
            self.true_ρ = self.rs_received / (t - self.birth + 1)

    def info(self, batch, t):
        """
        Accessor method for Agent

        Args:
            batch (int): Batch number
            t (int): Current time period

        Returns:
            dict: Dictionary with attribute values
        """

        return {
            "batch": batch,
            "id": self.id,
            "time": t,
            "birth": self.birth,
            "sex": self.sex,
            "attractiveness": self.θ,
            "budget": self.b,
            "observed_rate": self.observed_ρ,
            "true_rate": self.true_ρ,
            "matches": self.matches,
            "rs_given": self.rs_given,
            "rs_received": self.rs_received,
        }


def simulate_game(T, μ_star, ω_star, exog_params, batch=0, matches="random"):
    """
    Function used to simulate an SBDP game

    Args:
        T (int): Number of time periods
        exog_params (tuple): Exogenous model parameters
        batch (int, optional): Batch number (for multi-batch simulations). Defaults to 0.
        matches (str, optional): Matching process. Defaults to "random".

    Returns:
        list: Simulation logs
    """

    Bm, Bw, bm_vals, bw_vals, δ, um, uw, Fm, Fw, λm, λw = exog_params
    simulation = []
    men = []
    women = []
    for t in range(0, T):
        # Add new agents
        for i, θ in enumerate(Fm.rvs(size=λm)):
            men.append(Agent(t * λm + i, t, "Male", θ, Bm, μ_star))

        for i, θ in enumerate(Fw.rvs(size=λw)):
            women.append(Agent(t * λw + i, t, "Female", θ, Bw, ω_star))

        # Gameplay
        random.shuffle(men)
        random.shuffle(women)
        pairs = zip(men, women)

        if (matches == "gale-shapley") or (matches == "gs"):
            s_men, s_women = zip(*pairs)
            s_men = sorted(s_men, key=lambda m: m.θ)
            s_women = sorted(s_women, key=lambda w: w.θ)
            pairs = zip(s_men, s_women)

        for m, w in pairs:
            am = m.swipe(w, t)
            aw = w.swipe(m, t)
            m.update(am, aw, t)
            w.update(aw, am, t)

        # Logging
        for a in men + women:
            simulation.append(a.info(batch, t))

        # Departures
        m_departures = bernoulli.rvs((1 - δ), size=len(men))
        w_departures = bernoulli.rvs((1 - δ), size=len(women))

        men[:] = [m for i, m in enumerate(men) if (m.b != 0) and (m_departures[i] == 0)]
        women[:] = [
            w for i, w in enumerate(women) if (w.b != 0) and (w_departures[i] == 0)
        ]

    return simulation

