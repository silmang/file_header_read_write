filename = '3b5b21c00bc6a5.jpg'
blocksize = 256

# file header read
with open(filename, 'rb') as f: # block_utf = block.decode('utf-8', 'ignore')
    block = f.read(blocksize)
    count = 0
    result = ""
    for ch in block:
        count+=1
        if(count%16!=0):
            result += hex(ch)+" "
        else:
            result += hex(ch)+"\n"
    print(result)
    print("\nblock")
    print(type(block))
    print(block)
    print("\ntext")
    string_block = str(block).replace("\\x","\t").split('\t')
    string_block_temp = [i for i in string_block if len(i)>=3]
    for j in string_block_temp:
        print(j[2:].strip(), sep="\n")

# file header write
with open(filename, 'r+b') as f:
    newbytes = b'\xff'
    f.seek(0)
    f.write(newbytes)