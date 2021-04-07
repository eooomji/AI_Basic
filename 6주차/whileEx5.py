while True:
    word=input('단어를 입력하세요: ')
    if not word:    # 입력하는 단어가 없고 enter가 들어가면 종료 => 탈출 조건
        break
    print('입력한 단어는'+ word)
