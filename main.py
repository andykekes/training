from vitalsign import algo_Vitalsign

def main():
    # vitalsign (yue)
    vs = algo_Vitalsign.algoVitalsign()
    vs.reduce_rawdata(1)
    vs.push_rawdata(5)
    # fall     (kevin)


main()