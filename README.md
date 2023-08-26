# Judd-Ofelt

## Usage
1. Install anaconda3 for windows → [link](https://www.anaconda.com/download#downloads)
2. open anaconda prompt from start menu

3. Run the following commands in anaconda prompt to prepare environment
```
cd Downloads
git clone https://github.com/ruoyuGao/Judd-Ofelt.git
conda create -n judd-ofelt python=3.6
conda activate judd-ofelt
conda install numpy
```
4. put all the input file(JO-parameter) into Juud-Ofelt/input/input_files and Juud-Ofelt/input/peak_files, input files will contain all the JO-parameters and peak files will contain all the peak files.

5. put all the input file(Transitions) into Juud-Ofelt/input/input_trans and Juud-Ofelt/input/input_nre_omiga, there will be one file to store all the nre and omiga you want, output will generate in seperate files.

6. put all the input file(magnetic) into Juud-Ofelt/input/input_magnetic, there will be one file to store all the magnetic you want, output will generate in the one file.

5. Run the following commands in anaconda prompt to run the program
```
cd Judd-Ofelt
python new_source_code/JO_parameter_script.py 
python python new_source_code/Transitions_hwy.py 
python python new_source_code/magnetic.py
```