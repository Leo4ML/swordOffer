## Thoughtworks homework  

### 输入格式和报错说明：  
输入为两行；  
1.第一行为迷宫大小，格式为：数字+空格+数字；    
1.1 违反此格式，报错‘Incorrect command format.’    
1.2 若出现非整型数字 ，报错‘Invalid number format.’
1.3 若出现小于0的数或超出范围，报错  ”Number out of range .” 
   
2.第二行为连通格子位置，输入格式为：数字+‘，’+数字+‘ ’+ 数字+‘，’+数字，已分号间隔，最后一组无符号   
2.1 违反此格式，报错 'Incorrect command format.”  
2.2 包含非整型，报错 ”Invalid number format . ” 
2.3 若出现小于0的数或超出范围，报错  ”Number out of range .” 
3.出现连通性错误，本代码中将同一个格子连自己也视为无法连通，报错”Maze format error.”  



### 测试用例 （全部达到作业要求）  
##### 正确用例 
（1）得到正确结果     
3 3     
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1 
10 10
0,1 0,2;1,2 1,3;2,3 2,4;3,4 3,5;4,5 4,6;5,6 5,7;6,7 6,8;7,8 7,9、
##### 错误用例
（1）报错1.1   ‘Incorrect command format.’    
3   
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1    
3；3   
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1    
（2）报错1.2 ‘Invalid number format.’
3.2 6.1   
3 0,1 0,2;0,0 1,0;0,1 1,1;0,6 1,6;1,0 1,1;5,1 5,2;1,1 2,1;1,2 2,2;2,0 2,1      
A 3   
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1   
（3）报错1.3  ”Number out of range .”   
3 3   
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;3,1 3,1;1,2 2,2;2,0 2,1      
-3 3   
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1     
（4）报错2.1  'Incorrect command format.”   
3 3     
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1        
（5）报错2.2 ”Invalid number format . ”    
 3 3   
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2a 2,2;2,0 2,1    
（6）报错2.3 ”Number out of range .”    
3 3   
0,1 0,2;0,0 1,0;0,1 1,1;0,-2 1,2;1,0 1,1;1,1 1,2;1,1 2,1;1,2 2,2;2,0 2,1     
（7）报错3  ”Maze format error.”
3 3  
0,1 0,2;0,0 1,0;0,1 1,1;0,2 1,2;1,0 1,1;1,1 2,2;1,1 2,1;1,2 2,2;2,0 2,1   