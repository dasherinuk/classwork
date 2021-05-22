import rectangle
class Image:#объявление класса
    def __init__(self,row, col, fill): #констркто 
        self.row = row
        self.col = col
        self.fill = fill
        self.img = [[' ']*col for i in range(0,row)]#canvas

        #[[' ', ' ',' '],
        #[' ', ' ',' '],
        #[' ', ' ',' ']]

    def draw_horisontal_line(self, row, col1, col2):
        for i in range(col1, col2+1):
            self.img[row][i]=self.fill

    def draw_vertical_line(self,col,row1,row2):
        for i in range(row1,row2+1):
            self.img[i][col]=self.fill

    def draw_square(self, row, col, size):
        size=size-1
        self.draw_horisontal_line(row, col, col+size)
        self.draw_horisontal_line(row+size, col, col+size)
        self.draw_vertical_line(col, row, row+size)
        self.draw_vertical_line(col+size, row, row+size)

    def draw_rectangle(self,row,col, w, h):
        w=w-1
        h=h-1
        self.draw_horisontal_line(row, col, col+w)
        self.draw_horisontal_line(row+h, col, col+w)
        self.draw_vertical_line(col, row, row+h)
        self.draw_vertical_line(col+w, row, row+h)
        return self

        
    def draw_diagonal_line(self,row,col):
        while col<self.col and row<self.row:
            self.img[row][col]=self.fill
            col+=1
            row+=1

    def draw_opposite_diagonal(self,row,col):
         while col<self.col and row<self.row:
            self.img[row][col]=self.fill
            col-=1
            row+=1


    

           
            
            
            
            

        
        

    def point(self,row,col):
        pass


    def add(self, img):
        new_img = Image(self.row, self.col, self.fill)
        for i in range(self.row):
            for j in range(self.col):
                new_img.img[i][j]=self.img[i][j]
                if img.img[i][j]!=' ':
                    new_img.img[i][j]=img.img[i][j]
        return new_img

    def add_shift(self,img, row_des, col_des):
        new_img = Image(self.row, self.col, self.fill)
        
        for i in range(self.row):
            for j in range(self.col):
                new_img.img[i][j]=self.img[i][j]

        for i in range(img.row):
            for j in range(img.col):
                if img.img[i][j]!=' ':
                    new_img.img[row_des+i][col_des+j]=img.img[i][j]
        return new_img
        

    #def add2(self,img):
        #new_img = Image(self.row
    def print_canvas_size(self):
        print(self.row,self.col)

    def difference_size(self,img2):
        if self.row >= img2.row and self.col>=img2.col:
            print("Yes")
        else:
            print("No")

    def inside(self,img2, x, y):
        rect1 = rectangle.Rectangle(self.row, self.col)
        rect2 = rectangle.Rectangle(img2.row, img2.col)
        return rect1.compare_size(x,y, rect2)

    def mirror_left_right(self):
        new_img = Image(self.row, self.col, self.fill)
        for i in range(self.row):
            for j in range(self.col):
                new_img.img[i][j]=self.img[i][self.col-1-j]
        return new_img

        
    def __str__(self):#метод преобразования объекта в строку 
        result = ""
        for i in range(0,self.row):
            for j in range(0,self.col):
                result+=self.img[i][j]
            result+="\n"
        return result

canvas=Image(30,30,'.')
canvas2=Image(20,20,'+')

canvas.draw_rectangle(0,0,10,10)
canvas2.draw_rectangle(0,0,10,10)
print(canvas)
print(canvas2)
print(canvas.add_shift(canvas, 0, 10).add_shift(canvas2,5,5).draw_rectangle(0,0,30,30).mirror_left_right())

##canvas.draw_diagonal_line(0,0)
##canvas2.draw_opposite_diagonal(10,10)
##print(canvas.add_shift(canvas2,0,0))
##print(canvas.add_shift(canvas2,0,5))

##canvas.draw_diagonal_line(0,0)
##canvas2.draw_opposite_diagonal(10,10)
##print(canvas.add_shift(canvas2,0,0))
##print(canvas.add_shift(canvas2,0,5))

##
##canvas.draw_vertical_line(0,0,9)
##canvas2.draw_vertical_line(10,10,10)
##print(canvas.add_shift(canvas2,0,0))
##print(canvas.add_shift(canvas2,0,5))

##canvas.draw_horisontal_line(0,0,0)
##canvas2.draw_horisontal_line(10,10,10)
##print(canvas.add_shift(canvas2,0,0))
##




