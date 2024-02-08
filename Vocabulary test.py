# 导入模块
import pyodbc  # python 导入 Access
import openpyxl  # python 导入 Excel
import sys  # 导入系统模块


class App:
    def __init__(self):
        # 变量设定
        self.B = None
        self.C = None
        self.n = 2  # 设定Excel读取行
        # 数据变量初始化
        self.cellA = None
        self.cellB = None
        self.cellC = None
        self.cellD = None
        # 数据导入变量初始化
        self.word = ""
        self.pos = ""
        self.po = ""
        self.pron = ""
        self.pro = ""
        self.mean = ""
        # Access打开文件并建立游标访问
        self.acc = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=.\Words.accdb")
        self.tabl = self.acc.cursor()
        # Excel打开文件并打开表格
        self.wordbook = openpyxl.load_workbook(filename="./Words.xlsx")
        self.sheet = self.wordbook["Sheet1"]

        self.column = "Word, PartOfSpeech, Pronunciation, Meaning".split(",")  # 将四列标题存为表格形式
        # 将用户查看词性存为表格
        self.pos_lis_user = ["a.形容词", "a.interr.疑问形容词", "adv.副词", "conj.连词",
                             "loc.短语", "loc.adv.副词短语", "n.名词", "n.f.阴性名词", "n.f.pl.阴性复数名词",
                             "n.m.阳性名词", "n.m.pl.阳性复数名词", "prép.介词", "pron.代词", "pron.indéf.泛指代词",
                             "pron.interr.疑问代词", "v.i.不及物动词", "v.pr.代词式动词", "v.t.及物动词", "v.t.ind.间接及物动词"]
        # 判断用户输入词性表格
        self.pos_lis = ["a.", "a.interr.", "adv.", "conj.",
                        "loc.", "loc.adv.", "n.", "n.f.", "n.f.pl.",
                        "n.m.", "n.m.pl.", "prép.", "pron.", "pron.indéf.",
                        "pron.interr.", "v.i.", "v.pr.", "v.t.", "v.t.ind."]
        # 大表格，Excel数据打包存入Access
        self.lis = []

    def main(self):
        print("请问您是要用输入的方式还是Excel的方式录入法语单词？")
        while True:
            self.C = input("A. 输入\tB.Excel\n")
            if self.C in ["A", "a"]:
                print("好的。")
                self.inp_in()
                break
            elif self.C in ["B", "b"]:
                print("好的。")
                self.exc_in()
                break
            else:
                print("您输入的并不是A或B，请重新输入。")
                continue

    def inp_in(self):
        try:
            self.B = int(input("请问您要输入几个词语？"))
        except ValueError:
            print("您输入的并不是数字，请重新输入。")
        for i in range(self.B):  # 用变量b遍历，获取Excel表中每一行的数据
            self.word = input("请输入第{}个词语：".format(i + 1))  # 将word变量设为用户输入的词语
            if "'" in self.word:
                self.word = "''".join(self.word.split("'"))  # 适应SQL语言，将单撇变为双撇，在执行时便会被编译成单撇
            while True:  # 死循环以判断词性是否可以录入
                self.po = input("请输入词性（查看词性请输入”查看词性“）：")
                if self.po == "查看词性":  # 判断用户是否想要查看词性
                    for j in self.pos_lis_user:  # 将用户查询的词性表遍历
                        if (self.pos_lis_user.index(j) + 1) % 4 == 0:  # 用取余的方法将每一行的变量数固定
                            print(j, end="、\n")
                        elif self.pos_lis_user.index(j) + 1 == len(self.pos_lis_user):  # 如果变量是最后一个，那么不输出括号
                            print(j)
                        else:  # 如果上面的都不是，就只输出顿号
                            print(j, end="、")
                elif self.po in self.pos_lis:  # 如果词性输入在可接受范围内就退出循环
                    self.pos = self.po  # 如果词性不允许不存储到真正的变量
                    del self.po
                    break
                else:  # 如果输入的既不是允许的词性或者查询词性，便让用户重新输入。
                    print("您输入的不是允许的词性，请重新输入。")
                    continue
            while True:  # 死循环判断音标是否允许
                self.pro = input("请输入音标：")
                if self.pro[0] != "[" or self.pro[-1] != "]":  # 判断音标左右是否没有有中括号
                    print("请按照\"[音标]\"格式输入。")  # 如果没有重新输入
                    continue
                else:  # 输入允许判断
                    self.pron = self.pro  # 存储真实变量
                    del self.pro
                    break
            self.mean = input("请输入意思：")  # 意思格式无需判断，直接存入
            # 将四个变量存入
            self.tabl.execute("INSERT INTO Words ({}) VALUES ('{}')".format(
                ",".join(self.column), "','".join([self.word, self.pos, self.pro, self.mean])
            ))

    def exc_in(self):
        while True:  # 死循环将每行的数据录入
            # 每行四列中的数据存入到四个变量中
            self.cellA = self.sheet["A{}".format(self.n)]
            self.cellB = self.sheet["B{}".format(self.n)]
            self.cellC = self.sheet["C{}".format(self.n)]
            self.cellD = self.sheet["D{}".format(self.n)]
            if self.cellA.value is None or self.cellB.value is None or self.cellC.value is None or self.cellD.value is None:  # 判断单元格是否为空
                if self.n == 2:  # 判断空单元格是否是第一行
                    print("您还没有录入信息，请重新录入。")  # 如果空单元格在第一行那么就是未录入信息
                    sys.exit()  # 调用系统模块退出程序
                else:  # 如果空单元格不在第一行，那么就是信息截至可录入
                    for k in self.lis:  # 遍历大列表，获得小列表
                        self.tabl.execute("INSERT INTO Words ({}) VALUES ('{}')"
                                          .format(",".join(self.column), "','".join(k)))  # 将小列表中的数据按SQL语言逻辑写入
                    self.tabl.execute("SELECT * FROM Words ORDER BY Word ASC;")  # 将数据库排序
                    print("已录入完成。")
                    break  # 退出死循环上传
            if "'" in self.cellA.value:  # 判断单撇是否在单词中（如s'appeler这种词）
                word = "''".join(self.cellA.value.split("'"))  # 适应SQL语言，将一个撇变为两个撇，在SQL语言执行操作时会将''视为单撇
            else:  # 如果没有单撇便正常录入
                word = self.cellA.value
            if self.cellB.value not in self.pos_lis:  # 判断词性是否没在词性表内
                print("您在B{}处输入的词性不允许，请重新输入。".format(self.n))  # 如果没在，提示重新输入并退出程序
                sys.exit()
            pos = self.cellB.value  # 录入信息，如果词性不允许即会退出程序，不运行此代码
            if self.cellC.value[0] != "[" or self.cellC.value[-1] != "]":  # 判断音标左右是否没有中括号
                print("您在C{}处应输入\"[音标]\"，请重新输入。".format(self.n))  # 提示用户重新输入并退出程序
                sys.exit()
            # 录入信息
            pron = self.cellC.value
            mean = self.cellD.value
            self.lis.append([word, pos, pron, mean])  # 将信息存入大列表内
            self.n += 1  # 改变行数变量，切换至下一行

    def commit(self):
        # 提交Access
        self.tabl.commit()

    def close(self):
        # 关闭Access
        self.tabl.close()
        self.acc.close()
        # 关闭Excel
        self.wordbook.close()


if __name__ == "__main__":
    app = App()
    app.main()
