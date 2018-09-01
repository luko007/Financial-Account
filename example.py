from Account import *


outcome = Outcome()
outcome.addOutcome('Apartment', 1800)
outcome.addOutcome('Bills', 200)
outcome.addOutcome('Public Transportation', 100)

myAccount = Account(50000, outcome)
Analytics(myAccount).analyzeMonthAhead()
