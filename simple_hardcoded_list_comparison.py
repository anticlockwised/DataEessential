cdk = ['id', 'language', 'notes', 'saleType', 'priceCode', 'preferredContactMethod', 'preferredContactPhone', 'deleted', 'first', 'middle', 'last', 'title', 'suffix', 'preferred', 'company', 'line1', 'line2', 'city', 'state', 'county', 'country', 'postalCode', 'phoneNumbers', 'emails', 'creditLimit', 'taxExempt', 'stateTaxId', 'federalTaxId', 'ar', 'daysToFirstInterest', 'contactInfo', 'compensationLine', 'compensationCode', 'fleetOwner']


java = ['id', 'language', 'notes', 'saleType', 'priceCode', 'preferredContactMethod', 'preferredContactPhone', 'deleted', 'first', 'middle', 'last', 'title', 'suffix', 'preferred', 'company', 'line1', 'line2', 'city', 'state', 'county', 'country', 'postalCode', 'phoneNumbers', 'emails', 'creditLimit', 'taxExempt', 'stateTaxId', 'federalTaxId', 'ar', 'daysToFirstInterest', 'contactInfo', 'compensationLine', 'compensationCode', 'fleetOwner']


for item in java:
    if item not in cdk:
        print(item + " : Not Matched")

for item in cdk:
    if item not in java:
        print(item + " : Not Matched")
