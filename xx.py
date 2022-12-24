import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
# 1,4 ,7 m1 ---- 9, 12, 15

f = open('out1.txt')
n = f.readline()

    # dict(Task="", Start='', Finish='', Resource=""),
    # dict(Task="", Start='', Finish='', Resource=""),
    # dict(Task="", Start='', Finish='', Resource="")
df = pd.DataFrame(columns=['Task', 'Start', 'Finish', 'Resource'])

m1_req_list = []
m1_end_list = []

m2_req_list = []
m2_end_list = []

m3_req_list = []
m3_end_list = []

m1_task_list = []
m2_task_list = []
m3_task_list = []
c = 0
for line in f:
    number = line.split(' ')
    if number[0] == "id:":

        task_m1 = number[1].split(";")

        if task_m1[0].isnumeric():
            m1_task = task_m1[0]
            m1_task_list.append(m1_task)
        else:
            pass

        m1_time_req = number[4].split(";")
        if m1_time_req[0].isnumeric():
            time_m1 = m1_time_req[0]
            m1_req_list.append(time_m1)
        else:
            pass

        m1_end = number[7].split(";")
        if m1_end[0].isnumeric():
            end_m1 = m1_end[0]
            m1_end_list.append(end_m1)
        else:
            pass

        # --------------------------------------------------------------------
        task_m2 = number[9].split(";")
        if task_m2[0].isnumeric():
            m2_task = task_m2[0]
            m2_task_list.append(m2_task)
        else:
            pass

        m2_time_req = number[12].split(";")
        if m2_time_req[0].isnumeric():
            time_m2 = m2_time_req[0]
            m2_req_list.append(time_m2)
        else:
            pass

        m2_end = number[15].split(";")
        if m2_end[0].isnumeric():
            end_m2 = m2_end[0]
            m2_end_list.append(end_m2)
        else:
            pass

# --------------------------------------------------------------------
        task_m3 = number[18].split(";")
        if task_m3[0].isnumeric():
            m3_task = task_m3[0]
            m3_task_list.append(m3_task)
        else:
            pass

        m3_time_req = number[21].split(";")
        if m3_time_req[0].isnumeric():
            time_m3 = m3_time_req[0]
            m3_req_list.append(time_m3)
        else:
            pass

        m3_end = number[24].split("\n")
        if m3_end[0].isnumeric():
            end_m3 = m3_end[0]
            m3_end_list.append(end_m3)
            total_flow_time=0
            for i in m3_end_list:
                total_flow_time += int(i)
        else:
            pass


        # if c == 0:
        #     df2 = {'Task': m1_task, 'Start': 0, 'Finish': end_m1, 'Resource': 'M1'}
        #     df3 = {'Task': m2_task, 'Start': end_m1, 'Finish': end_m2, 'Resource': 'M2'}
        #     df = df.append(df2, ignore_index = True)
        #     df = df.append(df3, ignore_index=True)
        #     c += 1
        # else:
        #     finish1 = int(m1_time_req[0]) + int(m1_end[0])
        #     finish2 = int(m2_time_req[0]) + int(m1_end[0])
        #
        #     df2 = {'Task': int(m1_task), 'Start': int(m1_end[0]), 'Finish': finish1, 'Resource': 'M1'}
        #     df3 = {'Task': int(m2_task), 'Start': int(m2_end[0]), 'Finish': finish2, 'Resource': 'M2'}
        #     df = df.append(df2, ignore_index=True)
        #     df = df.append(df3, ignore_index=True)

    else:
        pass


print(m1_req_list)
print(m2_req_list)
print(m3_req_list)

print(m1_end_list)
print(m2_end_list)
print(m3_end_list)

print(m1_task_list)
print(m2_task_list)
print(m3_task_list)



for i in range(len(m1_task_list)):
    finish1 = int(m1_end_list[i]) + int(m2_req_list[i])
    finish2 = int(m2_time_req[0]) + int(m1_end_list[0])
    finish3 = int(m3_req_list[0]) + int(m2_end_list[0])


    if c == 0:
        df2 = {'Task': m1_task_list[i], 'Start': 0, 'Finish': m1_end_list[i], 'Resource': 'M1'}
        df3 = {'Task': m2_task_list[i], 'Start': m1_end_list[i], 'Finish':finish1 , 'Resource': 'M2'}
        #df4 = {'Task': m3_task_list[i], 'Start': m2_end_list[i], 'Finish':finish2 , 'Resource': 'M3'}
        df4 = {'Task': m3_task_list[i], 'Start': m2_end_list[i], 'Finish':finish3 , 'Resource': 'M3'}

        df = df.append(df2, ignore_index = True)
        df = df.append(df3, ignore_index=True)
        df = df.append(df4, ignore_index=True)
        c += 1
    else:
        df2 = {'Task': m1_task_list[i], 'Start': m1_end_list[i-1], 'Finish': m1_end_list[i], 'Resource': 'M1'}
        df3 = {'Task': m2_task_list[i], 'Start': max(int(m1_end_list[i]), int(m2_end_list[i-1])), 'Finish': m2_end_list[i], 'Resource': 'M2'}
        df4 = {'Task': m3_task_list[i], 'Start': max(int(m2_end_list[i]), int(m3_end_list[i-1])), 'Finish': m3_end_list[i], 'Resource': 'M3'}

        df = df.append(df2, ignore_index=True)
        df = df.append(df3, ignore_index=True)
        df = df.append(df4, ignore_index=True)

print(df)
print("\n")
print("Total flow time: ", total_flow_time)
print("Average flow time: ", total_flow_time/len(m2_task_list))
print("\n")
fig = ff.create_gantt(df, index_col = 'Task',  bar_width = 0.4, show_colorbar=True)
fig.update_layout(xaxis_type='linear', autosize=False, width=800, height=400)

fig.show()
#fig.write_image("gantt2.png")
#fig.write_image("gantt2.png")
