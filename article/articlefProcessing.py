class ArticleProcessing:
    def __init__(self):
        pass

    def show_total_article(self):
        total_article=0

        # open file(r)
        f=open("../article/articleReadf.txt",'r')
        lines = f.readlines()       # 모든 line의 값 가져오기
        for line in lines:
            total_article+=1        # 한 줄이 있을 때마다 총 article에 1 더함
        f.close()

        result=str(total_article)
        print("총 시간이 정상적으로 처리되었습니다. ["+result+"]")
        return result

    def the_article_is_new(self,URL):
        # open file(r)
        f = open("../article/articleReadf.txt", 'r')
        lines = f.readlines()  # 모든 line의 값 가져오기
        for line in lines:
            line = line.replace('\n', '')
            if str(URL)==str(line):
                f.close()
                return False    # 봤던 url이면 False 반환
        f.close()
        return True           # 파일에 url이 없으면 True반환


if __name__ == '__main__':
    article = ArticleProcessing()
    article.show_total_article()