import csv
######Rewrite on their own##############
input_filename = "dump"
atom1, num1 = "Cu", "48"
atom2, num2 = "Zr", "48"

########################################

data_list = []
with open(input_filename,newline='') as file:
    reader = csv.reader(file, delimiter=' ')
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
xlo_bound = float(data_list[5][0])
xhi_bound = float(data_list[5][1])
ylo_bound = float(data_list[6][0])
yhi_bound = float(data_list[6][1])
zlo_bound = float(data_list[7][0])
zhi_bound = float(data_list[7][1])
xy = float(data_list[5][2])
xz = float(data_list[6][2])
yz = float(data_list[7][2])
xlo = xlo_bound - min(0.0, xy, xz, xy+xz)
xhi = xhi_bound - max(0.0, xy, xz, xy+xz)
ylo = ylo_bound - min(0.0, yz)
yhi = yhi_bound - max(0.0, yz)
zlo = zlo_bound
zhi = zhi_bound
atom_num = len(data_list) - 9
with open('POSCAR', mode='w') as f:
    f.write("lammps2vasp << LAMMPS data file via writ\n")
    f.write(" 1.000000000000000\n")
    f.write("    {:.16f}   {:.16f}   {:.16f}\n".format(xhi, 0.0, 0.0))
    f.write("    {:.16f}   {:.16f}   {:.16f}\n".format(xy, yhi, 0.0))
    f.write("    {:.16f}   {:.16f}   {:.16f}\n".format(xz, yz, zhi))
    f.write("   "+atom1+"   "+atom2+"\n")
    f.write("   "+num1+"   "+num2+"\n")
    f.write("direct\n")
    data_list = data_list[-96:]
    list_1 = []
    list_2 = []
    for i in data_list:
        if i[1] == "1":
            list_1.append([float(i[2]), float(i[3]), float(i[4])])
        elif i[1] == "2":
            list_2.append([float(i[2]), float(i[3]), float(i[4])])
    for i in list_1:
            f.write("  {:.16f}  {:.16f}  {:.16f}".format(i[0], i[1], i[2]))
            f.write("\n")
    for i in list_2:
            f.write("  {:.16f}  {:.16f}  {:.16f}".format(i[0], i[1], i[2]))
            f.write("\n")
