import constants

def incomeAfterTaxes(city, state, salary):
    federalIncomeTaxRate = constants.getFederalIncomeTaxRate(salary)
    stateIncomeTaxRate = constants.getStateIncomeTaxRate(state)
    localIncomeTaxRate = constants.getLocalIncomeTaxRate(city) # TODO: Must be not hardcoded for obvious reasons
    deduction = (federalIncomeTaxRate * salary) + (stateIncomeTaxRate * salary) + (constants.ficaTaxRate * salary) + (localIncomeTaxRate * salary)
    return int(salary - deduction)
