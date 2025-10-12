from collections import deque, Counter

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)
        bans = {'R': 0, 'D': 0}
        live = Counter(senate)  #count live both sides

        def other(x): 
            return 'D' if x == 'R' else 'R'

        while live['R'] and live['D']: #If both team alive
            s = q.popleft()
            if bans[s] > 0:
                bans[s] -= 1
                live[s] -= 1      
            else:
                bans[other(s)] += 1 #Ban the opposite side
                q.append(s)
        return "Radiant" if live['R'] else "Dire"
