"""
    Turing machine simulator
    actions: 
    state, symbol read -> symbol written, new state, movement
"""
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as mpatches

"""
#Adds +1 to input
actions = {
    '00': '01L',
    '10': '12S',
    '20': '',
    '01': '11L',
    '11': '11L',
    '21': ''
}
end_states = ['2']
position = 5
state = '0'
input = '0000011111000000000'
"""

#Unary addition
actions = {
    '00': '02L',
    '01': '10R',
    '0x': '11R',
    '11': '10R',
    '21': '03S'
}
end_states = ['3']
position = 5
state = '0'
input = '0000011x1110000'

def run(p, s, i, a):
    #position, state, position, actions 
    try:
        a = actions[s+i[p]]
    except:
        return (p,s,i)
    if a=='':
        return (p,s,i)
    else:
        new_state = a[1]
        new_input = list(input)
        new_input[position] = a[0]
        new_input = "".join(new_input)
        if a[2]=='R':
            new_position = p+1
        if a[2]=='L':
            new_position = p-1
        if a[2]=='S':
            new_position = p
            #print("Stay there")
        return (new_position, new_state, new_input)
        
def prettyPrint(p,s,i):
    print(i)
    print(' '*p +'|')
    print(' '*p +s)


colorscheme = {
    '0': 'plum',
    '1': 'salmon',
    '2': 'orange',
    '3': 'red'
}

def plotting(p,s,i,y,c):
    for x in range(len(i)):
        if i[x]=='1':
            plt.scatter(x,y, color = c[s], marker = "s")
        else:
            plt.scatter(x,y, color = 'white')
    plt.scatter(p,y-.15, color = 'black', marker="2")	
    plt.scatter(p,y-.24, color = 'black', marker="o")	
    plt.scatter(p,y-.24, color = c[s], marker=".")	

def plottingTape(p,s,i,y,c):
    for x in range(len(i)):
        
        if i[x]=='1':
            plt.scatter(x-p,y, color = c[s], marker = "s")
        else:
            plt.scatter(x-p,y, color = 'white')
    plt.scatter(0,y-.15, color = 'black', marker="2")
    plt.scatter(0,y-.24, color = 'black', marker="o")
    plt.scatter(0,y-.24, color = c[s], marker=".")



i = 0
while i<10 and not (state in end_states):
    i+=1
    prettyPrint(position, state, input)
    plottingTape(position, state, input, 10-i, colorscheme)
    position, state, input = run(position, state, input, actions)
i+=1
plottingTape(position, state, input, 10-i, colorscheme)
prettyPrint(position, state, input)
if state in end_states:
    print("Computation complete!")
legends = []
for k in colorscheme.keys():
    legends.append(mpatches.Patch(color=colorscheme[k], label='state '+k))
plt.legend(handles=legends)
plt.title("Unary addition")
plt.show()
