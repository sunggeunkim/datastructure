"""
reference: https://codefights.com/interview-practice/task/iXJRYae6TBqc4ymFg/description
Suppose we represent our file system as a string. For example, the string "user\n\tpictures\n\tdocuments\n\t\tnotes.txt" represents:

user
    pictures
    documents
        notes.txt    
The directory user contains an empty sub-directory pictures and a sub-directory documents containing a file notes.txt.

The string "user\n\tpictures\n\t\tphoto.png\n\t\tcamera\n\tdocuments\n\t\tlectures\n\t\t\tnotes.txt" represents:

user
    pictures
        photo.png
        camera
    documents
        lectures
            notes.txt
The directory user contains two sub-directories pictures and documents. pictures contains a file photo.png and an empty second-level sub-directory camera. documents contains a second-level sub-directory lectures containing a file notes.txt.

We want to find the longest (as determined by the number of characters) absolute path to a file within our system. For example, in the second example above, the longest absolute path is "user/documents/lectures/notes.txt", and its length is 33 (not including the double quotes).

Given a string representing the file system in this format, return the length of the longest absolute path to a file in the abstracted file system. If there is not a file in the file system, return 0.

Example

For fileSystem = "user\n\tpictures\n\tdocuments\n\t\tnotes.txt", the output should be

longestPath(fileSystem) = 24.

The longest path is "user/documents/notes.txt", and it consists of 24 characters.

"""

class Node:
    def __init__(self, value, level = 0, children = None, text_length = None):
        self.value = value
        self.children = children
        self.level = level
        self.text_length = text_length
        
def longestPath(fileSystem):
    fileSystem = fileSystem.split('\r')
    root = Node(fileSystem[0], 0, None, len(fileSystem[0]))
    stack = [root]
    i = 1
    max_length = 0
    if "." in fileSystem[0]:
        max_length = len(fileSystem[0])
    while len(stack) > 0 and i < len(fileSystem):
        name = fileSystem[i]
        curr = stack[-1]
        curr_level = curr.level
        index = name.rfind('\t')
        next_level = index + 1
        if next_level <= curr_level:
            stack.pop()
            if len(stack) == 0 and next_level == 0:
                if "." in name:
                    max_length = max(max_length, len(name[index+1:]))
                if i + 1 < len(fileSystem):
                    root = Node(name,  0, None, len(name[index+1:]))
                    stack.append(root)
                    i += 1
                else:
                    return max_length
        else:
            next_node = Node(name[index+1:],\
                             next_level, None,\
                             curr.text_length + 1 + len(name[index+1:]))
            if "." in name and next_node.text_length > max_length:
                max_length = next_node.text_length
            if curr.children == None:
                curr.children = [next_node]
            else:
                curr.children.append(next_node)
            stack.append(next_node)
            i += 1
    return max_length
