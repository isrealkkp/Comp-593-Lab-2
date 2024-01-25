def main():
    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Israel Omisakin",
        "student_id": 10314936,
        "pizza_toppings": ["CHICKEN", "PEPPERONI", "BEEF"],
        "movies": [
            {"title": "spiderman", "genre": "action"},
            {"title": "jumanji", "genre": "action"},
        ],
    }
    
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    
    # TODO: Step 3 - Add another movie to the data structure
    new_movie = {"title": "thor", "genre": "action"}
    about_me["movies"].append(new_movie)

    # TODO: Step 4 - Call the function to add pizza toppings
    add_pizza_toppings(about_me, ["MUSHROOMS", "OLIVES"])

    # Print pizza toppings after adding new toppings
    print_pizza_toppings(about_me)
    
    # TODO: Step 7 - Call the function to print movie genres
    print_movie_genres(about_me)

    # TODO: Step 8 - Call the function to print movie titles
    print_movie_titles(about_me["movies"])

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    student_id = about_me["student_id"]
    first_name = full_name.split()[0]
    print(f"My name is {full_name}, but you can call me Sir {first_name}.\nMy student ID is {student_id}.")

# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, new_toppings):
    current_toppings = about_me["pizza_toppings"]
    current_toppings.extend(new_toppings)
    about_me["pizza_toppings"] = current_toppings

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    toppings_list = about_me["pizza_toppings"]
    print("My favorite pizza toppings are:")
    for topping in toppings_list:
        print(f"- {topping}")

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres_list = [movie["genre"] for movie in about_me["movies"]]
    genres_str = ", ".join(genres_list)
    print(f"My favorite movie genres are: {genres_str}")

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles_list = [movie["title"] for movie in movie_list]
    titles_str = ", ".join(titles_list)
    print(f"My favorite movies are: {titles_str}")

if _name_ == '_main_':
    main()