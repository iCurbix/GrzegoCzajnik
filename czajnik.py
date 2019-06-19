
a = input("write a filename to convert (ommit writing an extension, just a name)\n")
f = open(a + '.obj' , 'r')
fo = open(a + '.h' , 'w')
pop = ''
rzeczy = {'v': [] , 'vn': [] , 'f': [] , 'vt': []}
ile = 0

fo.write('#ifndef ' + a + '_H\n')
fo.write('#define ' + a + '_H\n\n')
for l in f:
    li = l.split()

    if li[0] not in rzeczy:
        continue

    rzeczy[li[0]].append(li[1:])




fo.write(f'float {a}Vertices[]={{\n')
for t in rzeczy['f']:
    for p in t:
        fo.write('\t')
        for xyz in rzeczy['v'][int(p.split('/')[0]) - 1]:
            fo.write(f'{xyz}f, ')
        fo.write('1.0f,\n')
        ile += 1
    fo.write('\n')
fo.write('};\n\n')

fo.write(f'unsigned int {a}VertexCount={ile};\n\n')

fo.write(f'float {a}Normals[]={{\n')
for t in rzeczy['f']:
    for p in t:
        fo.write('\t')
        for xyz in rzeczy['vn'][int(p.split('/')[2]) - 1]:
            fo.write(f'{xyz}f, ')
        fo.write('0.0f,\n')
    fo.write('\n')
fo.write('};\n\n')

fo.write(f'float {a}TexCoords[]={{\n')
for t in rzeczy['f']:
    for p in t:
        fo.write('\t')
        for xyz in rzeczy['vt'][int(p.split('/')[1]) - 1]:
            fo.write(f'{xyz}f, ')
        fo.write('\n')
    fo.write('\n')
fo.write('};\n')


fo.write('#endif')











