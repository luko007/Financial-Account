import csv
import datetime


class Outcome:

    def __init__(self, name = "", outcome = 0):
        self._outcomes = {}

    def getOutcome(self):
        return self._outcome

    def addOutcome(self, name, outcome):
        self._outcomes[name] = outcome

    def sumAllOutcomes(self):
        sum = 0
        for outcome in self._outcomes.values():
            sum += outcome
        return sum



class Account:

    def __init__(self, balance = 0, outcome = Outcome()):
        self._balance = balance
        self._monthlyOutcome = outcome

    def setMonthlyOutcome(self, outcome):
        self._monthlyOutcome = outcome

    def getBalance(self):
        return self._balance
    def getOutcome(self):
        return self._monthlyOutcome

class Analytics:
    def __init__(self, account = Account()):
        self._account = account

    def analyzeMonthAhead(self):
        date = datetime.datetime.now()
        with open('analyze.csv', 'w') as csvfile:
            self._writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=['Date', 'Balance'])

            self._writer.writeheader()
            for i in range(0, 12):
                self._writer.writerow({'Date' : (((date.month + i) % 12) + 1),
                                       'Balance' : self._account.getBalance() - (self._account.getOutcome().sumAllOutcomes() * i)})
