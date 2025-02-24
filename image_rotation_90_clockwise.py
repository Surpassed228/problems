class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def trans_outer(start_from):
            if start_from == len(matrix)-1:
                pass
            else:
                for j in range(start_from,len(matrix)):
                    matrix[start_from][j],matrix[j][start_from] = matrix[j][start_from],matrix[start_from][j]
                trans_outer(start_from+1)
        trans_outer(0)

        for i in range(len(matrix)):
            matrix[i].reverse()
