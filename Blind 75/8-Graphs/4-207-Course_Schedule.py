from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # O(n + p) -->  n: number of the course, p: the number of prerequisites
        # Map each course to prerequisite list

        # For every course, initially we wanna map it to an empty list
        preMap = { i: [] for i in numCourses}

        for course, pre in prerequisites:
            preMap[course] = pre

        # visitSet: all courses along the current DFS path
        visitSet = set()

        def dfs(course):

            # It means we are visiting a course twice --> loop
            if course in visitSet:
                return False

            # This course has no prerequisites
            if preMap[course] == []:
                return True

            visitSet.add(course)
            
            # Look through the prerequisites of this course
            for pre in preMap[course]:
                if not dfs(pre): return False

            visitSet.remove(course)

            # Since we know this course can be visited, we can set this preMap to be empty
            preMap[course] = []
            return True


        for course in numCourses:
            if not dfs(course): return False

        return True

    
s = Solution()
print(s.canFinish(2, [[1,0]]))
print(s.canFinish(2, [[1,0],[0,1]]))