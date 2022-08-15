from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Time: O(e + v) --> number of edges and number of vertices
        # or: O(p + n) --> number of prerequisites and number of courses
        # Build the adjacency list of prerequisites 

        prereq = { c: [] for c in range(numCourses) }

        for course, pre in prerequisites:
            prereq[course].append(pre)

        # A course may has three states:
        #   (1): visited --> course has been added to the output
        #   (2): visiting --> course has not been added to the output, but added to cycle.
        #           It will allowed us to detect the cycle.
        #   (3): unvisited --> course has not been added to the output or cycle

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            
            if course in visit:
                return True

            cycle.add(course)

            for pre in prereq[course]:
                
                # We meet a cycle
                if dfs(pre) == False:
                    return False

            cycle.remove(course)
            visit.add(course)
            output.append(course)

            return True

        for c in range(numCourses):
            
            # Meet cycle
            if dfs(c) == False:
                return []
            
        return output