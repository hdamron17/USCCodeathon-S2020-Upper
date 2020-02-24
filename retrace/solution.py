# Solves retrace problem using longest palindrome substring algorithm
# Author: Hunter Damron

# Longest palindrome substring algorithm modified from
# https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-3-2/

def findLongestPalindromicString(text):
    N = len(text)
    if N == 0:
        return
    N = 2*N+1    # Position count
    L = [0] * N
    L[0] = 0
    L[1] = 1
    C = 1     # centerPosition
    R = 2     # centerRightPosition
    i = 0    # currentRightPosition
    iMirror = 0     # currentLeftPosition
    maxLPSLength = 0
    maxLPSCenterPosition = 0
    start = -1
    end = -1
    diff = -1

    # Uncomment it to print LPS Length array
    # print("%d %d " % (L[0], L[1]))
    for i in range(2,N):

        # get currentLeftPosition iMirror for currentRightPosition i
        iMirror = 2*C-i
        L[i] = 0
        diff = R - i
        # If currentRightPosition i is within centerRightPosition R
        if diff > 0:
            L[i] = min(L[iMirror], diff)

        # Attempt to expand palindrome centered at currentRightPosition i
        # Here for odd positions, we compare characters and
        # if match then increment LPS Length by ONE
        # If even position, we just increment LPS by ONE without
        # any character comparison
        try:
            while ((i+L[i]) < N and (i-L[i]) > 0) and \
                    (((i+L[i]+1) % 2 == 0) or \
                    (text[(i+L[i]+1)//2] == text[(i-L[i]-1)//2])):
                L[i]+=1
        except Exception as e:
            pass

        if L[i] > maxLPSLength:        # Track maxLPSLength
            maxLPSLength = L[i]
            maxLPSCenterPosition = i

        # If palindrome centered at currentRightPosition i
        # expand beyond centerRightPosition R,
        # adjust centerPosition C based on expanded palindrome.
        if i + L[i] > R:
            C = i
            R = i + L[i]

    # Uncomment it to print LPS Length array
    # print("%d " % L[i])
    start = (maxLPSCenterPosition - maxLPSLength) // 2
    end = start + maxLPSLength - 1
    return text[start:end+1]

# Converts command sequence to positions
vel_cycle = [(0,1), (1,0), (0,-1), (-1,0)]
def drive(cmd, pos, vel):
    # Calculates new position and velocity
    if cmd == "f":
        return (pos[0] + vel[0], pos[1] + vel[1]), vel
    else:  # 'r' or 'l'
        i = vel_cycle.index(vel)
        inew = (i + (1 if cmd == 'r' else -1)) % len(vel_cycle)
        return pos, vel_cycle[inew]

def solve(ds):
    pos = (0,0)
    vel = (0,1)
    path = [pos]
    for d in ds:
        pos, vel = drive(d, pos, vel)
        if d == 'f':
            path.append(pos)
    retrace = findLongestPalindromicString(path)
    return (len(retrace) + 1) // 2

if __name__ == "__main__":
    n = int(input())
    ds = input()
    print(solve(ds))