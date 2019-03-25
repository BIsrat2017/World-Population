
# Bisrat Asefaw

# CSC 110 section 03

# Date 06/10/2018

# program that reads data from a file of world populaion  and analyzes this
# data in various ways and shows a report to the user.
# Each line in the file must contains the name of a
# country, the population, and the land area, in that order. otherwise the
# program will report an error or will show unexpected result.

infile=input('Enter file name:') # asking user for input file

read_file=open(infile,'r') 

line=read_file.readline()
total_coutries=0 # counter that counts number of countries
world_population=0 # accumulator that sums up the world population
split_variables=line.split(',')

highest_populaton=int(split_variables[1]) # initialization of highest population
#to the first file line
country_highest_population=split_variables[0] # initialization name of the country 
# that has highest population to the first file line
lowest_population=int(split_variables[1])#initialization of lowest population
#to the first file line
country_lowest_population=split_variables[0]# initialization name of the country 
# that has highest population to the first file line

greatest_land_area=int(split_variables[2])# greatest land area initialization to the
#first file line for comparison
country_greatest_land_area=split_variables[0]# greatest land area initialization to the
#first file line
lowest_land_area=int(split_variables[2])#greatest land area initialization to the
#first file line for comparison
country_lowest_land_area=split_variables[0]

highest_population_density=int(split_variables[1])/float(split_variables[2])#highest population density
#initialization
country_highest_population_density=split_variables[0] # country with highest population density
lowest_population_density=int(split_variables[1])/float(split_variables[2])#lowest population density
#initialization
country_lowest_population_density=split_variables[0]# country with lowest population density

total_population_density=0# to calculate the total population density and come up with average
#population density

# this while loop used to read all the file information line by line and prints: number of countries , 
# total world population,  name and population of highest and lowest population, greater and lower
# land area, highest and lowest population density
#
while line!='':
    
    total_coutries+=1
    
    x=line.split(',')
    
    population=int(x[1]) # inner loop population assighnement

    land_area=float(x[2]) # inner loop land area assighnement

    world_population+=population

    population_density= population/land_area

    total_population_density+=population_density

    if population > highest_populaton:
        
        highest_populaton=population
        country_highest_population=x[0]
        
    if population<lowest_population:
        
        lowest_population=population
        country_lowest_population=x[0]
        
    if land_area>greatest_land_area:
        
        greatest_land_area=land_area
        country_greatest_land_area=x[0]
        
    if land_area<lowest_land_area:

        lowest_land_area=land_area
        country_lowest_land_area=x[0]
        
    if population_density > highest_population_density:
        
        highest_population_density=population_density
        country_highest_population_density=x[0]
        
    if population_density < lowest_population_density:
        
        lowest_population_density=population_density
        country_lowest_population_density=x[0]
        

    line=read_file.readline()
    
   
    
read_file.close()

# number of countries and total world population
print('Number of countries in the file: '+str(total_coutries))
print('\nThe world population is: '+format(world_population,',.0f'))

# countries with lowest and highest population 
print('\n'+country_highest_population+' has the highest population of '+format(highest_populaton,',.0f'))
print('\n'+country_lowest_population+' has the lowest population of '+format(lowest_population,',.0f'))

# lowest and highest land area
print('\n'+country_greatest_land_area+' has the greatest land area of '+format(greatest_land_area,',.2f'))
print('\n'+country_lowest_land_area+' has the smallest land area of '+ format(lowest_land_area,',.2f'))

#name and country with highest and lowest population density
print('\n'+country_highest_population_density+' has the highest population density of '+format(highest_population_density,',.2f'))
print('\n'+country_lowest_population_density+' has the lowest population density of '+format(lowest_population_density,',.2f'))

#worlds average population
total_population_density/=total_coutries
print('\nThe average population density of the world is '+format(total_population_density,',.2f'))


read_file=open(infile,'r')

line=read_file.readline()

densely_populated_countries=[]

sparsely_populated_countries=[]

# this loop used to read the file line by line and calculates and prints the countries
#that are densely populated country and very sparsely populated countries.
while line!='':

    x=line.split(',')

    population_density=int(x[1])/float(x[2])

    if population_density > 2*total_population_density:

        densely_populated_countries.append(x[0])
        
    if population_density < ((1/100)*total_population_density):
        sparsely_populated_countries.append(x[0])
        
        
    line=read_file.readline()

read_file.close()
# list of densely populated country and sparsely populated countries.
print('\nList of densely populated country: ', densely_populated_countries)
print('\nList of very sparsely populated countries: ', sparsely_populated_countries)

# test cases , i belive those results are courect and the program is working corectly
# i checked some valuse using calculator to check for bug.
# file content
#  Afghanistan,36373176,652860
#  Albania,2934363,27400
#  Algeria,42008054,2381740
#  American Samoa,55679,200
#  Andorra,76953,470
# result printed in shell window
#   There are 5 countries in the world 
#   The world population is 81,448,225
#   Algeria has the highest population of 42,008,054
#   American Samoa has the lowest population of 55,679
#   Algeria has the greatest land area of 2,381,740
#   American Samoa has the smallest land area of 200
#   American Samoa has the highest population density of 278.39
#   Algeria has the lowest population density of 17.64
#   The average population density of the world is 124.51
#   list of densely populated country:  ['American Samoa']
#   list of very sparsely populated countries:  []

    


