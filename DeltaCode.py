class DeltaCodeObject:
    """
    初始化代码解析所用值：
    1.源代码文本
    2.源代码列表
    3.代码块列表
    4.关键字列表
    5.代码块关键字列表
    6.注释字符格式
    7.源代玛字符列表
    8.处理后的源代码文本
    """

    # 1.
    SOURCE_CODE: str
    # 2.
    SOURCE_CODE_LIST: list
    # 3.
    CODE_BLOCK_LIST: list
    # 4.
    KEY_WORD_LIST: list = ["const", "let", "if", "elseif", "else", "for", "in", "while"]
    # 5.
    BLOCK_KEY_WORD_LIST: list = ["func", "object"]
    # 6.
    ANNOTATION: str = "*"
    # 7.
    SOURCE_CODE_CHAR_LIST: list
    # 8.
    PROCESSED_CODE: str

    """
    初始化代码所用值：
    1.变量列表
    2.常量列表
    """
    # 1.
    VAR_LIST: list
    # 2.
    CONST_LIST: list

    """
    初始化所用语句：
    1.定义内置函数类
    2.定义变量类
    3.定义常量类
    4.定义列表类
    5.定义Map类
    6.定义if语句类
    7.定义for语句类
    8.定义while语句类
    """

    class BuildInFunc:
        """内置函数类"""

        def __init__(self, code):
            pass

        pass

    class Variable:
        """定义变量类"""

        def __init__(self, code):
            pass

        pass

    class Constant:
        """定义常量类"""

        def __init__(self, code):
            pass

        pass

    class List:
        """定义列表类"""

        def __init__(self, code):
            pass

        pass

    class Map:
        """定义Map类"""

        def __init__(self, code):
            pass

        pass

    class IfStatement:
        """定义if语句类"""

        def __init__(self, code):
            pass

        pass

    class ForStatement:
        """定义for语句类"""

        def __init__(self, code):
            pass

        pass

    class WhileStatement:
        """定义while语句类"""

        def __init__(self, code):
            pass

        pass

    """
    代码处理主流程类

    流程如下：
    1.读取源文件为字符串
    2.在每行末尾末尾添加分号，去除注释，换行等字符
    3.使用分块函数 toblock() 将代码分解为多个代码块
    4.解析代码块，生成一级语句树
    5.将每个一级语句树的子语句不断重复3，4两步骤
    6.生成完整语句树交给解释器模块运行
    """

    def get_source_code_file(self, filename):
        f = open(file=filename, mode="rb")
        self.SOURCE_CODE = f.read().decode()
        f.close()
        f0 = open(file=filename, mode="rb")
        self.SOURCE_CODE_LIST = f.readlines()
        f0.close()

    def code_format(self):
        process = ""  # 暂存处理后的源代码
        ann_flag = 0  # 碰到注释的标志
        ann_start = 0
        ann_end = 0
        for line in self.SOURCE_CODE_LIST:
            if line[-1] != "{" or line[-1] != "}":
                line += ";"
                process += line
        for char in list(process):
            """查找注释并删除"""
            if char == self.ANNOTATION:
                if ann_flag == 1:
                    ann_end = list(process).index(char)
                    ann_flag += 1
                else:
                    ann_start = list(process).index(char)
                    ann_flag += 1

            if ann_flag == 2:
                """删除注释"""
                del list(process)[ann_end:ann_start]
                ann_start = 0
                ann_end = 0
                ann_flag = 0
        while "\n" in list(process):
            list(process).remove("\n")

        self.PROCESSED_CODE = process

    def main(self, filename):
        """主过程函数"""
