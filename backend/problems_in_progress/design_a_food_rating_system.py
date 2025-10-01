"""
Problem: Design a Food Rating System 
Difficulty: Medium
Concepts: Hash Table, Design, Heap (Priority Queue), Strings
Link: https://leetcode.com/problems/design-a-food-rating-system/
Notes:
- Goal: 

Design a food rating system that can do the following:
 - Modify the rating of a food item listed in the system.
 - Return the highest-rated food item for a type of cuisine in the system.

Implement the FoodRatings class:
 - FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system.
   The food items are described by foods, cuisines and ratings, all of which have a length of n.
     - foods[i] is the name of the ith food,
     - cuisines[i] is the type of cuisine of the ith food, and
     - ratings[i] is the initial rating of the ith food.
 - void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
 - String highestRated(String cuisine) Returns the name of the food item that has the highest rating for 
   the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, 
that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] 
comes before y[i] in alphabetic order.

- Key insight: Use a combination of a dictionary and a max-heap (priority queue) to efficiently track 
  and retrieve the highest-rated food items for each cuisine.
- Alternate approaches: A simpler approach could involve sorting the food items by rating and cuisine, but this would be less efficient for frequent updates and queries.
"""



"""
Personal Notes:
So the first thing we need to do is to create an association for a food to its cuisine and its rating. (two dictionaries)
The i association means we can just zip them together and iterate through them to create the dictionaries.

We have a function to change the rating of a food item. So we can just update the food_to_rating dictionary.

Lastly we need to be able to find the highest rated food item for a given cuisine.
To do this efficiently, we can use a max-heap (priority queue) for each cuisine, 
which stores the food items along with their ratings so this is another dictionary.
This way, we can always get the highest rated food item in O(1) time.
The only issue is that when we change the rating of a food item, we need to update the heap.

In total we need three dictionaries:
1. food_to_cuisine: maps food items to their respective cuisines.
2. food_to_rating: maps food items to their current ratings.
3. cuisine_to_heap: maps each cuisine to a max-heap (priority queue) of food items based on their ratings.

* Note: part of the initialization involves populating these dictionaries 
  so we also need that as part of the constructor.

* Note: In Python, the heapq library implements a min-heap, so to simulate a max-heap, we can store negative ratings.

The void function to change the rating of a food item.
The string function to get the highest rated food item for a given cuisine.

"""
import heapq
from pyparsing import List


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = {}
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            # Initialize the heap for the cuisine if it doesn't exist
            if cuisine not in self.cuisine_to_heap:
                self.cuisine_to_heap[cuisine] = []
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_heap[cuisine]
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)
        return ""
        
        
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

# Example usage:
# Input
# ["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
# [[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], 
# ["korean", "japanese", "japanese", "greek", "japanese", "korean"], 
# [9, 12, 8, 15, 14, 7]], 
# ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
# Output
# [null, "kimchi", "ramen", null, "sushi", null, "ramen"]

# Explanation
# FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
# foodRatings.highestRated("korean"); // return "kimchi"
#                                     // "kimchi" is the highest rated korean food with a rating of 9.
# foodRatings.highestRated("japanese"); // return "ramen"
#                                       // "ramen" is the highest rated japanese food with a rating of 14.
# foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
# foodRatings.highestRated("japanese"); // return "sushi"
#                                       // "sushi" is the highest rated japanese food with a rating of 16.
# foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
# foodRatings.highestRated("japanese"); // return "ramen"
#                                       // Both "sushi" and "ramen" have a rating of 16.
#                                       // However, "ramen" is lexicographically smaller than "sushi".


foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 12, 8, 15, 14, 7]

food_ratings = FoodRatings(foods, cuisines, ratings)
print(food_ratings.highestRated("korean"))  # Output: "kimchi"
print(food_ratings.highestRated("japanese"))  # Output: "ramen"
food_ratings.changeRating("sushi", 16)
print(food_ratings.highestRated("japanese"))  # Output: "sushi"
food_ratings.changeRating("ramen", 16)
print(food_ratings.highestRated("japanese"))  # Output: "ramen"