class Node:
    def __init__(self, val):
        self.children = []
        self.val = val

    def insert(self, s):
        if len(s) > 0:
            toAdd = s[0]
            found = False
            index = 0
            for i in range(len(self.children)):
                if self.children[i].val == toAdd:
                    index = i
                    found = True
            if found:
                nodeToAdd = self.children[index]
            else:
                self.children.append(Node(toAdd))
                nodeToAdd = self.children[-1]
            nodeToAdd.insert(s[1:])

    def search(self, queryString):
        consideredNode = self
        wordList = []
        for j in range(len(queryString)):
            found = False
            index = 0
            for i in range(len(consideredNode.children)):
                if consideredNode.children[i].val == queryString[j]:
                    index = i
                    found = True
            if found:
                consideredNode = consideredNode.children[index]
            else:
                return []
        nodeStack = consideredNode.children
        if len(nodeStack) == 0:
            return [queryString]
        wordStack = []
        for i in range(len(nodeStack)):
            wordStack.append(nodeStack[i].val)
        while len(nodeStack) > 0:
            consideringNode = nodeStack.pop()
            consideringWord = wordStack.pop()
            if len(consideringNode.children) == 0:
                wordList.append(queryString+consideringWord)
            else:
                for child in consideringNode.children:
                    nodeStack.append(child)
                    wordStack.append(consideringWord+child.val)
        return wordList

def bruteSearch(q,dictionary):
    wordList = []
    for word in dictionary:
        if word.startswith(q):
            wordList.append(word)
    return wordList

from timeit import default_timer as timer
if __name__ == '__main__':
    # Preparing Data for searching
    dictionary = []
    f = open("wordlist.txt",'r')
    f1 = f.readlines()
    for word in f1:
        dictionary.append(str(word).rstrip('\n'))
    root = Node('')
    for word in dictionary:
        root.insert(word)
    print("Loaded dictionary.")
    q = str(input("Enter Query String:"))
    # Trie Search
    start = timer()
    trieResult = root.search(q)
    end = timer()
    print("Time taken by trie:"+str(end-start)+" seconds.")
    # Brute Search
    start = timer()
    bruteSearchResult = bruteSearch(q,dictionary)
    end = timer()
    print("Time taken by brute force search:"+str(end-start)+" seconds.")
    print("Suggestions:"+str(trieResult))