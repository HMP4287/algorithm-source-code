result_frame = []
def solution(n, build_frame):
    # frame = [x, y, a, b] x = 가로 , y 세로, a = 0기1보, b = 0삭1설
    for frame in build_frame:
        x, y, a, b = frame
        print(frame)
        if frame[3] == 1:
            result_frame.append([x, y, a])
            if not check():
                result_frame.remove([x, y, a])
            # if frame[2] == 0:
            #
            #     result_frame.append(frame)
            #     if not check():
            #         result_frame.remove(frame)
            #
            # 바닥 위에 있어야함
            # if frame[1] == 0:
            #     result_frame.append([frame[0], frame[1], frame[2]])
            # 기둥 아래 기둥 있어야 함
            # elif [frame[0], frame[1] - 1, 0] in result_frame:
            #     result_frame.append([frame[0], frame[1], frame[2]])
            # 기둥 아래 보 있어야 함
            # elif [frame[0] - 1, frame[1], 1] in result_frame:
            #     result_frame.append([frame[0], frame[1], frame[2]])
            # 보일때
            # else:
            #
            #     보의 왼쪽 아래가 기둥.
            # if [frame[0], frame[1] - 1, 0] in result_frame:
            #     result_frame.append([frame[0], frame[1], frame[2]])
            # 보의 오른쪽 아래가 기둥
            # elif [frame[0] + 1, frame[1]-1, 0] in result_frame:
            #     result_frame.append([frame[0], frame[1], frame[2]])
            # 보의 오른쪽 왼쪽이 보
            # elif [frame[0] - 1, frame[1], 1] in result_frame and [frame[0] + 1, frame[1], 1] in result_frame:
            #     result_frame.append([frame[0], frame[1], frame[2]])
        # 삭제일때
        else:
            # del_idx = result_frame.index([frame])
            del_idx = result_frame.index([x, y, a])
            del_data = [x, y, a]
            # del_data = [frame[0], frame[1], frame[2]]
            result_frame.remove([x, y, a])
            if not check():
                result_frame.insert(del_idx, del_data)
        print("res ", end = " ")
        print(result_frame)

    result_frame.sort(key=lambda x: (x[0], x[1], x[2]))
    return result_frame


def check():
    result = True
    for frame in result_frame:
        # 기둥일때
        if frame[2] == 0:
            # 바닥 위에 있어야함
            if frame[1] == 0:
                continue
                # result = True
            # 기둥 아래 기둥 있어야 함
            elif [frame[0], frame[1] - 1, 0] in result_frame:
                continue
                # result = True
            # 기둥 아래 보 있어야 함
            elif [frame[0] - 1, frame[1], 1] in result_frame:
                continue
                # result = True
            else:
                result = False
            if not result:
                return result
        # 보일때
        else:
            # 보의 왼쪽 아래가 기둥.
            if [frame[0] + 1, frame[1] - 1, 0] in result_frame:
                continue
                # result = True
            elif [frame[0], frame[1] - 1, 0] in result_frame:
                continue
                # result = True
            # 보의 오른쪽 아래가 기둥
            elif [frame[0] + 1, frame[1], 0] in result_frame:
                continue
                # result = True
            # 보의 오른쪽 왼쪽이 보
            elif [frame[0] - 1, frame[1], 1] in result_frame and [frame[0] + 1, frame[1], 1] in result_frame:
                continue
                # result = True
            else:
                result = False
            if not result:
                return result

    return result

ans = solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
print(ans)

