class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i: [] for i in range(numCourses)}
        
        for pr in prerequisites:
            prereq[pr[0]].append(pr[1])
            
        completedCourse = set()
        
        cycle = set()
        def courseCanCompleted(course):
            if course in completedCourse:
                return True
            if course in cycle:
                return False
            
            cycle.add(course)
            for p in prereq[course]:
                if courseCanCompleted(p)==False:
                    return False   
            cycle.remove(course)
            completedCourse.add(course)
            return True
        
        for c in range(numCourses):
            
            if not courseCanCompleted(c):
                return False
        
        return True
        