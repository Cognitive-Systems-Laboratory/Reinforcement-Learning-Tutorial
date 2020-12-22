import os
from tensorboardX import SummaryWriter

def mk_directory(root,mode='DQN'):
    
    
    sub_path=os.path.join(root,mode)
    try:
        os.makedirs(sub_path)
    except:
        print("hi")
    path=os.path.join(root,mode,"%02d" %(len(os.listdir(sub_path))))
    os.makedirs(path) #Create Exp Folder
    return path

def mk_SummaryWriter(root,mode='DQN'):
    path=mk_directory(root,mode)
    summary_writer=SummaryWriter(log_dir=path,comment=mode)
    return summary_writer
def add_scalar(label,y_value,x_value,summary_writer):
    summary_writer.add_scalar(label,y_value,x_value,)    
    
#Summary_Writer=mk_SummaryWriter(root,'DQN')
#add_scalar("Score",score /print_interval,n_epi,Summary_Writer)
#add_scalar("Score",score /print_interval,n_epi,Summary_Writer)
# add_scalar("Max Score",max_score /print_interval,n_epi,Summary_Writer)
# add_scalar("Buffer Size",memory.size() /print_interval,n_epi,Summary_Writer)
# add_scalar("Epsilon",epsilon ,n_epi,Summary_Writer)
#Summary_Writer.close()
