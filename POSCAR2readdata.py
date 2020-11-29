import csv
import numpy as np

######Rewrite on their own##############
o_name = "readdata.in" #output file name
########################################

data_list = []
with open("POSCAR",newline='') as files:
    reader = csv.reader(files, delimiter=' ')
    for row in reader:
        lis = []
        for i,w in enumerate(row):
            if w == '':
                lis.append(i)
        lis.reverse()
        for i in lis:
            del row[i]
        row2 = [str(i) for i in row]
        if row2 == []:
            continue
        data_list.append(row2)
atom_type = []
for i in data_list[5]:
    atom_type.append(i)
               
x = np.array([float(s) for s in data_list[2]])
y = np.array([float(s) for s in data_list[3]])
z = np.array([float(s) for s in data_list[4]])
x *= float(data_list[1][0])
y *= float(data_list[1][0])
z *= float(data_list[1][0])

def R_z(a):
    cos = a[0]/(a[0]**2 + a[1]**2)**0.5
    sin = a[1]/(a[0]**2 + a[1]**2)**0.5
    return np.array([[cos, sin, 0], [-1*sin, cos, 0], [0, 0, 1]])
def R_y(a):
    cos = a[0]/(a[0]**2 + a[2]**2)**0.5
    sin = a[2]/(a[0]**2 + a[2]**2)**0.5
    return np.array([[cos, 0, sin], [0, 1, 0], [-1*sin, 0, cos]])
def R_x(a):
    cos = a[1]/(a[2]**2 + a[1]**2)**0.5
    sin = a[2]/(a[2]**2 + a[1]**2)**0.5
    return np.array([[1, 0, 0], [0, cos, sin], [0, -1*sin, cos]])

Rz = R_z(x)
x = np.dot(Rz, x)
y = np.dot(Rz, y)
z = np.dot(Rz, z)
Ry = R_y(x)
x = np.dot(Ry, x)
y = np.dot(Ry, y)
z = np.dot(Ry, z)
Rx = R_x(y)
x = np.dot(Rx, x)
y = np.dot(Rx, y)
z = np.dot(Rx, z)

atom_num = str(sum([int(i) for i in data_list[6]]))
with open(o_name, mode='w') as f:
    f.write("# Model for "+"".join(data_list[5])+"\n")
    f.write("     "+atom_num+"     atoms\n")
    f.write("\n")
    f.write("         "+str(len(data_list[5]))+"     atom types\n")
    f.write("\n")
    f.write("    0.0000   "+str(x[0])+" xlo xhi\n")
    f.write("    0.0000   "+str(y[1])+" ylo yhi\n")
    f.write("    0.0000   "+str(z[2])+" zlo zhi\n")
    f.write("    "+str(y[0])+" "+str(z[0])+" "+str(z[1])+" xy xz yz\n")
    f.write("\n")
    f.write("Atoms\n")
    f.write("\n")
    count = 1
    for j in range(len(data_list[5])):
        for i in range(8+int(atom_num)//len(data_list[5])*j, 8+int(atom_num)//len(data_list[5])*(j+1)):
            x = float(data_list[i][0])
            y = float(data_list[i][1])
            z = float(data_list[i][2])
            a = np.array([x, y, z])
            S = np.array([[float(s) for s in data_list[2]], [float(s) for s in data_list[3]], [float(s) for s in data_list[4]]])
            S = S.T
            R = np.dot(S, a)*float(data_list[1][0])
            R = np.dot(Rz, R)
            R = np.dot(Ry, R)
            R = np.dot(Rx, R)    
            data_list[i][0] = str(R[0])
            data_list[i][1] = str(R[1])
            data_list[i][2] = str(R[2])
            if count < 10:
                f.write('         '+str(count)+"         "+str(j+1)+"        ")
                for k in data_list[i]:
                    if float(m) < 0:
                        f.write("     "+k[:15])
                    else:
                        f.write("      "+k[:14])
                f.write("\n")
            if count >= 10:
                f.write('        '+str(count)+"         "+str(j+1)+"        ")
                for k in data_list[i]:
                    if float(m) < 0:
                        f.write("     "+k[:15])
                    else:
                        f.write("      "+k[:14])
                f.write("\n")
            if count >= 100:
                f.write('       '+str(count)+"         "+str(j+1)+"        ")
                for k in data_list[i]:
                    if float(m) < 0:
                        f.write("     "+k[:15])
                    else:
                        f.write("      "+k[:14])
                f.write("\n")
            count += 1 
