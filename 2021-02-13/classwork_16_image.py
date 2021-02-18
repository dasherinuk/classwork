class Image:
    def __init__(self, row, col, fill):
        self.row = row
        self.col = col
        self.fill = fill
        self.img = [[' ']*col for i in range(0,row)]

    def draw_horisontal_line(self, row, col1, col2):
        for i in range(col1, col2+1):
            self.img[row][i]=self.fill

    def draw_vertical_line(self,col,row1,row2):
        for i in range(row1,row2+1):
            self.img[i][col]=self.fill
            

    def __str__(self):
        result = ""
        for i in range(0,self.row):
            for j in range(0,self.col):
                result+=self.img[i][j]
            result+="\n"
        return result


img = Image(10,10,'*')
img.draw_horisontal_line(4, 3 ,6)
img.draw_vertical_line(3, 4 ,9)
print(img)
