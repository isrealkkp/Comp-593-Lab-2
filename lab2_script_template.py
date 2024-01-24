def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name":"Israel Omisakin",
        "Student_id":10314936,
        "pizza_toppings": ["CHICKEN", "PEPPERONI", "BEEF"],
        "movies": [
            {"title": "spiderman", "genre": "action"},
            {"title": "jumanji", "genre": "action"},
        ],
    }

    # TODO: Step 3 - Add another movie to the data structure
    new_movie={"title": "thor", "genre": "action"}
    about_me["movies"].append(new_movie)

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    student_id = about_me["student_id"]
    first_name = full_name.split()[0]
    print(f"My name is {full_name}, but you can call me Sir {first_name}.\nMy student ID is {student_id}.")
    
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()