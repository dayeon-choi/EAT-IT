class TimeProcessing:
    def __init__(self):
        pass

    def show_total_time(self):
        total_hour = 0
        total_minute = 0
        total_second = 0
        to_add_minute = 0
        to_add_hour = 0

        # open file(r)
        f=open("../article/timef.txt",'r')
        # 모든 line의 값 가져오기
        lines = f.readlines()

        # 시간과 분 분리
        for line in lines:
            line_str=line.replace('\n','')
            total_minute+=int(line_str[:line.index(':')])
            total_second += int(line_str[line.index(':')+1:])

        # close file
        f.close()

        if total_second//60 != 0:               #총 second를 60으로 나눈 몫이 있을 때
            to_add_minute = total_second//60    #총 minute에 더할
            total_minute += to_add_minute       #총 munute에 더함
            total_second -= (60*to_add_minute)  #총 second에서 분으로 올려준 second만큼 뺌
        if total_minute//60!=0:                 #총 minute를 60으로 나눈 몫이 있을 때
            to_add_hour = total_minute//60      #총 hour에 더할
            total_hour += to_add_hour           #총 hour에 더함
            total_minute -= (60*total_hour)     #총 minute에서 시간으로 올려준 minute만큼 뺌

        result=str(total_hour)+"H "+str(total_minute)+"M "+str(total_second)+"S"
        print("총 시간이 정상적으로 처리되었습니다. ["+result+"]")

        return result

if __name__ == '__main__':
    time = TimeProcessing()
    time.show_total_time()
