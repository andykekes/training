class algoVitalsign():

    def __init__(self):
        self.rawdata = []
        return
    
    def reduce_rawdata(self, data):
        print("reduce_rawdata")
        return data

    def push_rawdata(self, data):
        print("push_rawdata")
        self.rawdata.append(data)
        return
    def get_rawdata(self):
        print("get_rawdata")
        return self.rawdata

    def algo_vitalsign_hr(self):
        print("algo_vitalsign_hr")
        return 70
    
    def algo_vitalsign_br(self):
        print("algo_vitalsign_br")
        br = 10*15
        return br