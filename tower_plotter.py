import time
import os
import pandas as pd

import matplotlib.pyplot as plt

from res_file_reader import Res_File_Reader


def find_element_sizes(dataframe:pd.DataFrame,elements:list):

    pass


def plot_tower(dataframe:pd.DataFrame,filename:str):

    plt.figure(figsize=(8, 6))

    # Loop through DataFrame rows and plot each line
    for _, row in dataframe.iterrows():
        plt.plot([row['origin_y'], row['end_y']], [row['origin_z'], row['end_z']],"b")

    plt.title('filename')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axis('equal')  # Equal scaling for x and y axes
    plt.savefig(filename,dpi=300)
    plt.axis("equal")
    plt.grid()
    plt.close()


def delete_all_files(folder_path):
    """
    Deletes all files in the specified folder. Subfolders and their contents are not affected.
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")









if __name__=="__main__":

    t_start=time.time()



    input_folder="Input"

    files=os.listdir(input_folder)
    files = [s for s in files if ".res"  in s]

    i=0

    max_files=10

    elements=["SOG","SUG","MMD","STV","MHJ",]

    output_csv="Output_csv"
    output_png="Output_png"

    delete_all_files(output_csv)
    delete_all_files(output_png)


    

    for file in files:
        print("**")
        print(file)

        res_file=Res_File_Reader.from_res_file(os.path.join(input_folder,file))
        if i>=max_files:
            break

        
        angles=res_file.parse_angle_info()
        foundations=res_file.find_foundations()
        
        angles.to_csv(os.path.join(output_csv,file[0:-4]+".csv"))
        plot_tower(angles,os.path.join(output_png,file[0:-4]+".png"))

        i+=1

    run_time=round(time.time()-t_start,2)
    print(f"Done, the runtime was {run_time} sec")