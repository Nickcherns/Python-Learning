
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[] for i in range(5)]

def get_destination_index(destination):
	for i in range(len(destinations)):
		if destinations[i] == destination:
			destination_index = i
			return destination_index

def get_traveler_location(traveler):
	traveler_destination = traveler[1]
	traveler_destination_index = get_destination_index(traveler_destination)
	return traveler_destination_index

def add_attraction(destination, attraction):
	destination_index = get_destination_index(destination)
	attractions_for_destination = attractions[destination_index]
	attractions_for_destination.append(attraction)

# def find_attractions(destination, interests):
# 	destination_index = get_destination_index(destination)
# 	attractions_in_city = attractions[destination_index]
# 	attractions_with_interest = []
# 	for attractions in attractions_in_city:
# 		possible_attraction = attractions
# 		attraction_tags = attractions[1]
# 		for interest in interests:
# 			if attraction_tags.count(interest) >= 1:
# 				attractions_with_interest.append(possible_attraction)
# 	return attractions_with_interest


test_destination_index = get_traveler_location(test_traveler)

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# la_arts = find_attractions("Los Angeles, USA", ['art'])
# print(la_arts)

print(test_destination_index)
print(get_destination_index("Hyderabad, India"))
print(attractions)
