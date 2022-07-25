# KCORE EXTRACTION README

## How to run

1. Clone the repository

2. Enter the directory for KCoreExtraction:
 `cd suspensions-research/KCoreExtraction`

3. Install numpy and networkx python packages with the following commands on the shell
 `pip install -r requirements.txt`

4. Make sure the input intfile is in the data/input folder

5. Change the following variables in the source file 'CalculateKcorenessFromIntFile.py', save and close the file:
  `INPUT_PATH, OUTPUT_PATH, input_filename, output_filename, Cycles, NumberofParticles`

6. Run the script using the following command:
  `python3 src/CalculateKcorenessFromIntFile.py`
