import random

class MonthlyInvestment:
    def __init__(self, investment, penalty, rates, prev_company):
        self.investment = investment
        self.penalty = penalty
        self.rates = rates
        self.prev_company = prev_company

    def findBest(self):
        max = 0.
        w = -1

        for i in range(len(self.rates)):

                if self.rates[i] > max:
                    max = self.rates[i]
                    w = i

        return [max, w]

    def switch(self, best):
        if best[1] == self.prev_company:
            return False

        switch_value = self.investment * best[0] - self.penalty
        stay_value = self.investment * self.rates[self.prev_company]

        if switch_value > stay_value:
            return True

        return False

    def sell(self, best):
        if self.switch(best):
            self.prev_company = best[1]

        return self.prev_company

# Define parameters
companies = 9
months = 11
investment = 100000
penalty = 7500
S = [ [ round(random.uniform(0, 3), 2) for company in range(companies) ] for month in range(months) ]
result = -1
C = [ 0 for month in range(months) ]
cash = [ investment for month in range(months) ]

# Testing
for k in range(len(S)):
    Month = MonthlyInvestment(investment, penalty, S[k], result)
    best = Month.findBest()
    result = Month.sell(best)
    C[k] = result
    cash[k] = cash[k] * S[k][result] - 100000

print("C: " + str(C))
print("Monthly Income: " + str(cash))
