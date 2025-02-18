# Time Complexity : O(V + E) - V is number of courses and E is len of prerequisites
# Space Complexity : O(V + E) - V is number of courses and E is len of prerequisites
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no

"""
Keep track of number of prerequisites for each course in a list
Keep track of list of children/dependents for each course in a map
Add all independent courses to the queue
Iterate over queue and check what other courses can be taken based on the independent courses
"""


from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # to maintain the number of dependencies for each course
        inDegrees = [0 for i in range(0 ,numCourses)]

        # to maintain the list of courses that are depdendent on the key
        dependencyMap = {}

        # to process the courses
        queue = deque()

        # to track the number of courses that can be taken
        count = 0

        # loop through the prerequisites(edges) list to populate inDegrees and dependencyMap
        for i in range(0 ,len(prerequisites)):
            ind = prerequisites[i][0]
            dep = prerequisites[i][1]
            inDegrees[dep] += 1

            if ind not in dependencyMap:
                dependencyMap[ind] = []

            dependencyMap[ind].append(dep)

        # loop through the inDegrees list to find the independent courses and add them to the queue
        for i in range(0 ,numCourses):
            if inDegrees[i] == 0:
                count += 1
                queue.append(i)

        # if all courses are independent, all courses can be taken
        if count == numCourses: return True

        # if no courses are independent and there is a cycle, all courses cannot be taken
        if len(queue) == 0: return False


        # process the courses
        while queue:
            parent = queue.popleft()
            if parent not in dependencyMap: continue
            dependents = dependencyMap[parent]

            # process the dependent courses of the independent course
            for dependent in dependents:
                # decrement the dependency count by 1 as one dependent (prerequisite) course could be taken
                inDegrees[dependent] -= 1

                # if dependency count reduces to 0, that means all prerequisites are done and this course can be taken too
                if inDegrees[dependent] == 0:
                    count += 1
                    queue.append(dependent)
                    if count == numCourses: return True

        return False
