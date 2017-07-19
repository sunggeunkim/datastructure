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
       
def longestPath(fsystem):
    stack = [0] * 100
    ans = 0
    for line in fsystem.split('\r'):
        depth = 0
        while depth < len(line) and line[depth] == '\t':
            depth += 1
        name = line[depth:]
        stack[depth] = len(name)
        if '.' in name:
            ans = max(ans, sum(stack[:depth]) + depth + len(name) )
    return ans
