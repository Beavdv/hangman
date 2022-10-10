from dataclasses import replace
import random
from re import I
from typing import List, Union


class hangman:

    def __init__(self):
        self.possible_words: List[str]=['vader', 'moeder', 'dochter', 'zoon', 'nicht', 'neef',
                'becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find=str('')
        self.well_guessed_letters=int(0)
        self.bad_guessed_letters=int(0)
        self.turn_count=int(0)
        self.error_count=int(0)
        self.lives=int(5)
        self.guessed_word= str('')
        self.word_to_find=random.choice(self.possible_words)
        self.splitted_word=list(self.word_to_find)
        self.pos=int()
        self.elem=''
        self.empty_list_str = ['_']* len(self.splitted_word)
        self.index=int()

    def play(self):
        print(self.splitted_word)
        print(self.empty_list_str)
        self.letter_asked=input('give a letter')        
        self.turn_count=self.turn_count+1
        if self.letter_asked in self.splitted_word:
            self.well_guessed_letters+=1
        else:
            self.bad_guessed_letters+=1
            self.error_count+=1
            self.lives=self.lives-1
        for self.pos, self.elem in enumerate (self.splitted_word):
            if self.elem == self.letter_asked:
                self.empty_list_str[self.pos]=self.letter_asked
                print(self.empty_list_str)
                if self.empty_list_str==self.splitted_word:
                    self.guessed_word.join(self.empty_list_str)
                    print(self.guessed_word)
        print(self.well_guessed_letters, self.bad_guessed_letters, self.error_count, self.lives)

    def game_over():    
        print('Game over')

    def well_played(self):
        print(f"You found the word: {self.guessed_word} in {self.turn_count} turns with {self.error_count} errors!")
    
    def start_game(self):
        while self.lives >0 or self.guessed_word!= self.word_to_find:
            self.play()
        if self.lives ==0:
            self.game_over()
        else:
            self.well_played()

