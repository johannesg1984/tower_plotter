
import time
import os

from res_file_reader import Res_File_Reader



if __name__=="__main__":

    t_start=time.time()



    input_folder="Input"

    files=os.listdir(input_folder)
    files = [s for s in files if ".res"  in s]

    i=0

    max_files=10

    for file in files:

        res_file=Res_File_Reader.from_res_file(os.path.join(input_folder,file))
        if i>=max_files:
            break

        
        res_file.parse_angle_info()
        i+=1

    run_time=round(time.time()-t_start,2)
    print(f"Done, the runtime was {run_time} sec")