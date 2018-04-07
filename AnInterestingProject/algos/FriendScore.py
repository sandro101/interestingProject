from collections import defaultdict


class FriendScore:
    def highestScore(self, friends):
        two_friends = defaultdict(int)
        for i, person in enumerate(friends):
            friends_of_friends = {i for i, v in enumerate(person) if v == "Y"}
            if len(friends_of_friends) > 1:
                for friend in friends_of_friends:
                    for friend2 in friends_of_friends:
                        if friend != friend2:
                            if friends[friend][friend2] != "Y":
                                two_friends[friend] += 1
            for possible_friend in person:
                if possible_friend == "Y":
                    two_friends[i] += 1

        return 0 if len(two_friends) == 0 else max(two_friends.values())


friends = ["NNNNNNNNNNNNNNY", "NNNNNNNNNNNNNNN", "NNNNNNNYNNNNNNN", "NNNNNNNYNNNNNNY", "NNNNNNNNNNNNNNY",
           "NNNNNNNNYNNNNNN", "NNNNNNNNNNNNNNN", "NNYYNNNNNNNNNNN", "NNNNNYNNNNNYNNN", "NNNNNNNNNNNNNNY",
           "NNNNNNNNNNNNNNN", "NNNNNNNNYNNNNNN", "NNNNNNNNNNNNNNN", "NNNNNNNNNNNNNNN", "YNNYYNNNNYNNNNN"]
print(FriendScore().highestScore(friends))
friends = [
 "NNNNYNNNNN",
 "NNNNYNYYNN",
 "NNNYYYNNNN",
 "NNYNNNNNNN",
 "YYYNNNNNNY",
 "NNYNNNNNYN",
 "NYNNNNNYNN",
 "NYNNNNYNNN",
 "NNNNNYNNNN",
 "NNNNYNNNNN"]
print(FriendScore().highestScore(friends))
friends = ["NYY","YNY","YYN"]
print(FriendScore().highestScore(friends))