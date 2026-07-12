
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Approach:
        1. Create a graph of each course num, with parent tracking done by iterating over prerequisites
        2. for each course, check if a cycle exists
            a. can do by running dfs on each node and maintaining a visited set
            b. for each dependency we track, check if the current node exists in its visited set. if it does, cycle exists
        '''
        # Create graph
        adjList = { i:[] for i in range(numCourses) }
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        # Define DFS and visited set
        visited = set()
        def dfs(course):
            # base case 1: No dependencies, course can be finished
            if not adjList[course]:
                return True

            # base case 2: course in visited set for prereq traversal
            # impossible to complete all prerequisites
            if course in visited:
                return False
            
            # otherwise, add course to visited set, add prereqs to recursion stack
            visited.add(course)
            for c in adjList[course]:
                # if any prereq recurses to False, return false
                if not dfs(c):
                    return False
            # reset visited set so we can run on other nodes
            visited.remove(course)
            # optimization: remove course node from graph so we don't repeat work
            adjList[course] = []
            return True

        # run dfs on every course
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
