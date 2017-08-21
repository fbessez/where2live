# Resources:
# https: // www.thebalance.com / state - income - tax - rates - 3193320
# https: // smartasset.com / taxes / ohio - tax - calculator  # NHK86xVMxu

ficaTaxRate = .062 + .0145  # social security and medicare

statesToTaxRates = {
    "Alabama": .05,
    "Alaska": .00,
    "Arizona": .04,
    "Arkansas": .07,
    "California": .08,
    "Colorado": .0463,
    "Connecticut": .045,
    "Delaware": .045,
    "Florida": .00,
    "Georgia": .06,
    "Hawaii": .0825,
    "Idaho": .074,
    "Illinois": .0375,
    "Indiana": .033,
    "Iowa": .0898,
    "Kansas": .046,
    "Kentucky": .06,
    "Louisiana": .06,
    "Maine": .06,
    "Maryland": .04,
    "Massachusetts": .051,
    "Michigan": .0425,
    "Minnesota": .075,
    "Mississippi": .05,
    "Missouri": .06,
    "Montana": .069,
    "Nebraska": .0684,
    "Nevada": .00,
    "New Hampshire": .00,
    "New Jersey": .04,
    "New Mexico": .049,
    "New York": .052,
    "North Carolina": .0575,
    "North Dakota": .02,
    "Ohio": .03,
    "Oklahoma": .0525,
    "Oregon": .08,
    "Pennsylvania": 0.0307,
    "Rhode Island": .045,
    "South Carolina": .07,
    "South Dakota": .00,
    "Tennessee": .00,
    "Texas": .00,
    "Utah": .05,
    "Vermont": .048,
    "Virginia": .0575,
    "Washington": .00,
    "West Virginia": .065,
    "Wisconsin": .06,
    "Wyoming": .00
}

localTaxRates = {
    "Birmingham": .01,
    "Cleveland": .02,
    "Detroit": .02,
    "Kansas City": .01,
    "Miami": .01,
    "St. Louis": .01,
    "New York": .03648,
    "Pittsburgh": .03,
    "Philadelphia": .035,
    "San Francisco": .015,
    "Washington": .08
}

def getFederalIncomeTaxRate(salary):
    if salary < 9275:
        return .10
    elif salary < 37650:
        return .15
    elif salary < 91150:
        return .25
    elif salary < 190150:
        return .28
    elif salary < 413350:
        return .33
    elif salary < 415040:
        return .35
    else:
        return .396

def getStateIncomeTaxRate(state):
    try:
        return statesToTaxRates[state]
    except:
        return .0000000000001

def getLocalIncomeTaxRate(city):
    try:
        return localTaxRates[city]
    except:
        return .0000000000001

def readableCurrency(amount):
    return "${:,}".format(amount)

jobConstantsFromTeleport = [
    'Account Manager', 'Accountant', 'Administrative Assistant',
    'Architect', 'Attorney', 'Business Analyst', 'Business Development',
    'C Level Executive', 'Cashier', 'Chef', 'Chemical Engineer', 'Civil Engineer',
    'Content Marketing', 'Copywriter', 'Customer Support', 'Data Analyst',
    'Data Scientist', 'Dentist', 'Electrical Engineer', 'Executive Assistant',
    'Fashion Designer', 'Finance Manager', 'Financial Analyst', 'Graphic Designer',
    'Hardware Engineer','Human Resources Manager', 'IT Manager',
    'Industrial Designer', 'Interior Designer', 'Lecturer', 'Marketing Manager',
    'Mechanical Engineer', 'Mobile Developer', 'Nurse', 'Office Manager',
    'Operations Manager', 'Pharmacist', 'Physician', 'Postdoctoral Researcher',
    'Product Manager', 'Project Manager', 'QA Engineer', 'Receptionist',
    'Research Scientist', 'Sales Manager', 'Software Engineer',
    'Systems Administrator', 'Teacher', 'UX Designer', 'Waiter',
    'Web Designer', 'Web Developer'
]
