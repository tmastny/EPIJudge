from test_framework import generic_test


def shortest_equivalent_path1(path: str) -> str:
    directories = []
    name = ''
    for s in path:
        if s == "/":
            if name != "":
                directories.append(name)
                name = ''
        else:
            name += s

    if name != "":
        directories.append(name)

    stack = []
    if path[0] == "/":
        stack.append("/")
        
    for dir in directories:
        if dir == ".":
            continue
        elif dir == ".." and stack:
            if stack[-1] == "/":
                continue
            elif stack[-1] == ".":
                stack[-1] = ".."
            elif stack[-1] == "..":
                stack.append(dir)
            else:
                stack.pop()
        else:
           stack.append(dir)
    
    normalized = "/".join(stack)
    if path[0] == "/" and len(normalized) > 1:
        return normalized[1:] 
    
    return normalized 

def shortest_equivalent_path(path: str) -> str:
    tokens = [token for token in path.split("/") if token not in [".", ""]]
    
    stack = []
    if path[0] == "/":
        stack.append("/")
    
    for token in tokens:
        if token == "..":
            if stack and stack[-1] != "..":
                stack.pop()
            else:
                stack.append(token)
        else:
            stack.append(token)
    
    normalized = "/".join(stack)
    if normalized.startswith("//"):
        return normalized[1:]
        
    return normalized



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
