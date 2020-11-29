# About this package
This package provides a python script to convert the structure files used by LAMMPS and VASP to each other.


### POSCAR2lammps.py
Python script to convert POSCAR file into a file that can be read by LAMMPS read_data command.
In POSCAR file, the atomic positions are provided in direct coordinates. 

### dump2POSCAR.py
Python script to convert dump file output by LAMMPS into POSCAR file.
you need to write 

```
dump 1 all custom 1000 dump id type xs ys zs 
```
in the LAMMPS input file.


