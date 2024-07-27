# AutoCircos project

## Overall program goal
Automatic generation of Circos for visualisation of genomic data based on 
raw FASTA files containing nucleic acid sequences.

## Detailed program flow
1) Single image with files as follows:
   - **FASTA files** are run via R script containing nucleoid acids sequences;
   - **Script R**, that generates text file containing the start and end position on the genome;
   - **metadata.ini** - configuration file with all information needed for Circos: names, number of charts, chart types and position - modified based on user input;
   - **Python scripts**:
     - **circos manipulator.py** - main script that generates and modifies the circos.conf file
     - **plotting.py** - class with methods for circos.conf modifications (start and end of chart, parameters, chart type)
2) Inserting FASTA files to container
3) Running the main program (circos_manipulator.py)
4) Generating modified circos.conf
5) Linux commands (and environment setting):
   1) Setting path to directory with circos files
   2) If no virtual enviornment
   ```shell
   conda create -n circos --file package-list.txt
   ```
   3) 
   ```shell
   conda activate circos
   ```
   4)
   ```shell
   circos --conf circos.conf 
   ```
   
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

## Prerequisites
Docker on linux

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

