"""
Fetches data from about popular tv show game of thrones from a public api

Usage:
    game_of_thrones.py --house=N
    game_of_thrones.py --character=N
    game_of_thrones.py --books=N
"""
import requests

from docopt import docopt, DocoptExit


BASE_URL = 'http://anapioficeandfire.com/api/'

def get_character(arg):
    """ gets character based on their ids"""
    character = requests.get(BASE_URL+'characters/'+arg)
    print character.json()
    return character.status_code

def get_house(arg):
    """ gets houses based on their ids"""
    house = requests.get(BASE_URL+'houses/'+arg)
    print house.json()
    return house.status_code

def get_book(arg):
    """ gets books based on their ids"""
    book = requests.get(BASE_URL+'books/'+arg)
    print book.json()
    return book.status_code



def main():
    """main function that get arguments"""
    try:
        arguments = docopt(__doc__)
        house = arguments['--house']
        character = arguments['--character']
        book = arguments['--books']
        if house:
            get_house(house)
        if character:
            get_character(character)
        if book:
            get_book(book)

    except DocoptExit as e:
        print e.message


if __name__ =='__main__':
    main()
