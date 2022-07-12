import numpy as np

# this is my varsion of calculate function
def calculate(list):
    # checking for list input
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else:
        # initializing dictionary
        calculations = {'mean' : '', 'variance' : '', 'standard deviation' : '', 'max' : '', 'min' : '', 'sum' : ''}  
        
        a = np.array(list).reshape(3,3)
        # mean
        mean_ax0 = np.mean(a,axis=0)
        mean_ax1 = np.mean(a,axis=1)
        mean_flatten = np.mean(a.flatten())
        # variance 
        var_ax0 = a.var(axis=0)
        var_ax1 = a.var(axis=1)
        var_flatten = a.flatten().var()
        # standard deviation
        std_ax0 = np.std(a,axis=0)
        std_ax1 = np.std(a,axis=1)
        std_flatten = np.std(a.flatten())
        # max
        max_ax0 = np.max(a,axis=0)
        max_ax1 = np.max(a,axis=1)
        max_flatten = np.max(a.flatten())
        # min
        min_ax0 = np.min(a,axis=0)
        min_ax1 = np.min(a,axis=1)
        min_flatten = np.min(a.flatten())
        # sum
        sum_ax0 = a.sum(axis=0)
        sum_ax1 = a.sum(axis=1)
        sum_flatten = a.flatten().sum()
        
        # updating dictionary to corresponding value
        calculations.update({"mean":[mean_ax0.tolist(),mean_ax1.tolist(),mean_flatten]})
        calculations.update({"variance":[var_ax0.tolist(),var_ax1.tolist(),var_flatten]})
        calculations.update({"standard deviation":[std_ax0.tolist(),std_ax1.tolist(),std_flatten]})
        calculations.update({"max":[max_ax0.tolist(),max_ax1.tolist(),max_flatten]})
        calculations.update({"min":[min_ax0.tolist(),min_ax1.tolist(),min_flatten]})
        calculations.update({"sum":[sum_ax0.tolist(),sum_ax1.tolist(),sum_flatten]})
        print(calculations)
        
    return calculations
