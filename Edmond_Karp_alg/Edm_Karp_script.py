import numpy as np

infile = open("file.in", "r", encoding='UTF8')
outfile = open("file.out", "w", encoding='UTF8')

first_str = infile.readline()
params = first_str.split()
g_size = int(params[0])
weight_arr = []
sourses = []
drains = []

total_stream = 0
stream_arr = []
added_streams = []
for i in range(g_size):
    stream_arr.append([0 for j in range(g_size)])
while True:
    line = infile.readline().split()
    if not line:
        break
    for i in range(len(line)):
        if line[i] == '*':
            line[i] = '0'
    weight_arr.append([int(item) for item in line])
weight_matrix = np.array(weight_arr, int)

for i in range(g_size):
    trig_str = 0
    trig_stl = 0
    stroka = weight_matrix[i]
    stolbec = weight_matrix[:, i]
    for j in range(g_size):
        if stroka[j] != 0:
            trig_str = 1
        if stolbec[j] != 0:
            trig_stl = 1
    if trig_str == 0:
        drains.append(i)
    if trig_stl == 0:
        sourses.append(i)

print(sourses)
print(drains)
print()


def width_search(sourse, drain):
    # print(sourse)
    # print(drain)
    visited = {}
    queue = []
    parent = sourse
    put = []
    last_top = drain
    for i in range(g_size):
        if weight_arr[sourse][i] != 0:
            queue.append(i)
            visited[i] = parent
    # print(visited)
    # print(queue)
    if not queue:
        return []

    while drain not in visited:
        if not queue:
            # print("РїСѓС‚Рё РЅРµС‚")
            return []
        top = queue[0]
        queue.pop(0)
        parent = top
        # print()
        # print(visited)
        for i in range(g_size):
            if weight_arr[top][i] != 0 and i not in queue and i not in visited:
                visited[i] = parent
                queue.append(i)
                if i == drain:
                    last_top = i
                    break
    while last_top != sourse:
        put.insert(0, last_top)
        last_top = visited[last_top]
    put.insert(0, sourse)
    # print(put)
    return put


# width_search(sourses[0], drains[0])


def edm_karp_alg():
    global total_stream
    for i in range(len(sourses)):
        for j in range(len(drains)):
            put = width_search(sourses[i], drains[j])
            while put:
                put = width_search(sourses[i], drains[j])
                print(put)
                if not put:
                    continue
                # print()
                # print(put)
                min_potok = weight_arr[put[0]][put[1]]
                for q in range(1, len(put)):
                    if weight_arr[put[q - 1]][put[q]] < min_potok:
                        min_potok = weight_arr[put[q - 1]][put[q]]
                # print(min_potok)
                added_streams.append(min_potok)
                for q in range(1, len(put)):
                    weight_arr[put[q - 1]][put[q]] = weight_arr[put[q - 1]][put[q]] - min_potok
                    stream_arr[put[q - 1]][put[q]] = stream_arr[put[q - 1]][put[q]] + min_potok
                total_stream = total_stream + min_potok


edm_karp_alg()
sourses = [str(item + 1) for item in sourses]
drains = [str(item + 1) for item in drains]
added_streams = [str(item) for item in added_streams]
# print(' '.join(sourses))
outfile.write(' '.join(sourses))
outfile.write('\n')
# print(' '.join(drains))
outfile.write(' '.join(drains))
outfile.write('\n')
# print(', '.join(added_streams))
outfile.write(', '.join(added_streams))
outfile.write('\n')
for i in range(g_size):
    stream_arr[i] = [str(item) for item in stream_arr[i]]
    # print(' '.join(stream_arr[i]))
    outfile.write(' '.join(stream_arr[i]))
    outfile.write('\n')
print(total_stream)
outfile.write(str(total_stream))
outfile.write('\n')
outfile.close()