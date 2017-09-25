from enums.unwatched import *
from enums.watched import *
from enums.state import *

import argparse

from utils.maths_helper import *
from utils.list_helper import *

from math import pow


class Main:
    def __init__(self):
        # Initialize vars
        self.users = {}
        self.user_watched = {}
        self.playersUnwatched = {}

        # Works
        self.works = {}
        self.categories = {}

        # Initializalize users
        for p_id in range(1983):
            self.users[p_id] = {}
            self.user_watched[p_id] = []
            self.playersUnwatched[p_id] = []

        self.similarity_matrix = {}

    def process(self, users, works):
        # Check size of arrays
        assert len(users) == len(works)

        #  Calculate probabilities
        n = len(users)

        data = []
        for j in range(n):
            try:
                if j % 100 == 0:
                    print("\tUnit begin " + str(j) + "(" + str(users[j]) + ", " + str(works[j]) + ")")

                r = self.find_probability(users[j], works[j])
                data.append(r)

                if j % 100 == 0:
                    print("\tUnit ended " + str(j) + "(" + str(users[j]) + ", " + str(works[j]) + ") || " + str(r))
                    print("")

            except Exception as e:
                print("Error" + repr(e))
                exit(1)

        return data

    @staticmethod
    def get_factor(val):
        i = Watched.get_factor(val)

        if i is None:
            return Unwatched.get_factor(val)

        return i

    @staticmethod
    def assign(value):
        r = Watched.assign(value)

        if r is None:
            r = Unwatched.assign(float(value))

        if r is None:
            raise Exception("Error with " + value)

        return r

    def has_watched(self, user, work):
        return Watched.assign(self.users[user][work]) is not None

    def add_user(self, user, work, value):
        self.users[user][work] = self.assign(value)

        if Watched.assign(value) is not None:
            self.user_watched[user].append(work)
        else:
            self.playersUnwatched[user].append(work)

    def add_work(self, work, category):
        self.works[work] = category

        if category not in self.categories.keys():
            self.categories[category] = []

        self.categories[category].append(work)

    def calculate_similarity(self, u1, u2, category):
        pass

    def get_similarity(self, u1, u2):
        # Try to search val in cache
        try:
            return self.similarity_matrix[(u1, u2)]
        except KeyError:
            pass

        try:
            return self.similarity_matrix[(u2, u1)]
        except KeyError:
            pass

        # If val isn't in cache, we calculate it
        self.similarity_matrix[(u1, u2)] = None
        return self.similarity_matrix[(u1, u2)]

    def get_similarity_with_category(self, u1, u2, category):
        # Try to search val in cache
        try:
            return self.similarity_matrix[(u1, u2, category)]
        except KeyError:
            pass

        try:
            return self.similarity_matrix[(u2, u1, category)]
        except KeyError:
            pass

        # If val isn't in cache, we calculate it
        self.similarity_matrix[(u1, u2, category)] = None
        return self.similarity_matrix[(u1, u2)]

    def find_probability(self, user, work):
        for p in self.users:
            if (p != user) and (work in self.users[p].keys()):
                pass

        return prob


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process')
    parser.add_argument('--train', dest='train_file', help='The train file')
    parser.add_argument('--test', dest='test_file', help='The test file')
    parser.add_argument('--watched', dest='watched_file', help='The watched file')
    parser.add_argument('--output', dest='output_file', help='The output file')

    args = parser.parse_args()
    print("Args : " + repr(args))

    #  Run instance of process
    app = Main()

    for fileName in [args.train_file, args.watched_file]:
        with open(fileName, 'r') as file:
            l = 0
            for line in file:
                if l > 0:
                    user_id, work_id, rating = line.split(',')
                    app.add_user(int(user_id.rstrip()),
                                 int(work_id.rstrip()),
                                 rating.rstrip())
                l += 1

    with open(args.titles_file, 'r') as file:
        l = 0
        for line in file:
            if l > 0:
                work_id, title, work_category = line.split(',')
                app.add_work(int(work_id.rstrip()),
                             work_category.rstrip())
            l += 1

    given_players, given_works = [], []

    # Read test
    with open(args.test_file, 'r') as file:
        l = 0
        for line in file:
            if l > 0:
                user_id, work_id = line.split(',')
                given_players.append(int(user_id.rstrip()))
                given_works.append(int(work_id.rstrip()))
            l += 1

    # Run program
    result = app.process(given_players, given_works)

    # Write result
    with open(args.output_file, 'w') as file:
        for k in range(-1, len(result)):
            if k == -1:
                file.write("user_id,work_id,prob_willsee\n")
            else:
                file.write(str(given_players[k]) + "," + str(given_works[k]) + "," + str(result[k]) + "\n")
            k += 1
