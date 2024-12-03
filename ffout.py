# Fresh Foods Program (ffout.py)
# Author: Farmandeh Bana

def create_output_file():
    # Tab for formatting the output
    tab = "\t"
    
    ############## output file ###############
    out_file = "payroll.txt"
    f = open(out_file, "w")  # Open the file for writing

    # Assuming the original output consists of employee names and their pay
    f.write("Employee Name" + tab + "Hours Worked" + tab + "Pay Rate" + tab + "Total Pay\n")
    f.write("John Doe" + tab + "40" + tab + "$15" + tab + "$600\n")
    f.write("Jane Smith" + tab + "38" + tab + "$16" + tab + "$608\n")
    f.write("Sam Brown" + tab + "42" + tab + "$14" + tab + "$588\n")

    f.close()  # Close the file
    print("Open " + out_file + " to view your report")

def main():
    create_output_file()  # Call the function to create the output file

if __name__ == "__main__":
    main()
