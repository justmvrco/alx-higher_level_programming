# 0x0B-python-input_output


## 0-read_file.py

A function that reads a text file (```UTF8```) and prints it to stdout:

- Prototype: ``` def read_file(filename=""): ```.

## 1-write_file.py

A function that writes a string to a text file (```UTF8```) and returns the number of characters written.

- Prototype: ``` def write_file(filename="", text=""): ```.

## 2-append_write.py

A function that appends a string at the end of a text file (```UTF8```) and returns the number of characters added.

- Prototype: ``` def append_write(filename="", text=""): ```.

## 3-to_json_string.py

A function that returns the JSON representation of an object (string):

- Prototype: ``` def to_json_string(my_obj): ```.

## 4-from_json_string.py

A function that returns an object (Python data structure) represented by a JSON string:

- Prototype: ``` def from_json_string(my_str): ```.

## 5-save_to_json_file.py

A function that writes an object to a text file, using a JSON representation:

- Prototype: ``` def save_to_json_file(my_obj, filename): ```

## 6-load_from_json_file.py

A function that creats an object from a JSON file.

- Prototype: ``` def load_from_json_file(filename): ```.

## 7-add_item.py

A script that adds all arguments to a Pythonn list, and then saves them to a file.

- Uses ``` save_to_json_file ``` and ``` load_from_json_file ```.
- List is saved as a JSON representation in a file called ``` add_item.json ```.

## 8-class_to_json.py

A function that returns the dictionary description woth simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

- Prototype: ``` def class_to_json(obj): ```.
- ``` obj ``` is an instance of a class.
- Alll attributes of the ``` obj ``` class are serializable.

## 9-student.py

A class ``` Student ``` that defines a student by:

- Public instance attributes:
	* ``` first_name ```
	* ``` last_name ```
	* ``` age ```
- Instantiation with ``` first_name ```, ``` last_name ``` and ``` age ```: ``` def __init__(self, first_name, last_name, age): ```.
- Public method ``` def to_json(self): ``` that retrieves a dictonary representation of a ``` Student ``` instance.

## 10-student.py

A class ``` Student ``` that defines a student by: (based on ``` 9-student.py ```)

- Public instance attributes:
	* ``` first_name ```
	* ``` last_name ```
	* ``` age ```
- Instantiation with ``` first_name ```, ``` last_name ``` and ``` age ```: ``` def __init__(self, first_name, last_name, age): ```.
- Public method ``` def to_json(self, attrs=None): ``` that retrieves a dictonary representation of a ```Student ``` instance.
	* If ``` attrs ``` is a list of strings, only attribute names contained in this list are retrieved.
	* Otherwise, all attributes are retrieved.

## 11-student.py

A class ``` Student ``` that defines a student by: (based on ``` 10-student.py ```)

- Public instance attributes:
	* ``` first_name ```
	* ``` last_name ```
	* ``` age ```
- Instantiation with ``` first_name ```, ``` last_name ``` and ``` age ```: ``` def __init__(self, first_name, last_name, age): ```.
- Public method ``` def to_json(self, attrs=None): ``` that retrieves a dictonary representation of a ```Student ``` instance.
        * If ``` attrs ``` is a list of strings, only attribute names contained in this list are retrieved.
        * Otherwise, all attributes are retrieved.
- Public method ``` def reload_from_json(self, json): ``` that replaces all attributes of the Student instance:
	* Assumption: ``` json ``` will always be a dictionary.
	* A dictionary key will be the public attribute name.
	* A dictionary value will be the value of the public attribute.
