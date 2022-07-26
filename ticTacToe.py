

theBoard = {'top-L': " ", 'top-M': " ", 'top-R': " ",
            'mid-L': " ", 'mid-M': " ", 'mid-R': " ",
            'low-L': " ", 'low-M': " ", 'low-R': " "}

def prinBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid=L'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-L'])