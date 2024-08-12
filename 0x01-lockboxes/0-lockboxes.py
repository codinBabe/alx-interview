#!/usr/bin/python3
""" Lockboxes """

def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened """
    n = len(boxes)
    visited = [False] * n
    stack = [0]
    while stack:
        box = stack.pop()
        if visited[box]:
            continue
        visited[box] = True
        for key in boxes[box]:
            if 0 <= key < n and not visited[key]:
                stack.append(key)
    return all(visited)
