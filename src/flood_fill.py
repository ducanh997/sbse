from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        dis = [1, 0, -1, 0]
        djs = [0, 1, 0, -1]

        nrow = len(image)
        ncol = len(image[0])

        oldColor = image[sr][sc]

        seen = {(sr, sc)}

        queue = [(sr, sc)]
        while queue:
            focus = queue.pop()
            focus_sr, focus_sc = focus

            image[focus_sr][focus_sc] = newColor

            for di, dj in zip(dis, djs):
                new_sr = focus_sr + di
                new_sc = focus_sc + dj

                if 0 <= new_sr < nrow and 0 <= new_sc < ncol and image[new_sr][new_sc] == oldColor and (
                        new_sr, new_sc) not in seen:
                    queue.append((new_sr, new_sc))
                    seen.add((new_sr, new_sc))

        return image
