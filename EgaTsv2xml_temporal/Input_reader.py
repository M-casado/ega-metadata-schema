import sys
import pandas as pd
#! Also need to install "openpyxl" package if you don't have it installed along pandas.
import os
from yaml import safe_load

# Headers that define attributes within the YAML configuration file
required_headers_key = "required"

class Input_reader():
    """
    Reader for CSV / TSV / XLSX (excel) input that contains the metadata information
    """
    def __init__(self, input_file, conf_file, conf_key):
        """
        Initialization (constructor) of an instance.

        Parameters:
            - self: not given, it's the instance itself.
            - input_file (str): file path to the input file (.tsv, .csv or .xlsx | e.g. samples.tsv)
            - conf_file (str): file path to the configuration file (e.g. conf.yaml)
            - conf_key (str): key string that defines the metadata object (e.g. "sample" or "run")
        """

        self.conf_key = conf_key
        # We load the YAML file, creating a dictionary (of dictionaries) with its content.
        #     e.g. self.conf_dict = {'worksheets': ['Sample'], 'Sample': {'required': ['Sample_ID'], 'optional': ['Sample_title']}}
        try:
            with open(conf_file, "r") as conf_file:
                self.conf_dict = safe_load(conf_file)

        except:
            print("ERROR in Input_reader(): given configuration filepath '%s' could not be read" % conf_file, file=sys.stderr)
            sys.exit()

        # We save the basename and file extension of the input file for future checks
        self.input_file = input_file
        self.input_file_basename = os.path.basename(self.input_file)
        self.input_filetype = os.path.splitext(self.input_file)[1]

        # We generate the dataframe containing the metadata
        self.generate_dataframe()

        # We check if the input file meets the requirements (i.e. contains the required fields)
        if not self.check_if_valid():
            print("ERROR in Input_reader(): given input file (%s) does not contain the required fields for '%s' object:\n\t- Required fields: %s\n\t- Input fields: %s" \
                  % (self.input_file_basename, self.conf_key, self.required_headers, self.input_file_headers), file=sys.stderr)
            sys.exit()

    def generate_dataframe(self):
        """
        Transforms the input file into a dataframe ("self.input_dataframe"), converging from different input file
            types (.csv, .tsv and .xlsx) into a unified format.

        Regarding datatypes (dtype), we choose to preserve data as stored in the input file (dtype = "object") instead
            of letting pandas interpret it or giving a dictionary with datatypes. This approach advocates for a higher
            flexibility.
        """

        # We check the given filepath exists and is a file
        if not os.path.isfile(self.input_file):
            print("ERROR in Input_reader(): given input filepath '%s' does not exist" % self.input_file, file=sys.stderr)
            sys.exit()

        try:
            # Depending on what filetype it is, we read it with different pandas' methods
            if self.input_filetype == ".csv":
                 self.input_dataframe = pd.read_csv(filepath_or_buffer = self.input_file, sep = ",", dtype = "object")

            elif self.input_filetype == ".tsv":
                self.input_dataframe = pd.read_csv(filepath_or_buffer = self.input_file, sep = "\t", dtype = "object")

            elif self.input_filetype == ".xlsx":
                self.input_dataframe = pd.read_excel(io = self.input_file, dtype = "object", engine='openpyxl')

            else:
                # If given a filetype that we didn't expect
                print("ERROR in generate_dataframe(): given input file (%s) has extension '%s', while the allowed file types are [.csv | .tsv | .xlsx]" \
                      % (self.input_file_basename, self.input_filetype), file=sys.stderr)
                sys.exit()
        except:
            print("ERROR in Input_reader(): given input filepath '%s' could not be read" % self.input_file, file=sys.stderr)
            sys.exit()

    def check_if_valid(self):
        """
        Checks if the input file contains all the required fields (for that metadata object),
            which are described in the configuration file (indexing the corresponding object).

        Return:
            - self.is_valid (boolean): "True" if all required fields are present in the input file.
                                       "False" otherwise.
        """

        # We index the dictionary we created from the conf.yaml file (self.conf_dict) with its configuration key (e.g. Sample)
        self.required_headers = self.conf_dict[self.conf_key][required_headers_key]

        # Get the input_file headers and then compare the two
        #     (">=" so that we allow additional headers in the input file besides the required)
        self.input_file_headers = list(self.input_dataframe.columns.values)
        self.is_valid = set(self.input_file_headers) >= set(self.required_headers)

        return self.is_valid
