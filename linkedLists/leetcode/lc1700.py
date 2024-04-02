students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        myCounter = Counter(students)
        for s in sandwiches:
            if myCounter[s] > 0:
                myCounter[s] -= 1
            else:
                break
        return myCounter.total()