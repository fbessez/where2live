import teleportAPI as api
import getTaxRates as tax
import googleMapsAPI as gmaps
import scrapers
import config
import constants


savingsByCity = {}

def getAverageSalary(city, job, state, results_dict):
    avg_salary_teleport = api.find_salary(city, job)
    avg_salary_indeed = scrapers.indeedScrape(city, job)
    avg_salary = (avg_salary_indeed + avg_salary_teleport) // 2

    results_dict['avgSalaryTeleport'] = constants.readableCurrency(avg_salary_teleport)
    results_dict['avgSalaryIndeed'] = constants.readableCurrency(avg_salary_indeed)
    results_dict['avgSalary'] = avg_salary
    results_dict['job'] = job
    results_dict['city'] = city
    return results_dict

def getCostOfLivingFromTeleport(city):
    return api.get_urban_cost_by_name(city) * 12

def getCostOfLivingFromNomadList(city):
    return scrapers.nomadListScrape(city) * 12

def calculateAverageAnnualCost(teleportEstimate, nomadListEstimate):
    if nomadListEstimate == 0:
        return teleportEstimate
    else:
        return (teleportEstimate + nomadListEstimate) // 2

def calculateCost(city, job):

    state = gmaps.convertCityToState(city)
    city = gmaps.convertInputToCity(city)

    results_dict = getAverageSalary(city, job, state, {})
    results_dict['state'] = state
    incomeAfterTaxes = tax.incomeAfterTaxes(city, state, results_dict['avgSalary'])
    results_dict['incomeAfterTaxes'] = constants.readableCurrency(incomeAfterTaxes)

    annualCostTeleport = getCostOfLivingFromTeleport(city)
    results_dict['annualCostTeleport'] = constants.readableCurrency(annualCostTeleport)
    annualCostNomadlist = getCostOfLivingFromNomadList(city)
    results_dict['annualCostNomadlist'] = constants.readableCurrency(annualCostNomadlist)

    avgAnnualCost = calculateAverageAnnualCost(annualCostTeleport, annualCostNomadlist)
    results_dict['avgAnnualCost'] = constants.readableCurrency(avgAnnualCost)
    
    savings = incomeAfterTaxes - avgAnnualCost
    results_dict['savings'] = constants.readableCurrency(savings)

    return results_dict

def calculateAllCities():
    for city in config.cities:
        results = calculateCost(city, config.jobtitle)
        savingsByCity[city] = results


if __name__ == '__main__':
    calculateAllCities()

