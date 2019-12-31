import xlrd


class GetData(object):

    def __init__(self, files):
        self.file = files
        self.data = xlrd.open_workbook(files)

    def get_value(self, sheet_name):
        table = self.data.sheet_by_name(sheet_name)
        data = []
        rows = table.nrows
        for i in range(1, rows):
            r = tuple(table.row_values(i))
            data.append(r)
        return data

    def get_datas(self, sheet_name):
        table = self.data.sheet_by_name(sheet_name)
        title = table.row_values(0)
        d = self.get_value()
        title.append(d)
        return tuple(title)


if __name__ == "__main__":
    file = r'C:\sunym\03_workspace\00_PythonWorkspac\RPAControl\data\data.xlsx'
    a = GetData(file)
    print(a.get_datas())
