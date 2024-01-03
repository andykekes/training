from vitalsign import algo_Vitalsign
from fall import algo_Fall

def main():
    # vitalsign (yue)
    vs = algo_Vitalsign.algoVitalsign()
    vs.reduce_rawdata(1)
    vs.push_rawdata(5)
    # fall     (kevin)
    fall = algo_Fall.algoFall() 
    fall.reduce_rawdata("123") 
    print(fall.algo_fall_status())

main()