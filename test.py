def question5(letters):
    same = False
    for i in range(len(letters)-1):
        if(letters[i]==letters[i+1]):
            same = True
            break
    
    return same

if __name__ == "__main__":
    user_input = str(input('5번 함수에 들어갈 문자열을 넣어주세요 : '))
    print(question5(user_input))