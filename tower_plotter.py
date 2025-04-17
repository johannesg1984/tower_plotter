import time
import os
import pandas as pd

import matplotlib.pyplot as plt

from res_file_reader import Res_File_Reader


def find_element_sizes(dataframe:pd.DataFrame,elements:list):

    pass


def plot_tower(dataframe:pd.DataFrame,foundations:pd.DataFrame,filename:str):

    y_value_right = foundations.loc[foundations['found'] == "f1", 'y'].values[0]
    y_value_left = foundations.loc[foundations['found'] == "f2", 'y'].values[0]


    # elements_right_panel=dataframe
    # elements_right_panel = dataframe[(dataframe['origin_y'] - y_value_right).abs() <= 0.1&(dataframe['end_y'] - y_value_right).abs() <= 0.1]
    elements_right_panel = dataframe[
    ((dataframe['origin_y'] - y_value_right).abs() <= 0.1) &
    ((dataframe['end_y'] - y_value_right).abs() <= 0.1)
    ]

    elements_left_panel = dataframe[
    ((dataframe['origin_y'] - y_value_left).abs() <= 0.1) &
    ((dataframe['end_y'] - y_value_left).abs() <= 0.1)
    ]
    # Create a figure with 1 row, 3 columns of axes
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 4))

    # First plot
    for _, row in elements_left_panel.iterrows():
        axes[0].plot([row['origin_x'], row['end_x']], [row['origin_z'], row['end_z']],"b")
    axes[0].set_aspect('equal', adjustable='box')
 

    # Second plot
    for _, row in dataframe.iterrows():
        axes[1].plot([row['origin_y'], row['end_y']], [row['origin_z'], row['end_z']],"b")
    axes[1].set_aspect('equal', adjustable='box')

    # Third plot
    # Note: tan grows large—limit the y‑axis for clarity
   # Second plot
    for _, row in elements_right_panel.iterrows():
        axes[2].plot([row['origin_x'], row['end_x']], [row['origin_z'], row['end_z']],"b")
    axes[2].set_aspect('equal', adjustable='box')
    plt.savefig(filename,dpi=300)





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

    max_files=20

    elements=["SOG","SUG","MMD","STV","MHJ",]

    output_csv="Output_csv"
    output_png="Output_png"

    delete_all_files(output_csv)
    delete_all_files(output_png)


    

    for file in files:
   
        res_file=Res_File_Reader.from_res_file(os.path.join(input_folder,file))
        if i>=max_files:
            break

        
        angles=res_file.parse_angle_info()
        foundations=res_file.find_foundations()
        
        angles.to_csv(os.path.join(output_csv,file[0:-4]+".csv"))
        plot_tower(angles,foundations,os.path.join(output_png,file[0:-4]+".png"))

        i+=1

    run_time=round(time.time()-t_start,2)
    print(f"Done, the runtime was {run_time} sec")