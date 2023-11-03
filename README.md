**# holbertonschool-AirBnB_clone**


# Use for each file

> file_storage.py:
Will handle the file.json thats created, it will save and read the data inside of it and it will deserialize it.

> base_model.py:
It is the base for each class (amenity, city, place, review, state, user).
It also creates the basic dictionary for the classes and it handles the date it was created in and updated in.

> console.py:
It will handle the running of commands (EOF, all, count, create, destroy, help, quit, show, update).


# Running the console

> To start the program in interactive mode, use "./console"

> To start the program in non-interactive mode use "echo '#command' | ./console"

* **help:** *It will print out all the commands you can use and when it's followed by a console command it will print out the use of the command and the syntaxis.*
* **EOF:** *Signals to exit the program.*
* **all:** *Display string representations of all instances of a given class. If no class is specified, displays all instantiated objects.*
* **count:** *Retrieve the number of instances of a given class.*
* **create:** *Create a new class instance and print its id.*
* **destroy:** *Delete a class instance of a given id.*
* **quit:** *Quit command to exit the program.*
* **show:** *Display the string representation of a class instance of a given id.*
* **update:** *Update a class instance of a given id by adding or updating a given attribute key/value pair or dictionary.*
