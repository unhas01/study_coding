n = int(input())
candies=[]
ans = 1
 
for i in range(n):
    temp =[]
    temp_str = input()
    for j in range(n):
        temp.append(temp_str[j])
    candies.append(temp)
    
# 몇개 먹을 수 있는지 찾는 함수
def search():
    global ans
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candies[i][j]== candies[i][j+1]:
                cnt+=1
                ans = max(cnt,ans)
            else:
                cnt = 1
        
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candies[j][i] == candies[j+1][i]:
                cnt+=1
                ans = max(cnt,ans)
            else:
                cnt = 1
       
# 가로
for i in range(n):
    for j in range(n-1):
        candies[i][j],candies[i][j+1] = candies[i][j+1],candies[i][j]
        search()
        candies[i][j],candies[i][j+1] = candies[i][j+1],candies[i][j]

# 세로 뒤집기
for i in range(n):
    for j in range(n-1):
        candies[j][i],candies[j+1][i] = candies[j+1][i],candies[j][i]
        search()
        candies[j][i],candies[j+1][i] = candies[j+1][i],candies[j][i]

        
print(ans)