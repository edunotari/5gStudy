


# CAPEX D-RAN
print("\n ### CAPEX ### \n")

numSite = 1         # Site Numbers


## Site installation cost
numRU = 2           # Radio Unit Number
ru = 1000           # Radio Unit Price
du = 5000           # DU cost per CU
cu = 4000           # CU unit Price
cpri = 3000         # Common Public Radio Interface Price
mast = 10000        # Mast Price
cool = 2000         # Site cooling price
ducu = du + 0.5*cu
instSite = ducu + (numRU * ru) + cpri + mast + cool
print(f'The Site Installation price is: {instSite} US dollars.')

## Work cost per Site
cwSite = 0.2*((numRU * ru) + du + cpri)     # Work cost is considered 20% of the equipments
print(f'The work cost per site is: {cwSite} US dollars.')

## Optic line cost
dig = 1000          # Digging cost
fhLenght = 10000    # Fronthaul lenght in kilometers
bhLenght = 5000     # Backhaul lenght in kilometers
rol = 5000          # Fiber cost and add ons
optics = dig * ((fhLenght / numRU) + bhLenght) + rol * (fhLenght + bhLenght)
print(f'The optics implementation cost is: {optics} US dollars.')

## Core Price

core = 40000        # Core Price
print(f'The core cost is: {core} US dollars.')
coreCool = 3000     # Core cooling
print(f'The core cooling cost is: {coreCool} US dollars.')
coreWork = 10000    # Work cost for Core installation
print(f'The core work is {coreWork} US dollars.')

capex5gDran = numSite*(instSite + cwSite) + optics + core + coreCool + coreWork
print("\n capex5gDran = numSite*(instSite + cwSite) + optics + core + coreCool + coreWork")
print(f'The CAPEX cost is: {capex5gDran} US dollars.')


# OPEX D-RAN
print('\n ### OPEX ### \n')

wh = 2                      # Watt-hour cost
print(f'The cost of the watt per hour is: {wh} US dollar/hour')
rent = 2000                 # Site location rent
print(f'The site location rent is: {rent} US dollar monthly.')
L = fhLenght + bhLenght     # Optical line total
print(f'The fiber optics length is: {L} kilometers.')
fiberMan = 300              # Fiber optics maintenance
print(f'The fiber optics maintenance is: {fiberMan} US dollars per kilometer.')

## Energy consumption
numHour = 400               # Hour per year number
pRu = 200                   # Power consumption by Radio Unit   
pDucu = 300                 # Power consumption by du/cu
pCool = 400                 # Power consumption by cooling
pSite = numRU * pRu + pDucu + pCool     # Power consumtion by site
pCore = 300                 # Core power consumtion
pCoreCool = 300             # Core Cooling power consumption 
P = 0.6 * numHour * ((numSite * pSite) + pCore + pCoreCool)
print(f'The energy consumption is: {P} watts.')

## Annual Maintenance and Operation
ebitida = 0.1               # Equipment depreciation
oem = ebitida*(numSite*((numRU*ru) + ducu + cpri) + core)
print(f'The maintenance and operations cost is: {oem} US dollars.')

# Worker Wages Salary per period
months = 12         # Number of months
wage = 500          # Worker Salary
numStaff = 3        # Workers number
wages = months * wage * numStaff
print(f'The work ages is: {wages} US dollars.')

## Software cost
sw = 0.3*(numSite*((ru*numRU)+ducu) + core)     # 30% from SW cost
print(f'The Software cost is: {sw} US dollars.')

opex5gDran = (wh * P) + (numSite * rent) + (L * fiberMan) + oem + wages + sw
print('\n opex5gDran = (wh * P) + (numSite * rent) + (L * fiberMan) + oem + wages + sw')
print(f'The OPEX cost is: {opex5gDran} US dollars.')