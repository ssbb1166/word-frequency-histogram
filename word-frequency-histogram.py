# word-frequency-histogram.py
from graphics import *
import time
import random


def main():
    # 메인 화면 인터페이스
    title = Text(Point(400, 350), "How Many Words in the File?")
    title.setFill("Midnight Blue")
    title.setFace("courier")
    title.setSize(33)
    title.setStyle("bold")
    helpButton = Rectangle(Point(460, 250), Point(590, 300))
    helpButton.setFill("Light Gray")
    helpButton.setOutline("Gray")
    helpButton.setWidth(3)
    helpText = Text(Point(525, 275), "HELP")
    helpText.setStyle("bold")
    quitButton = Rectangle(Point(610, 250), Point(740, 300))
    quitButton.setFill("Light Gray")
    quitButton.setOutline("Gray")
    quitButton.setWidth(3)
    quitText = Text(Point(675, 275), "QUIT")
    quitText.setStyle("bold")
    executeBox = Rectangle(Point(450, 15), Point(750, 220))
    executeBox.setFill("Powder Blue")
    executeBox.setWidth(0)
    mainMessage = Text(Point(600, 195), "파일 이름을 입력하고 실행하세요")
    inputBox = Entry(Point(600, 165), 22)
    inputBox.setFill("Honeydew")
    inputBox.setSize(15)
    inputBox.setStyle("bold")
    inputBox.setTextColor("Gray")
    frequencyButton = Rectangle(Point(470, 90), Point(590, 135))
    frequencyButton.setFill("Medium Aquamarine")
    frequencyButton.setOutline("Medium Sea Green")
    frequencyButton.setWidth(3)
    frequencyText = Text(Point(530, 112.5), "빈도순")
    frequencyText.setFill("Dim Gray")
    randomButton = Rectangle(Point(470, 30), Point(590, 75))
    randomButton.setFill("Medium Aquamarine")
    randomButton.setOutline("Medium Sea Green")
    randomButton.setWidth(3)
    randomText = Text(Point(530, 52.5), "랜덤순")
    randomText.setFill("Dim Gray")
    ascendingButton = Rectangle(Point(610, 90), Point(730, 135))
    ascendingButton.setFill("Medium Aquamarine")
    ascendingButton.setOutline("Medium Sea Green")
    ascendingButton.setWidth(3)
    ascendingText = Text(Point(670, 112.5), "오름차순")
    ascendingText.setFill("Dim Gray")
    descendingButton = Rectangle(Point(610, 30), Point(730, 75))
    descendingButton.setFill("Medium Aquamarine")
    descendingButton.setOutline("Medium Sea Green")
    descendingButton.setWidth(3)
    descendingText = Text(Point(670, 52.5), "내림차순")
    descendingText.setFill("Dim Gray")

    # 그래픽 창 만들기
    win = GraphWin("단어 등장 횟수 그래프", 800, 400)
    win.setBackground("Wheat")

    try:
        while True:
            # 메인 화면 그리기
            win.setCoords(0, 0, 800, 400)
            mainMessage.setText("파일 이름을 입력하고 실행하세요")
            mainMessage.setFill("Black")
            inputBox.setText("ex: filename.txt")
            title.draw(win)
            helpButton.draw(win)
            helpText.draw(win)
            quitButton.draw(win)
            quitText.draw(win)
            executeBox.draw(win)
            mainMessage.draw(win)
            inputBox.draw(win)
            frequencyButton.draw(win)
            frequencyText.draw(win)
            randomButton.draw(win)
            randomText.draw(win)
            ascendingButton.draw(win)
            ascendingText.draw(win)
            descendingButton.draw(win)
            descendingText.draw(win)

            # 샘플 그래프 그리기
            wordEX = ["숙명", "IT공학과", "이종우", "파이썬", "사랑", "성공", "희망"]
            frequencyEX = [1, 8, 1, 2, 6, 8, 4]
            x_WordLabelEX = []
            barListEX = []
            valueListEX = []
            for x in range(7):
                x_WordLabelEX.append(Text(Point(70 + x * 50, 15), wordEX[x]))
                x_WordLabelEX[-1].setSize(7)
                x_WordLabelEX[-1].draw(win)
            for bar in range(7):
                barListEX.append(Rectangle(Point(55 + bar * 50, 25), Point(85 + bar * 50, 25 + frequencyEX[bar] * 30)))
                barListEX[-1].setFill("Light Salmon")
                barListEX[-1].setWidth(0)
                barListEX[-1].draw(win)
            for value in range(7):
                valueListEX.append(Text(Point(70 + value * 50, 30 + frequencyEX[value] * 30), frequencyEX[value]))
                valueListEX[-1].setFill("Firebrick")
                valueListEX[-1].setSize(8)
                valueListEX[-1].draw(win)

            while True:
                p = win.getMouse()
                try:
                    # HELP 버튼 클릭하면 도움말 실행
                    if 460 < p.getX() < 590 and 250 < p.getY() < 300:
                        helpButton.setFill("Gray")
                        time.sleep(0.1)
                        helpButton.setFill("Light Gray")
                        time.sleep(0.1)
                        # 도움말
                        helpWin = GraphWin("도움말", 400, 200)
                        helpWin.setBackground("white")
                        helpMessage = Text(Point(200, 100), ("< HELP >\n\n\n"
                                                             "▶ 빈도순 : 많이 등장하는 단어부터\n\n"
                                                             "▶ 랜덤순 : 무작위로 단어를 선택함\n\n"
                                                             "▶ 오름차순 : 단어를 오름차순 정렬\n\n"
                                                             "▶ 내림차순 : 단어를 내림차순 정렬"))
                        helpMessage.setSize(10)
                        helpMessage.setStyle("bold")
                        helpMessage.draw(helpWin)
                        helpWin.getMouse()
                        continue
                    else:
                        pass
                except GraphicsError:
                    continue

                # QUIT 버튼 클릭
                if 610 < p.getX() < 740 and 250 < p.getY() < 300:
                    quitButton.setFill("Gray")
                    time.sleep(0.1)
                    quitButton.setFill("Light Gray")
                    time.sleep(0.1)
                    break
                # 빈도순 버튼 클릭
                elif 470 < p.getX() < 590 and 95 < p.getY() < 140:
                    frequencyButton.setFill("Medium Sea Green")
                    time.sleep(0.1)
                    frequencyButton.setFill("Medium Aquamarine")
                    time.sleep(0.1)
                # 랜덤순 버튼 클릭
                elif 470 < p.getX() < 590 and 30 < p.getY() < 75:
                    randomButton.setFill("Medium Sea Green")
                    time.sleep(0.1)
                    randomButton.setFill("Medium Aquamarine")
                    time.sleep(0.1)
                # 오름차순 버튼 클릭
                elif 610 < p.getX() < 730 and 95 < p.getY() < 140:
                    ascendingButton.setFill("Medium Sea Green")
                    time.sleep(0.1)
                    ascendingButton.setFill("Medium Aquamarine")
                    time.sleep(0.1)
                # 내림차순 버튼 클릭
                elif 610 < p.getX() < 730 and 30 < p.getY() < 75:
                    descendingButton.setFill("Medium Sea Green")
                    time.sleep(0.1)
                    descendingButton.setFill("Medium Aquamarine")
                    time.sleep(0.1)
                else:
                    continue

                try:
                    specialChar = '''.,?!'"‘’/~-:;()[]<>'''  # 단어와 함께 쓰이는 특수문자

                    # 파일 이름 입력
                    filename = inputBox.getText()

                    # 파일 이름이 처음 값 그대로이면 "파일 이름을 입력하고 실행하세요"
                    if filename == "ex: filename.txt":
                        mainMessage.setText("")
                        mainMessage.setTextColor("Black")
                        time.sleep(0.1)
                        mainMessage.setText("파일 이름을 입력하고 실행하세요")
                        continue

                    # 파일 단어 읽기
                    file = open(filename, 'r')
                    data = file.read().lower().split()
                    file.close()

                    # 단어 양옆 특수문자 제거
                    words = []
                    for word in data:
                        delSpecialChar = [word]
                        for char in specialChar:
                            delSpecialChar[0] = delSpecialChar[0].strip(char)
                        if delSpecialChar[0] == "":
                            continue
                        else:
                            words.extend(delSpecialChar)

                    # 파일에 단어가 존재하지 않으면 "파일에 단어가 존재하지 않습니다"
                    if len(words) == 0:
                        mainMessage.setText("")
                        mainMessage.setFill("Tomato")
                        time.sleep(0.1)
                        mainMessage.setText("파일에 단어가 존재하지 않습니다")
                        continue

                # 파일이 존재하지 않으면 "파일을 찾을 수 없습니다"
                except FileNotFoundError:
                    mainMessage.setText("")
                    mainMessage.setFill("Tomato")
                    time.sleep(0.1)
                    mainMessage.setText("파일을 찾을 수 없습니다")
                    continue

                # 중복 단어 제거
                uniqueWords = set(words)
                
                # 단어 빈도를 센 다음 리스트에 넣기
                frequency = []
                for word in uniqueWords:
                    frequency.append(words.count(word))
                frequencyWords = list(zip(uniqueWords, frequency))

                # 빈도순으로 정렬하기
                if 470 < p.getX() < 590 and 95 < p.getY() < 140:
                    wordSorting = sorted(frequencyWords, key=lambda x: x[1], reverse=True)
                    print("빈도순", end=" # ")
                    break
                # 랜덤순으로 정렬하기
                if 470 < p.getX() < 590 and 30 < p.getY() < 75:
                    random.shuffle(frequencyWords)
                    wordSorting = frequencyWords
                    print("랜덤순", end=" # ")
                    break
                # 오름차순으로 정렬하기
                if 610 < p.getX() < 730 and 95 < p.getY() < 140:
                    wordSorting = sorted(frequencyWords, key=lambda x: x[0])
                    print("오름차순", end=" # ")
                    break
                # 내림차순으로 정렬하기
                if 610 < p.getX() < 730 and 30 < p.getY() < 75:
                    wordSorting = sorted(frequencyWords, key=lambda x: x[0], reverse=True)
                    print("내림차순", end=" # ")
                    break

            # 프로그램 종료
            if 610 < p.getX() < 740 and 250 < p.getY() < 300:
                win.close()
                print("프로그램이 종료되었습니다.")
                break

            # 인터페이스 지우기
            title.undraw()
            helpButton.undraw()
            helpText.undraw()
            quitButton.undraw()
            quitText.undraw()
            executeBox.undraw()
            mainMessage.undraw()
            inputBox.undraw()
            frequencyButton.undraw()
            frequencyText.undraw()
            randomButton.undraw()
            randomText.undraw()
            ascendingButton.undraw()
            ascendingText.undraw()
            descendingButton.undraw()
            descendingText.undraw()

            # 샘플 그래프 지우기
            for x in x_WordLabelEX:
                x.undraw()
            for bar in barListEX:
                bar.undraw()
            for value in valueListEX:
                value.undraw()

            frequencyList = []  # 그래프로 출력할 단어 빈도수 리스트

            # 단어가 10개 미만이면 모두 출력
            if len(wordSorting) < 10:
                for i in range(len(wordSorting)):
                    frequencyList.append(wordSorting[i][1])
            # 단어가 10개 이상이면 10개만 출력
            else:
                for i in range(10):
                    frequencyList.append(wordSorting[i][1])

            # 빈도수 최댓값을 올림해서 y축 최댓값 정하기
            max_y5 = (max(frequencyList) + 4) // 5 * 5  # ex) 44 → 45
            max_y10 = (max(frequencyList) + 9) // 10 * 10  # ex) 44 → 50

            # 빈도수 최댓값에 따라 그래픽 창 세로 좌표 바꾸기
            if max(frequencyList) <= 10:
                winHeight = 10 * 40
            elif max(frequencyList) <= 20:
                winHeight = 20 * 40
            elif max(frequencyList) <= 50:
                winHeight = max_y5 * 40
            else:
                winHeight = max_y10 * 40

            x_WordLabel = []  # x축(단어)
            y_FrequencyLabel = []  # y축(빈도)
            barList = []  # 막대그래프
            valueList = []  # 빈도수

            # 좌표 재설정
            win.setCoords(0, 0, 800, winHeight)

            # x축, y축 단위 표시
            x_axis = Text(Point(100 + (len(frequencyList) - 1) * 70 + 50, winHeight * 10 / 400), "(단어)")
            x_axis.setSize(7)
            y_axis = Text(Point(20, winHeight * 380 / 400), "(개수)")
            y_axis.setSize(7)
            x_axis.draw(win)
            y_axis.draw(win)

            # x축(단어) 표시
            for x in range(len(frequencyList)):
                if len(wordSorting[x][0]) <= 7:
                    x_WordLabel.append(Text(Point(100 + x * 70, winHeight * 10 / 400), wordSorting[x][0]))
                else:
                    x_WordLabel.append(Text(Point(100 + x * 70, winHeight * 10 / 400), wordSorting[x][0][0:5] + "…"))
                x_WordLabel[-1].setSize(7)
                x_WordLabel[-1].draw(win)

            # y축(빈도) 표시
            if max(frequencyList) <= 10:
                for y in range(0, 11):
                    y_FrequencyLabel.append(Text(Point(40, winHeight * 20 / 400 + y * 36), y))
                    y_FrequencyLabel[-1].setSize(8)
                    y_FrequencyLabel[-1].draw(win)
            elif max(frequencyList) <= 20:
                for y in range(0, 21, 2):
                    y_FrequencyLabel.append(Text(Point(40, winHeight * 20 / 400 + y * 36), y))
                    y_FrequencyLabel[-1].setSize(8)
                    y_FrequencyLabel[-1].draw(win)
            elif max(frequencyList) <= 50:
                for y in range(0, max_y5 + 1, 5):
                    y_FrequencyLabel.append(Text(Point(40, winHeight * 20 / 400 + y * 36), y))
                    y_FrequencyLabel[-1].setSize(8)
                    y_FrequencyLabel[-1].draw(win)
            else:
                for y in range(0, max_y10 + 1, 10):
                    y_FrequencyLabel.append(Text(Point(40, winHeight * 20 / 400 + y * 36), y))
                    y_FrequencyLabel[-1].setSize(8)
                    y_FrequencyLabel[-1].draw(win)

            # 막대그래프 그리기
            for bar in range(len(frequencyList)):
                if wordSorting[bar][1] == 0:
                    continue
                else:
                    barList.append(Rectangle(Point(85 + bar * 70, winHeight * 20 / 400),
                                             Point(115 + bar * 70, winHeight * 20 / 400 + wordSorting[bar][1] * 36)))
                    barList[-1].setFill("Light Salmon")
                    barList[-1].setWidth(0)
                    barList[-1].draw(win)

            # 빈도수 표시
            for value in range(0, len(x_WordLabel)):
                valueList.append(
                    Text(Point(100 + value * 70, winHeight * 25 / 400 + wordSorting[value][1] * 36),
                         wordSorting[value][1]))
                valueList[-1].setFill("Firebrick")
                valueList[-1].setSize(8)
                valueList[-1].draw(win)

            # 파일 이름과 단어별 빈도수 출력
            print("<%s>  전체단어수: %s개 / " % (filename, len(words)), end="")
            for (word, frequency) in wordSorting:
                if word == wordSorting[len(frequencyList) - 1][0]:
                    print("%s: %s개" % (word, frequency), end="\n")
                    break
                else:
                    print("%s: %s개" % (word, frequency), end=" / ")
            print("-" * 200)

            while True:
                # 히스토그램 지우기
                if win.checkMouse():
                    for x in range(len(x_WordLabel)):
                        x_WordLabel[0].undraw()
                        del x_WordLabel[0]
                    for y in range(0, len(y_FrequencyLabel)):
                        y_FrequencyLabel[0].undraw()
                        del y_FrequencyLabel[0]
                    for bar in barList:
                        bar.undraw()
                    for value in range(0, len(valueList)):
                        valueList[0].undraw()
                        del valueList[0]
                    x_axis.undraw()
                    y_axis.undraw()
                    break
                else:
                    continue

            continue

    # X 버튼을 클릭하면 프로그램 종료
    except GraphicsError:
        print("프로그램이 종료되었습니다.")


main()
