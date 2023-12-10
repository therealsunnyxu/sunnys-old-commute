import sys
from random import random
from enum import Enum

class CommuteState(Enum):
    NONE = 0
    HOME = 1
    LEAVE_HOME_BY_CAR = 2
    LEAVE_HOME_BY_BUS = 3
    LEAVE_SF_BY_CAR = 4
    LEAVE_SF_BY_TRAIN = 5
    GO_SOUTH_BY_CAR_VIA_101 = 6
    GO_SOUTH_BY_CAR_VIA_280 = 7
    GO_SOUTH_BY_TRAIN = 8
    ARRIVE_SJ_BY_CAR = 9
    ARRIVE_SJ_BY_TRAIN = 10
    COLLEGE = 11
    GO_NORTH = 12

class Story():
    def __init__(self) -> None:
        self.storyState = CommuteState.NONE
        self.playingState = True

    """
    Method getStoryInput
    Gets the input when the reader is at a stage of a story
    param:
        str prompt: a custom prompt
    return:
        int: An integer representing the choice the reader made, or -1 if invalid
    """
    def getStoryInput(self, prompt: str):
        prompt = prompt or ""
        try:
            currAnswer = input(prompt)
            if not currAnswer:
                print("Input was empty. Please make a selection.")
            elif currAnswer == "q":
                print("Goodbye")
                exit(0)
                
            if self.storyState == CommuteState.NONE:
                return 0
            
            return int(currAnswer)
        except ValueError:
            print("Invalid choice made. Please try again.")
            return 0
        except Exception as ex:
            print("Uh oh, an error has occured:", ex)

        return -1
    
    """
        Method getCurrentStoryStatePrompt
        Gets the prompt of the current story state
        return:
            str prompt: the prompt of the current story state
    """
    def getCurrentStoryStatePrompt(self):
        prompt = "This part of the story hasn't been written yet: " + str(self.storyState)
        if self.storyState == CommuteState.HOME:
            # Sunny is at home
            # He can either go to school by car or bus
            prompt = '''
                Sunny lives in San Francisco and commutes to college in San Jose.
                Sunny is ready to go to school this morning.
                How should he get there?

                Press 1 to drive his car.
                Press 2 to take the bus.
                '''
        elif self.storyState == CommuteState.LEAVE_HOME_BY_CAR:
            prompt = '''
                Sunny decides to drive his car today. 
                Should he drive straight to school or to the train station in San Bruno?

                Press 1 to drive straight to school.
                Press 2 to drive to the train station.
                '''
        elif self.storyState == CommuteState.LEAVE_HOME_BY_BUS:
            prompt = '''
                Sunny decides to take the bus to the train station in San Bruno.

                Press 1 to board the bus.
                '''
        elif self.storyState == CommuteState.LEAVE_SF_BY_CAR:
            prompt = '''
                Sunny decides to drive straight to school.
                Which highway should he take?

                Press 1 to take the 101.
                Press 2 to take the 280
                '''
        elif self.storyState == CommuteState.LEAVE_SF_BY_TRAIN:
            prompt = '''
                Sunny arrives at the train station in San Bruno. He buys a ticket, then waits for the train.
                The train arrives on time.

                Press 1 to board the train.
                '''
        elif self.storyState == CommuteState.GO_SOUTH_BY_CAR_VIA_101:
            prompt = '''
                Sunny enters the 101 and immediately gets stuck behind a long line of cars.
                Sunny tunes into the regional news radio channel. What's causing the backup today? 

                Press 1 to find out.
                '''
        elif self.storyState == CommuteState.GO_SOUTH_BY_CAR_VIA_280:
            prompt = '''
                Sunny enters the 280.
                How smooth is the drive?

                Press 1 to find out.
                '''
        elif self.storyState == CommuteState.GO_SOUTH_BY_TRAIN:
            prompt = '''
                Sunny boards the train.
                He decides to get a head-start on his homework. He pulls out his binder.
                While he studies, he looks out of the window and admires the industrial cityscape flying past him.

                Press 1 to continue.
                '''
        elif self.storyState == CommuteState.ARRIVE_SJ_BY_CAR:
            prompt = '''
                Sunny finally reaches San Jose, feeling tired and sluggish.
                He eventually finds a parking spot after driving around inside the parking garage several times.

                Press 1 to go to his first morning class.
                '''
        elif self.storyState == CommuteState.ARRIVE_SJ_BY_TRAIN:
            prompt = '''
                Sunny finally reaches San Jose, feeling refreshed and rejuvenated.
                He takes the bus from the train station to the university.

                Press 1 to go to his first morning class.
                '''
        elif self.storyState == CommuteState.COLLEGE:
            prompt = '''
                Sunny gets through a whole day of classes. The endless lectures drain his concentration.

                Press 1 to barely stay awake.
                '''
        elif self.storyState == CommuteState.GO_NORTH:
            prompt = '''
                After a long day of classes, Sunny can finally go home.

                The end. 
                Press 1 to go to the next day.
                Press q to exit.
                '''
        else:
            prompt = '''
                    Sunny's Commute, by Sunny Xu
                    What did Sunny's commute look like in 2019?

                    Press any key to continue, or press q to exit.
                '''
        
        return prompt
    
    """
        Method getCurrentStoryStateInput
        Receives user input based on the choices for the current story prompt
    """

    def getCurrentStoryStateInput(self, prompt: str):
        numChoice = self.getStoryInput(prompt)
        if self.storyState == CommuteState.HOME:
            # Sunny leaves home by car or bus
            if numChoice == 1:
                self.storyState = CommuteState.LEAVE_HOME_BY_CAR
            elif numChoice == 2:
                self.storyState = CommuteState.LEAVE_HOME_BY_BUS
        elif self.storyState == CommuteState.LEAVE_HOME_BY_CAR:
            # Sunny drives his car straight to San Jose or to the train station in San Bruno
            if numChoice == 1:
                self.storyState = CommuteState.LEAVE_SF_BY_CAR
            elif numChoice == 2:
                self.storyState = CommuteState.LEAVE_SF_BY_TRAIN
        elif self.storyState == CommuteState.LEAVE_HOME_BY_BUS:
            # Sunny takes the bus to the train station in San Bruno
            if numChoice == 1:
                self.storyState = CommuteState.LEAVE_SF_BY_TRAIN
        elif self.storyState == CommuteState.LEAVE_SF_BY_CAR:
            # Sunny takes either the 101 or the 280 highways
            if numChoice == 1:
                self.storyState = CommuteState.GO_SOUTH_BY_CAR_VIA_101
            elif numChoice == 2:
                self.storyState = CommuteState.GO_SOUTH_BY_CAR_VIA_280
        elif self.storyState == CommuteState.LEAVE_SF_BY_TRAIN:
            # Sunny boards the train to San Jose
            if numChoice == 1:
                self.storyState = CommuteState.GO_SOUTH_BY_TRAIN
        elif self.storyState == CommuteState.GO_SOUTH_BY_CAR_VIA_101:
            # Sunny takes the 101 and immediately encounters traffic
            if numChoice == 1:
                self.storyState = CommuteState.ARRIVE_SJ_BY_CAR
            # roll a random number
            chance = random()
            if chance >= 0 and chance <= 0.33:
                print(
                    '''
                        The news anchor reports about a collision that happened earlier this morning.
                        The police and Caltrans have moved the wreckage to the side of the road, but people are slowing down to take a look at the mess.
                    '''
                )
            else:
                print(
                    '''
                        The news anchor mentions heavy traffic on the 101. Who knows why the 101's always gummed up...
                    '''
                )
        elif self.storyState == CommuteState.GO_SOUTH_BY_CAR_VIA_280:
            # Sunny takes the 101 and immediately encounters traffic
            if numChoice == 1:
                self.storyState = CommuteState.ARRIVE_SJ_BY_CAR
            # roll a random number
            chance = random()
            if chance >= 0 and chance <= 0.33:
                print(
                    '''
                        Sunny encounters light traffic at most. He's able to keep a steady speed all the way to San Jose.
                    '''
                )
            else:
                print(
                    '''
                        Sunny encounters medium traffic. Sometimes he's going 25 mph and sometimes he's going 75 mph.
                    '''
                )
        elif self.storyState == CommuteState.GO_SOUTH_BY_TRAIN:
            # Sunny rides the train
            if numChoice == 1:
                self.storyState = CommuteState.ARRIVE_SJ_BY_TRAIN
        elif self.storyState == CommuteState.ARRIVE_SJ_BY_CAR:
            if numChoice == 1:
                self.storyState = CommuteState.COLLEGE
        elif self.storyState == CommuteState.ARRIVE_SJ_BY_TRAIN:
            if numChoice == 1:
                self.storyState = CommuteState.COLLEGE
        elif self.storyState == CommuteState.COLLEGE:
            if numChoice == 1:
                self.storyState = CommuteState.GO_NORTH
        elif self.storyState == CommuteState.GO_NORTH:
            if numChoice == 1:
                self.storyState = CommuteState.HOME
        else:
            self.storyState = CommuteState.HOME 
    
    """
        Method isPlaying
        return:
            True if playing
            False if not
    """
    def isPlaying(self):
        return self.playingState
    
currStory = Story()
while currStory.isPlaying():
    currPrompt = currStory.getCurrentStoryStatePrompt()
    currStory.getCurrentStoryStateInput(currPrompt)