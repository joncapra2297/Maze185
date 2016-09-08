from Maze import *
import random
import turtle
import unittest

class testmaze (unittest.TestCase):
    """
    This class inherits from a class called TestCase which is
    defined in the unittest module.

    When you inherit from a class, you get all the methods that are
    defined in that class for free.

    Since this is a TestCase class, calling unittest.main() will automatically
    run any of the functions that start with the word 'test'
    """
    
    def setUp (self):
        """
        The setUp function is called each time one of your tests is run.
        We create an insatnce of the maze here before each test.
        """
        self.m = Maze()

    def testMazeExists(self):
        """
        this will check to see if we have a maze class but as soon
        as setUp is run, we will see a failure so we really dont need
        to do anything here
        """
        pass

    def testScreenExists(self):
       assert type(self.m.s) == turtle._Screen

    def testTurtleExists(self):
        assert type(self.m.t) == turtle._Turtle

unittest.main()
