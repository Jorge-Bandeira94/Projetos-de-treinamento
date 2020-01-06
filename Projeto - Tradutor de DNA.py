# Created by Jorge

from time import sleep
print(50*'-=-')
seq = input('Insira sua sequência de nucleotídeos em formato FASTA: ').strip()
print(50*'-=-')
print('Processando...\n\n')
sleep(2)
print('_ : Stop códon\nM : Start códon\n')
seq = ''.join(seq)
seq = seq.lower()
import csv
with open('tradução.xls', 'w') as tradução:
    lista = []
    seq1 = ''
    for i in seq:
        seq1 = seq1 + i
        if len(seq1) == 3:
            lista.append(seq1)
            seq1 = ''
            if 'ata' in lista:
                lista.remove('ata')
                lista.append('I')
                seq1 = ''
            if 'aaa' in lista:
                lista.remove('aaa')
                lista.append('K')
                seq1 = ''
            if 'atc' in lista:
                lista.remove('atc')
                lista.append('I')
                seq1 = ''
            if 'att' in lista:
                lista.remove('att')
                lista.append('I')
                seq1 = ''
            if 'aat' in lista:
                lista.remove('aat')
                lista.append('N')
                seq1 = ''
            if 'atg' in lista:
                lista.remove('atg')
                lista.append('M')
                seq1 = ''
            if 'aca' in lista:
                lista.remove('aca')
                lista.append('T')
                seq1 = ''
            if 'acc' in lista:
                lista.remove('acc')
                lista.append('T')
                seq1 = ''
            if 'aac' in lista:
                lista.remove('aac')
                lista.append('N')
            if 'acg' in lista:
                lista.remove('acg')
                lista.append('T')
                seq1 = ''
            if 'act' in lista:
                lista.remove('act')
                lista.append('T')
                seq1 = ''
            if 'acc' in lista:
                lista.remove('acc')
                lista.append('N')
                seq1 = ''
            if 'aag' in lista:
                lista.remove('aag')
                lista.append('K')
                seq1 = ''
            if 'agc' in lista:
                lista.remove('agc')
                lista.append('S')
                seq1 = ''
            if 'agt' in lista:
                lista.remove('agt')
                lista.append('S')
                seq1 = ''
            if 'aga' in lista:
                lista.remove('aga')
                lista.append('R')
                seq1 = ''
            if 'agg' in lista:
                lista.remove('agg')
                lista.append('R')
                seq1 = ''
            if 'cta' in lista:
                lista.remove('cta')
                lista.append('L')
                seq1 = ''
            if 'ctc' in lista:
                lista.remove('ctc')
                lista.append('L')
                seq1 = ''
            if 'ctg' in lista:
                lista.remove('ctg')
                lista.append('L')
                seq1 = ''
            if 'ctt' in lista:
                lista.remove('ctt')
                lista.append('L')
                seq1 = ''
            if 'cca' in lista:
                lista.remove('cca')
                lista.append('P')
                seq1 = ''
            if 'ccc' in lista:
                lista.remove('ccc')
                lista.append('P')
                seq1 = ''
            if 'ccg' in lista:
                lista.remove('ccg')
                lista.append('P')
                seq1 = ''
            if 'cct' in lista:
                lista.remove('cct')
                lista.append('P')
                seq1 = ''
            if 'cac' in lista:
                lista.remove('cac')
                lista.append('H')
                seq1 = ''
            if 'cat' in lista:
                lista.remove('cat')
                lista.append('H')
                seq1 = ''
            if 'caa' in lista:
                lista.remove('caa')
                lista.append('Q')
                seq1 = ''
            if 'cag' in lista:
                lista.remove('cag')
                lista.append('Q')
                seq1 = ''
            if 'cga' in lista:
                lista.remove('cga')
                lista.append('R')
                seq1 = ''
            if 'cgc' in lista:
                lista.remove('cgc')
                lista.append('R')
                seq1 = ''
            if 'cgg' in lista:
                lista.remove('cgg')
                lista.append('R')
                seq1 = ''
            if 'cgt' in lista:
                lista.remove('cgt')
                lista.append('R')
                seq1 = ''
            if 'gta' in lista:
                lista.remove('gta')
                lista.append('V')
                seq1 = ''
            if 'gtc' in lista:
                lista.remove('gtc')
                lista.append('V')
                seq1 = ''
            if 'gtg' in lista:
                lista.remove('gtg')
                lista.append('V')
                seq1 = ''
            if 'gtt' in lista:
                lista.remove('gtt')
                lista.append('V')
                seq1 = ''
            if 'gca' in lista:
                lista.remove('gca')
                lista.append('A')
                seq1 = ''
            if 'gcc' in lista:
                lista.remove('gcc')
                lista.append('A')
                seq1 = ''
            if 'gcg' in lista:
                lista.remove('gcg')
                lista.append('A')
                seq1 = ''
            if 'gct' in lista:
                lista.remove('gct')
                lista.append('A')
                seq1 = ''
            if 'gac' in lista:
                lista.remove('gac')
                lista.append('D')
                seq1 = ''
            if 'gat' in lista:
                lista.remove('gat')
                lista.append('D')
                seq1 = ''
            if 'gag' in lista:
                lista.remove('gag')
                lista.append('E')
                seq1 = ''
            if 'gga' in lista:
                lista.remove('gga')
                lista.append('G')
                seq1 = ''
            if 'gaa' in lista:
                lista.remove('gaa')
                lista.append('E')
                seq1 = ''
            if 'ggc' in lista:
                lista.remove('ggc')
                lista.append('G')
                seq1 = ''
            if 'ggg' in lista:
                lista.remove('ggg')
                lista.append('G')
                seq1 = ''
            if 'ggt' in lista:
                lista.remove('ggt')
                lista.append('G')
                seq1 = ''
            if 'tca' in lista:
                lista.remove('tca')
                lista.append('S')
                seq1 = ''
            if 'ttc' in lista:
                lista.remove('ttc')
                lista.append('F')
                seq1 = ''
            if 'tcg' in lista:
                lista.remove('tcg')
                lista.append('S')
                seq1 = ''
            if 'tct' in lista:
                lista.remove('tct')
                lista.append('S')
                seq1 = ''
            if 'ttc' in lista:
                lista.remove('ttc')
                lista.append('F')
                seq1 = ''
            if 'ttt' in lista:
                lista.remove('ttt')
                lista.append('F')
                seq1 = ''
            if 'tta' in lista:
                lista.remove('tta')
                lista.append('L')
                seq1 = ''
            if 'ttg' in lista:
                lista.remove('ttg')
                lista.append('L')
                seq1 = ''
            if 'tac' in lista:
                lista.remove('tac')
                lista.append('Y')
                seq1 = ''
            if 'tat' in lista:
                lista.remove('tat')
                lista.append('Y')
                seq1 = ''
            if 'taa' in lista:
                lista.remove('taa')
                lista.append(('_'))
                seq1 = ''
            if 'tag' in lista:
                lista.remove('tag')
                lista.append(('_'))
                seq1 = ''
            if 'tgc' in lista:
                lista.remove('tgc')
                lista.append('C')
                seq1 = ''
            if 'tgt' in lista:
                lista.remove('tgt')
                lista.append('C')
                seq1 = ''
            if 'tga' in lista:
                lista.remove('tga')
                lista.append(('_'))
                seq1 = ''
            if 'tgg' in lista:
                lista.remove('tgg')
                lista.append('W')
                seq1 = ''
            if 'tcc' in lista:
                lista.remove('tcc')
                lista.append('S')
                seq1 = ''
            else:
                seq1 = ''
    a = ''.join(lista)
    a1 = a.find('M')
    a2 = a.find('K''K''K''K''K''K')
    print('Sua sequência traduzida em quadro de leitura +1 é:\n', a)
    print('A sequência a partir do start códon é:\n', a[a1:a2])
    print(50 * '-=-', '\n\n')
    tradução.write('Sequência integral +1:\t')
    for aa in a:
        tradução.write(aa)
    tradução.write('\nSequência tratada +1:\t')
    for aa in a[a1:a2]:
        tradução.write(aa)


    def tradutor2():
        lista = []
        seq1 = ''
        for i in seq[1:]:
            seq1 = seq1 + i
            if len(seq1) == 3:
                lista.append(seq1)
                seq1 = ''
                if 'ata' in lista:
                    lista.remove('ata')
                    lista.append('I')
                    seq1 = ''
                if 'aaa' in lista:
                    lista.remove('aaa')
                    lista.append('K')
                    seq1 = ''
                if 'atc' in lista:
                    lista.remove('atc')
                    lista.append('I')
                    seq1 = ''
                if 'att' in lista:
                    lista.remove('att')
                    lista.append('I')
                    seq1 = ''
                if 'aat' in lista:
                    lista.remove('aat')
                    lista.append('N')
                    seq1 = ''
                if 'atg' in lista:
                    lista.remove('atg')
                    lista.append('M')
                    seq1 = ''
                if 'aca' in lista:
                    lista.remove('aca')
                    lista.append('T')
                    seq1 = ''
                if 'acc' in lista:
                    lista.remove('acc')
                    lista.append('T')
                    seq1 = ''
                if 'aac' in lista:
                    lista.remove('aac')
                    lista.append('N')
                if 'acg' in lista:
                    lista.remove('acg')
                    lista.append('T')
                    seq1 = ''
                if 'act' in lista:
                    lista.remove('act')
                    lista.append('T')
                    seq1 = ''
                if 'acc' in lista:
                    lista.remove('acc')
                    lista.append('N')
                    seq1 = ''
                if 'aag' in lista:
                    lista.remove('aag')
                    lista.append('K')
                    seq1 = ''
                if 'agc' in lista:
                    lista.remove('agc')
                    lista.append('S')
                    seq1 = ''
                if 'agt' in lista:
                    lista.remove('agt')
                    lista.append('S')
                    seq1 = ''
                if 'aga' in lista:
                    lista.remove('aga')
                    lista.append('R')
                    seq1 = ''
                if 'agg' in lista:
                    lista.remove('agg')
                    lista.append('R')
                    seq1 = ''
                if 'cta' in lista:
                    lista.remove('cta')
                    lista.append('L')
                    seq1 = ''
                if 'ctc' in lista:
                    lista.remove('ctc')
                    lista.append('L')
                    seq1 = ''
                if 'ctg' in lista:
                    lista.remove('ctg')
                    lista.append('L')
                    seq1 = ''
                if 'ctt' in lista:
                    lista.remove('ctt')
                    lista.append('L')
                    seq1 = ''
                if 'cca' in lista:
                    lista.remove('cca')
                    lista.append('P')
                    seq1 = ''
                if 'ccc' in lista:
                    lista.remove('ccc')
                    lista.append('P')
                    seq1 = ''
                if 'ccg' in lista:
                    lista.remove('ccg')
                    lista.append('P')
                    seq1 = ''
                if 'cct' in lista:
                    lista.remove('cct')
                    lista.append('P')
                    seq1 = ''
                if 'cac' in lista:
                    lista.remove('cac')
                    lista.append('H')
                    seq1 = ''
                if 'cat' in lista:
                    lista.remove('cat')
                    lista.append('H')
                    seq1 = ''
                if 'caa' in lista:
                    lista.remove('caa')
                    lista.append('Q')
                    seq1 = ''
                if 'cag' in lista:
                    lista.remove('cag')
                    lista.append('Q')
                    seq1 = ''
                if 'cga' in lista:
                    lista.remove('cga')
                    lista.append('R')
                    seq1 = ''
                if 'cgc' in lista:
                    lista.remove('cgc')
                    lista.append('R')
                    seq1 = ''
                if 'cgg' in lista:
                    lista.remove('cgg')
                    lista.append('R')
                    seq1 = ''
                if 'cgt' in lista:
                    lista.remove('cgt')
                    lista.append('R')
                    seq1 = ''
                if 'gta' in lista:
                    lista.remove('gta')
                    lista.append('V')
                    seq1 = ''
                if 'gtc' in lista:
                    lista.remove('gtc')
                    lista.append('V')
                    seq1 = ''
                if 'gtg' in lista:
                    lista.remove('gtg')
                    lista.append('V')
                    seq1 = ''
                if 'gtt' in lista:
                    lista.remove('gtt')
                    lista.append('V')
                    seq1 = ''
                if 'gca' in lista:
                    lista.remove('gca')
                    lista.append('A')
                    seq1 = ''
                if 'gcc' in lista:
                    lista.remove('gcc')
                    lista.append('A')
                    seq1 = ''
                if 'gcg' in lista:
                    lista.remove('gcg')
                    lista.append('A')
                    seq1 = ''
                if 'gct' in lista:
                    lista.remove('gct')
                    lista.append('A')
                    seq1 = ''
                if 'gac' in lista:
                    lista.remove('gac')
                    lista.append('D')
                    seq1 = ''
                if 'gat' in lista:
                    lista.remove('gat')
                    lista.append('D')
                    seq1 = ''
                if 'gag' in lista:
                    lista.remove('gag')
                    lista.append('E')
                    seq1 = ''
                if 'gga' in lista:
                    lista.remove('gga')
                    lista.append('G')
                    seq1 = ''
                if 'gaa' in lista:
                    lista.remove('gaa')
                    lista.append('E')
                    seq1 = ''
                if 'ggc' in lista:
                    lista.remove('ggc')
                    lista.append('G')
                    seq1 = ''
                if 'ggg' in lista:
                    lista.remove('ggg')
                    lista.append('G')
                    seq1 = ''
                if 'ggt' in lista:
                    lista.remove('ggt')
                    lista.append('G')
                    seq1 = ''
                if 'tca' in lista:
                    lista.remove('tca')
                    lista.append('S')
                    seq1 = ''
                if 'ttc' in lista:
                    lista.remove('ttc')
                    lista.append('F')
                    seq1 = ''
                if 'tcg' in lista:
                    lista.remove('tcg')
                    lista.append('S')
                    seq1 = ''
                if 'tct' in lista:
                    lista.remove('tct')
                    lista.append('S')
                    seq1 = ''
                if 'ttc' in lista:
                    lista.remove('ttc')
                    lista.append('F')
                    seq1 = ''
                if 'ttt' in lista:
                    lista.remove('ttt')
                    lista.append('F')
                    seq1 = ''
                if 'tta' in lista:
                    lista.remove('tta')
                    lista.append('L')
                    seq1 = ''
                if 'ttg' in lista:
                    lista.remove('ttg')
                    lista.append('L')
                    seq1 = ''
                if 'tac' in lista:
                    lista.remove('tac')
                    lista.append('Y')
                    seq1 = ''
                if 'tat' in lista:
                    lista.remove('tat')
                    lista.append('Y')
                    seq1 = ''
                if 'taa' in lista:
                    lista.remove('taa')
                    lista.append(('_'))
                    seq1 = ''
                if 'tag' in lista:
                    lista.remove('tag')
                    lista.append(('_'))
                    seq1 = ''
                if 'tgc' in lista:
                    lista.remove('tgc')
                    lista.append('C')
                    seq1 = ''
                if 'tgt' in lista:
                    lista.remove('tgt')
                    lista.append('C')
                    seq1 = ''
                if 'tga' in lista:
                    lista.remove('tga')
                    lista.append(('_'))
                    seq1 = ''
                if 'tgg' in lista:
                    lista.remove('tgg')
                    lista.append('W')
                    seq1 = ''
                if 'tcc' in lista:
                    lista.remove('tcc')
                    lista.append('S')
                    seq1 = ''
                else:
                    seq1 = ''
        a = ''.join(lista)
        a1 = a.find('M')
        a2 = a.find('K''K''K''K''K''K')
        print('Sua sequência traduzida em quadro de leitura +2 é:\n', a)
        print('A sequência a partir do start códon é:\n', a[a1:a2])
        print(50 * '-=-', '\n\n')
        tradução.write('\n\nSequência integral +2:\t')
        for aa in a:
            tradução.write(aa)
        tradução.write('\nSequência tratada +2:\t')
        for aa in a[a1:a2]:
            tradução.write(aa)
    tradutor2()
    def tradutor3():
        lista = []
        seq1 = ''
        for i in seq[2:]:
            seq1 = seq1 + i
            if len(seq1) == 3:
                lista.append(seq1)
                seq1 = ''
                if 'ata' in lista:
                    lista.remove('ata')
                    lista.append('I')
                    seq1 = ''
                if 'aaa' in lista:
                    lista.remove('aaa')
                    lista.append('K')
                    seq1 = ''
                if 'atc' in lista:
                    lista.remove('atc')
                    lista.append('I')
                    seq1 = ''
                if 'att' in lista:
                    lista.remove('att')
                    lista.append('I')
                    seq1 = ''
                if 'aat' in lista:
                    lista.remove('aat')
                    lista.append('N')
                    seq1 = ''
                if 'atg' in lista:
                    lista.remove('atg')
                    lista.append('M')
                    seq1 = ''
                if 'aca' in lista:
                    lista.remove('aca')
                    lista.append('T')
                    seq1 = ''
                if 'acc' in lista:
                    lista.remove('acc')
                    lista.append('T')
                    seq1 = ''
                if 'aac' in lista:
                    lista.remove('aac')
                    lista.append('N')
                if 'acg' in lista:
                    lista.remove('acg')
                    lista.append('T')
                    seq1 = ''
                if 'act' in lista:
                    lista.remove('act')
                    lista.append('T')
                    seq1 = ''
                if 'acc' in lista:
                    lista.remove('acc')
                    lista.append('N')
                    seq1 = ''
                if 'aag' in lista:
                    lista.remove('aag')
                    lista.append('K')
                    seq1 = ''
                if 'agc' in lista:
                    lista.remove('agc')
                    lista.append('S')
                    seq1 = ''
                if 'agt' in lista:
                    lista.remove('agt')
                    lista.append('S')
                    seq1 = ''
                if 'aga' in lista:
                    lista.remove('aga')
                    lista.append('R')
                    seq1 = ''
                if 'agg' in lista:
                    lista.remove('agg')
                    lista.append('R')
                    seq1 = ''
                if 'cta' in lista:
                    lista.remove('cta')
                    lista.append('L')
                    seq1 = ''
                if 'ctc' in lista:
                    lista.remove('ctc')
                    lista.append('L')
                    seq1 = ''
                if 'ctg' in lista:
                    lista.remove('ctg')
                    lista.append('L')
                    seq1 = ''
                if 'ctt' in lista:
                    lista.remove('ctt')
                    lista.append('L')
                    seq1 = ''
                if 'cca' in lista:
                    lista.remove('cca')
                    lista.append('P')
                    seq1 = ''
                if 'ccc' in lista:
                    lista.remove('ccc')
                    lista.append('P')
                    seq1 = ''
                if 'ccg' in lista:
                    lista.remove('ccg')
                    lista.append('P')
                    seq1 = ''
                if 'cct' in lista:
                    lista.remove('cct')
                    lista.append('P')
                    seq1 = ''
                if 'cac' in lista:
                    lista.remove('cac')
                    lista.append('H')
                    seq1 = ''
                if 'cat' in lista:
                    lista.remove('cat')
                    lista.append('H')
                    seq1 = ''
                if 'caa' in lista:
                    lista.remove('caa')
                    lista.append('Q')
                    seq1 = ''
                if 'cag' in lista:
                    lista.remove('cag')
                    lista.append('Q')
                    seq1 = ''
                if 'cga' in lista:
                    lista.remove('cga')
                    lista.append('R')
                    seq1 = ''
                if 'cgc' in lista:
                    lista.remove('cgc')
                    lista.append('R')
                    seq1 = ''
                if 'cgg' in lista:
                    lista.remove('cgg')
                    lista.append('R')
                    seq1 = ''
                if 'cgt' in lista:
                    lista.remove('cgt')
                    lista.append('R')
                    seq1 = ''
                if 'gta' in lista:
                    lista.remove('gta')
                    lista.append('V')
                    seq1 = ''
                if 'gtc' in lista:
                    lista.remove('gtc')
                    lista.append('V')
                    seq1 = ''
                if 'gtg' in lista:
                    lista.remove('gtg')
                    lista.append('V')
                    seq1 = ''
                if 'gtt' in lista:
                    lista.remove('gtt')
                    lista.append('V')
                    seq1 = ''
                if 'gca' in lista:
                    lista.remove('gca')
                    lista.append('A')
                    seq1 = ''
                if 'gcc' in lista:
                    lista.remove('gcc')
                    lista.append('A')
                    seq1 = ''
                if 'gcg' in lista:
                    lista.remove('gcg')
                    lista.append('A')
                    seq1 = ''
                if 'gct' in lista:
                    lista.remove('gct')
                    lista.append('A')
                    seq1 = ''
                if 'gac' in lista:
                    lista.remove('gac')
                    lista.append('D')
                    seq1 = ''
                if 'gat' in lista:
                    lista.remove('gat')
                    lista.append('D')
                    seq1 = ''
                if 'gag' in lista:
                    lista.remove('gag')
                    lista.append('E')
                    seq1 = ''
                if 'gga' in lista:
                    lista.remove('gga')
                    lista.append('G')
                    seq1 = ''
                if 'gaa' in lista:
                    lista.remove('gaa')
                    lista.append('E')
                    seq1 = ''
                if 'ggc' in lista:
                    lista.remove('ggc')
                    lista.append('G')
                    seq1 = ''
                if 'ggg' in lista:
                    lista.remove('ggg')
                    lista.append('G')
                    seq1 = ''
                if 'ggt' in lista:
                    lista.remove('ggt')
                    lista.append('G')
                    seq1 = ''
                if 'tca' in lista:
                    lista.remove('tca')
                    lista.append('S')
                    seq1 = ''
                if 'ttc' in lista:
                    lista.remove('ttc')
                    lista.append('F')
                    seq1 = ''
                if 'tcg' in lista:
                    lista.remove('tcg')
                    lista.append('S')
                    seq1 = ''
                if 'tct' in lista:
                    lista.remove('tct')
                    lista.append('S')
                    seq1 = ''
                if 'ttc' in lista:
                    lista.remove('ttc')
                    lista.append('F')
                    seq1 = ''
                if 'ttt' in lista:
                    lista.remove('ttt')
                    lista.append('F')
                    seq1 = ''
                if 'tta' in lista:
                    lista.remove('tta')
                    lista.append('L')
                    seq1 = ''
                if 'ttg' in lista:
                    lista.remove('ttg')
                    lista.append('L')
                    seq1 = ''
                if 'tac' in lista:
                    lista.remove('tac')
                    lista.append('Y')
                    seq1 = ''
                if 'tat' in lista:
                    lista.remove('tat')
                    lista.append('Y')
                    seq1 = ''
                if 'taa' in lista:
                    lista.remove('taa')
                    lista.append(('_'))
                    seq1 = ''
                if 'tag' in lista:
                    lista.remove('tag')
                    lista.append(('_'))
                    seq1 = ''
                if 'tgc' in lista:
                    lista.remove('tgc')
                    lista.append('C')
                    seq1 = ''
                if 'tgt' in lista:
                    lista.remove('tgt')
                    lista.append('C')
                    seq1 = ''
                if 'tga' in lista:
                    lista.remove('tga')
                    lista.append(('_'))
                    seq1 = ''
                if 'tgg' in lista:
                    lista.remove('tgg')
                    lista.append('W')
                    seq1 = ''
                if 'tcc' in lista:
                    lista.remove('tcc')
                    lista.append('S')
                    seq1 = ''
                else:
                    seq1 = ''
        a = ''.join(lista)
        a1 = a.find('M')
        a2 = a.find('K''K''K''K''K''K')
        print('Sua sequência traduzida em quadro de leitura +3 é:\n', a)
        print('A sequência a partir do start códon é:\n', a[a1:a2])
        print(50 * '-=-', '\n\n')
        tradução.write('\n\nSequência integral +3:\t')
        for aa in a:
            tradução.write(aa)
        tradução.write('\nSequência tratada +3:\t')
        for aa in a[a1:a2]:
            tradução.write(aa)
    tradutor3()
    def tradutor_1():
        lista3 = []
        seq4 = ''
        d2 = len(seq)
        for i in seq[d2::-1]:
            seq4 = seq4 + i
            if len(seq4) == 3:
                lista3.append(seq4)
                seq4 = ''
                if 'ata' in lista3:
                    lista3.remove('ata')
                    lista3.append('I')
                    seq4 = ''
                if 'aaa' in lista3:
                    lista3.remove('aaa')
                    lista3.append('K')
                    seq4 = ''
                if 'atc' in lista3:
                    lista3.remove('atc')
                    lista3.append('I')
                    seq4 = ''
                if 'att' in lista3:
                    lista3.remove('att')
                    lista3.append('I')
                    seq4 = ''
                if 'aat' in lista3:
                    lista3.remove('aat')
                    lista3.append('N')
                    seq4 = ''
                if 'atg' in lista3:
                    lista3.remove('atg')
                    lista3.append('M')
                    seq4 = ''
                if 'aca' in lista3:
                    lista3.remove('aca')
                    lista3.append('T')
                    seq4 = ''
                if 'acc' in lista3:
                    lista3.remove('acc')
                    lista3.append('T')
                    seq4 = ''
                if 'acg' in lista3:
                    lista3.remove('acg')
                    lista3.append('T')
                    seq4 = ''
                if 'act' in lista3:
                    lista3.remove('act')
                    lista3.append('T')
                    seq4 = ''
                if 'acc' in lista3:
                    lista3.remove('acc')
                    lista3.append('N')
                    seq4 = ''
                if 'aag' in lista3:
                    lista3.remove('aag')
                    lista3.append('K')
                    seq4 = ''
                if 'agc' in lista3:
                    lista3.remove('agc')
                    lista3.append('S')
                    seq4 = ''
                if 'agt' in lista3:
                    lista3.remove('agt')
                    lista3.append('S')
                    seq4 = ''
                if 'aga' in lista3:
                    lista3.remove('aga')
                    lista3.append('R')
                    seq4 = ''
                if 'agg' in lista3:
                    lista3.remove('agg')
                    lista3.append('R')
                    seq4 = ''
                if 'cta' in lista3:
                    lista3.remove('cta')
                    lista3.append('L')
                    seq4 = ''
                if 'ctc' in lista3:
                    lista3.remove('ctc')
                    lista3.append('L')
                    seq4 = ''
                if 'ctg' in lista3:
                    lista3.remove('ctg')
                    lista3.append('L')
                    seq4 = ''
                if 'ctt' in lista3:
                    lista3.remove('ctt')
                    lista3.append('L')
                    seq4 = ''
                if 'cca' in lista3:
                    lista3.remove('cca')
                    lista3.append('P')
                    seq4 = ''
                if 'ccc' in lista3:
                    lista3.remove('ccc')
                    lista3.append('P')
                    seq4 = ''
                if 'ccg' in lista3:
                    lista3.remove('ccg')
                    lista3.append('P')
                    seq4 = ''
                if 'cct' in lista3:
                    lista3.remove('cct')
                    lista3.append('P')
                    seq4 = ''
                if 'cac' in lista3:
                    lista3.remove('cac')
                    lista3.append('H')
                    seq4 = ''
                if 'cat' in lista3:
                    lista3.remove('cat')
                    lista3.append('H')
                    seq4 = ''
                if 'caa' in lista3:
                    lista3.remove('caa')
                    lista3.append('Q')
                    seq4 = ''
                if 'cag' in lista3:
                    lista3.remove('cag')
                    lista3.append('Q')
                    seq4 = ''
                if 'cga' in lista3:
                    lista3.remove('cga')
                    lista3.append('R')
                    seq4 = ''
                if 'cgc' in lista3:
                    lista3.remove('cgc')
                    lista3.append('R')
                    seq4 = ''
                if 'cgg' in lista3:
                    lista3.remove('cgg')
                    lista3.append('R')
                    seq4 = ''
                if 'cgt' in lista3:
                    lista3.remove('cgt')
                    lista3.append('R')
                    seq4 = ''
                if 'gta' in lista3:
                    lista3.remove('gta')
                    lista3.append('V')
                    seq4 = ''
                if 'gtc' in lista3:
                    lista3.remove('gtc')
                    lista3.append('V')
                    seq4 = ''
                if 'gtg' in lista3:
                    lista3.remove('gtg')
                    lista3.append('V')
                    seq4 = ''
                if 'gtt' in lista3:
                    lista3.remove('gtt')
                    lista3.append('V')
                    seq4 = ''
                if 'gca' in lista3:
                    lista3.remove('gca')
                    lista3.append('A')
                    seq4 = ''
                if 'gcc' in lista3:
                    lista3.remove('gcc')
                    lista3.append('A')
                    seq4 = ''
                if 'gcg' in lista3:
                    lista3.remove('gcg')
                    lista3.append('A')
                    seq4 = ''
                if 'gct' in lista3:
                    lista3.remove('gct')
                    lista3.append('A')
                    seq4 = ''
                if 'gac' in lista3:
                    lista3.remove('gac')
                    lista3.append('D')
                    seq4 = ''
                if 'gat' in lista3:
                    lista3.remove('gat')
                    lista3.append('D')
                    seq4 = ''
                if 'gag' in lista3:
                    lista3.remove('gag')
                    lista3.append('E')
                    seq4 = ''
                if 'gga' in lista3:
                    lista3.remove('gga')
                    lista3.append('G')
                    seq4 = ''
                if 'gaa' in lista3:
                    lista3.remove('gaa')
                    lista3.append('E')
                    seq4 = ''
                if 'ggc' in lista3:
                    lista3.remove('ggc')
                    lista3.append('G')
                    seq4 = ''
                if 'ggg' in lista3:
                    lista3.remove('ggg')
                    lista3.append('G')
                    seq4 = ''
                if 'ggt' in lista3:
                    lista3.remove('ggt')
                    lista3.append('G')
                    seq4 = ''
                if 'tca' in lista3:
                    lista3.remove('tca')
                    lista3.append('S')
                    seq4 = ''
                if 'ttc' in lista3:
                    lista3.remove('ttc')
                    lista3.append('F')
                    seq4 = ''
                if 'tcg' in lista3:
                    lista3.remove('tcg')
                    lista3.append('S')
                    seq4 = ''
                if 'tct' in lista3:
                    lista3.remove('tct')
                    lista3.append('S')
                    seq4 = ''
                if 'ttc' in lista3:
                    lista3.remove('ttc')
                    lista3.append('F')
                    seq4 = ''
                if 'ttt' in lista3:
                    lista3.remove('ttt')
                    lista3.append('F')
                    seq4 = ''
                if 'tta' in lista3:
                    lista3.remove('tta')
                    lista3.append('L')
                    seq4 = ''
                if 'ttg' in lista3:
                    lista3.remove('ttg')
                    lista3.append('L')
                    seq4 = ''
                if 'tac' in lista3:
                    lista3.remove('tac')
                    lista3.append('Y')
                    seq4 = ''
                if 'tat' in lista3:
                    lista3.remove('tat')
                    lista3.append('Y')
                    seq4 = ''
                if 'taa' in lista3:
                    lista3.remove('taa')
                    lista3.append(('_'))
                    seq4 = ''
                if 'tag' in lista3:
                    lista3.remove('tag')
                    lista3.append(('_'))
                    seq4 = ''
                if 'tgc' in lista3:
                    lista3.remove('tgc')
                    lista3.append('C')
                    seq4 = ''
                if 'tgt' in lista3:
                    lista3.remove('tgt')
                    lista3.append('C')
                    seq4 = ''
                if 'tga' in lista3:
                    lista3.remove('tga')
                    lista3.append(('_'))
                    seq4 = ''
                if 'tgg' in lista3:
                    lista3.remove('tgg')
                    lista3.append('W')
                    seq4 = ''
                if 'tcc' in lista3:
                    lista3.remove('tcc')
                    lista3.append('S')
                    seq4 = ''
                if 'aac' in lista3:
                    lista3.remove('aac')
                    lista3.append('N')
                    seq4 = ''
                else:
                    seq4 = ''
        d = ''.join(lista3)
        d1 = d.find('M')
        print('Sua sequência traduzida em quadro de leitura -1 é:\n', d)
        print('A sequência a partir do start códon é:\n', d[d1:])
        print(50 * '-=-', '\n\n')
        tradução.write('\n\nSequência integral -1:\t')
        for aa in d:
            tradução.write(aa[d2::-1])
        tradução.write('\nSequência tratada -1:\t')
        for aa in d[d1:]:
            tradução.write(aa)
    tradutor_1()
    def tradutor_2():
        lista3 = []
        seq4 = ''
        d2 = len(seq)
        for i in seq[d2::-2]:
            seq4 = seq4 + i
            if len(seq4) == 3:
                lista3.append(seq4)
                seq4 = ''
                if 'ata' in lista3:
                    lista3.remove('ata')
                    lista3.append('I')
                    seq4 = ''
                if 'aaa' in lista3:
                    lista3.remove('aaa')
                    lista3.append('K')
                    seq4 = ''
                if 'atc' in lista3:
                    lista3.remove('atc')
                    lista3.append('I')
                    seq4 = ''
                if 'att' in lista3:
                    lista3.remove('att')
                    lista3.append('I')
                    seq4 = ''
                if 'aat' in lista3:
                    lista3.remove('aat')
                    lista3.append('N')
                    seq4 = ''
                if 'atg' in lista3:
                    lista3.remove('atg')
                    lista3.append('M')
                    seq4 = ''
                if 'aca' in lista3:
                    lista3.remove('aca')
                    lista3.append('T')
                    seq4 = ''
                if 'acc' in lista3:
                    lista3.remove('acc')
                    lista3.append('T')
                    seq4 = ''
                if 'acg' in lista3:
                    lista3.remove('acg')
                    lista3.append('T')
                    seq4 = ''
                if 'act' in lista3:
                    lista3.remove('act')
                    lista3.append('T')
                    seq4 = ''
                if 'acc' in lista3:
                    lista3.remove('acc')
                    lista3.append('N')
                    seq4 = ''
                if 'aag' in lista3:
                    lista3.remove('aag')
                    lista3.append('K')
                    seq4 = ''
                if 'agc' in lista3:
                    lista3.remove('agc')
                    lista3.append('S')
                    seq4 = ''
                if 'agt' in lista3:
                    lista3.remove('agt')
                    lista3.append('S')
                    seq4 = ''
                if 'aga' in lista3:
                    lista3.remove('aga')
                    lista3.append('R')
                    seq4 = ''
                if 'agg' in lista3:
                    lista3.remove('agg')
                    lista3.append('R')
                    seq4 = ''
                if 'cta' in lista3:
                    lista3.remove('cta')
                    lista3.append('L')
                    seq4 = ''
                if 'ctc' in lista3:
                    lista3.remove('ctc')
                    lista3.append('L')
                    seq4 = ''
                if 'ctg' in lista3:
                    lista3.remove('ctg')
                    lista3.append('L')
                    seq4 = ''
                if 'ctt' in lista3:
                    lista3.remove('ctt')
                    lista3.append('L')
                    seq4 = ''
                if 'cca' in lista3:
                    lista3.remove('cca')
                    lista3.append('P')
                    seq4 = ''
                if 'ccc' in lista3:
                    lista3.remove('ccc')
                    lista3.append('P')
                    seq4 = ''
                if 'ccg' in lista3:
                    lista3.remove('ccg')
                    lista3.append('P')
                    seq4 = ''
                if 'cct' in lista3:
                    lista3.remove('cct')
                    lista3.append('P')
                    seq4 = ''
                if 'cac' in lista3:
                    lista3.remove('cac')
                    lista3.append('H')
                    seq4 = ''
                if 'cat' in lista3:
                    lista3.remove('cat')
                    lista3.append('H')
                    seq4 = ''
                if 'caa' in lista3:
                    lista3.remove('caa')
                    lista3.append('Q')
                    seq4 = ''
                if 'cag' in lista3:
                    lista3.remove('cag')
                    lista3.append('Q')
                    seq4 = ''
                if 'cga' in lista3:
                    lista3.remove('cga')
                    lista3.append('R')
                    seq4 = ''
                if 'cgc' in lista3:
                    lista3.remove('cgc')
                    lista3.append('R')
                    seq4 = ''
                if 'cgg' in lista3:
                    lista3.remove('cgg')
                    lista3.append('R')
                    seq4 = ''
                if 'cgt' in lista3:
                    lista3.remove('cgt')
                    lista3.append('R')
                    seq4 = ''
                if 'gta' in lista3:
                    lista3.remove('gta')
                    lista3.append('V')
                    seq4 = ''
                if 'gtc' in lista3:
                    lista3.remove('gtc')
                    lista3.append('V')
                    seq4 = ''
                if 'gtg' in lista3:
                    lista3.remove('gtg')
                    lista3.append('V')
                    seq4 = ''
                if 'gtt' in lista3:
                    lista3.remove('gtt')
                    lista3.append('V')
                    seq4 = ''
                if 'gca' in lista3:
                    lista3.remove('gca')
                    lista3.append('A')
                    seq4 = ''
                if 'gcc' in lista3:
                    lista3.remove('gcc')
                    lista3.append('A')
                    seq4 = ''
                if 'gcg' in lista3:
                    lista3.remove('gcg')
                    lista3.append('A')
                    seq4 = ''
                if 'gct' in lista3:
                    lista3.remove('gct')
                    lista3.append('A')
                    seq4 = ''
                if 'gac' in lista3:
                    lista3.remove('gac')
                    lista3.append('D')
                    seq4 = ''
                if 'gat' in lista3:
                    lista3.remove('gat')
                    lista3.append('D')
                    seq4 = ''
                if 'gag' in lista3:
                    lista3.remove('gag')
                    lista3.append('E')
                    seq4 = ''
                if 'gga' in lista3:
                    lista3.remove('gga')
                    lista3.append('G')
                    seq4 = ''
                if 'gaa' in lista3:
                    lista3.remove('gaa')
                    lista3.append('E')
                    seq4 = ''
                if 'ggc' in lista3:
                    lista3.remove('ggc')
                    lista3.append('G')
                    seq4 = ''
                if 'ggg' in lista3:
                    lista3.remove('ggg')
                    lista3.append('G')
                    seq4 = ''
                if 'ggt' in lista3:
                    lista3.remove('ggt')
                    lista3.append('G')
                    seq4 = ''
                if 'tca' in lista3:
                    lista3.remove('tca')
                    lista3.append('S')
                    seq4 = ''
                if 'ttc' in lista3:
                    lista3.remove('ttc')
                    lista3.append('F')
                    seq4 = ''
                if 'tcg' in lista3:
                    lista3.remove('tcg')
                    lista3.append('S')
                    seq4 = ''
                if 'tct' in lista3:
                    lista3.remove('tct')
                    lista3.append('S')
                    seq4 = ''
                if 'ttc' in lista3:
                    lista3.remove('ttc')
                    lista3.append('F')
                    seq4 = ''
                if 'ttt' in lista3:
                    lista3.remove('ttt')
                    lista3.append('F')
                    seq4 = ''
                if 'tta' in lista3:
                    lista3.remove('tta')
                    lista3.append('L')
                    seq4 = ''
                if 'ttg' in lista3:
                    lista3.remove('ttg')
                    lista3.append('L')
                    seq4 = ''
                if 'tac' in lista3:
                    lista3.remove('tac')
                    lista3.append('Y')
                    seq4 = ''
                if 'tat' in lista3:
                    lista3.remove('tat')
                    lista3.append('Y')
                    seq4 = ''
                if 'taa' in lista3:
                    lista3.remove('taa')
                    lista3.append(('_'))
                    seq4 = ''
                if 'tag' in lista3:
                    lista3.remove('tag')
                    lista3.append(('_'))
                    seq4 = ''
                if 'tgc' in lista3:
                    lista3.remove('tgc')
                    lista3.append('C')
                    seq4 = ''
                if 'tgt' in lista3:
                    lista3.remove('tgt')
                    lista3.append('C')
                    seq4 = ''
                if 'tga' in lista3:
                    lista3.remove('tga')
                    lista3.append(('_'))
                    seq4 = ''
                if 'tgg' in lista3:
                    lista3.remove('tgg')
                    lista3.append('W')
                    seq4 = ''
                if 'tcc' in lista3:
                    lista3.remove('tcc')
                    lista3.append('S')
                    seq4 = ''
                if 'aac' in lista3:
                    lista3.remove('aac')
                    lista3.append('N')
                    seq4 = ''
                else:
                    seq4 = ''
        d = ''.join(lista3)
        d1 = d.find('M')
        print('Sua sequência traduzida em quadro de leitura -2 é:\n', d)
        print('A sequência a partir do start códon é:\n', d[d1:])
        print(50 * '-=-', '\n\n')
        tradução.write('\n\nSequência integral -2:\t')
        for aa in d:
            tradução.write(aa[d2::-2])
        tradução.write('\nSequência tratada -2:\t')
        for aa in d[d1:]:
            tradução.write(aa)
    tradutor_2()
    def tradutor_3():
        lista3 = []
        seq4 = ''
        d2 = len(seq)
        for i in seq[d2::-3]:
            seq4 = seq4 + i
            if len(seq4) == 3:
                lista3.append(seq4)
                seq4 = ''
                if 'ata' in lista3:
                    lista3.remove('ata')
                    lista3.append('I')
                    seq4 = ''
                if 'aaa' in lista3:
                    lista3.remove('aaa')
                    lista3.append('K')
                    seq4 = ''
                if 'atc' in lista3:
                    lista3.remove('atc')
                    lista3.append('I')
                    seq4 = ''
                if 'att' in lista3:
                    lista3.remove('att')
                    lista3.append('I')
                    seq4 = ''
                if 'aat' in lista3:
                    lista3.remove('aat')
                    lista3.append('N')
                    seq4 = ''
                if 'atg' in lista3:
                    lista3.remove('atg')
                    lista3.append('M')
                    seq4 = ''
                if 'aca' in lista3:
                    lista3.remove('aca')
                    lista3.append('T')
                    seq4 = ''
                if 'acc' in lista3:
                    lista3.remove('acc')
                    lista3.append('T')
                    seq4 = ''
                if 'acg' in lista3:
                    lista3.remove('acg')
                    lista3.append('T')
                    seq4 = ''
                if 'act' in lista3:
                    lista3.remove('act')
                    lista3.append('T')
                    seq4 = ''
                if 'acc' in lista3:
                    lista3.remove('acc')
                    lista3.append('N')
                    seq4 = ''
                if 'aag' in lista3:
                    lista3.remove('aag')
                    lista3.append('K')
                    seq4 = ''
                if 'agc' in lista3:
                    lista3.remove('agc')
                    lista3.append('S')
                    seq4 = ''
                if 'agt' in lista3:
                    lista3.remove('agt')
                    lista3.append('S')
                    seq4 = ''
                if 'aga' in lista3:
                    lista3.remove('aga')
                    lista3.append('R')
                    seq4 = ''
                if 'agg' in lista3:
                    lista3.remove('agg')
                    lista3.append('R')
                    seq4 = ''
                if 'cta' in lista3:
                    lista3.remove('cta')
                    lista3.append('L')
                    seq4 = ''
                if 'ctc' in lista3:
                    lista3.remove('ctc')
                    lista3.append('L')
                    seq4 = ''
                if 'ctg' in lista3:
                    lista3.remove('ctg')
                    lista3.append('L')
                    seq4 = ''
                if 'ctt' in lista3:
                    lista3.remove('ctt')
                    lista3.append('L')
                    seq4 = ''
                if 'cca' in lista3:
                    lista3.remove('cca')
                    lista3.append('P')
                    seq4 = ''
                if 'ccc' in lista3:
                    lista3.remove('ccc')
                    lista3.append('P')
                    seq4 = ''
                if 'ccg' in lista3:
                    lista3.remove('ccg')
                    lista3.append('P')
                    seq4 = ''
                if 'cct' in lista3:
                    lista3.remove('cct')
                    lista3.append('P')
                    seq4 = ''
                if 'cac' in lista3:
                    lista3.remove('cac')
                    lista3.append('H')
                    seq4 = ''
                if 'cat' in lista3:
                    lista3.remove('cat')
                    lista3.append('H')
                    seq4 = ''
                if 'caa' in lista3:
                    lista3.remove('caa')
                    lista3.append('Q')
                    seq4 = ''
                if 'cag' in lista3:
                    lista3.remove('cag')
                    lista3.append('Q')
                    seq4 = ''
                if 'cga' in lista3:
                    lista3.remove('cga')
                    lista3.append('R')
                    seq4 = ''
                if 'cgc' in lista3:
                    lista3.remove('cgc')
                    lista3.append('R')
                    seq4 = ''
                if 'cgg' in lista3:
                    lista3.remove('cgg')
                    lista3.append('R')
                    seq4 = ''
                if 'cgt' in lista3:
                    lista3.remove('cgt')
                    lista3.append('R')
                    seq4 = ''
                if 'gta' in lista3:
                    lista3.remove('gta')
                    lista3.append('V')
                    seq4 = ''
                if 'gtc' in lista3:
                    lista3.remove('gtc')
                    lista3.append('V')
                    seq4 = ''
                if 'gtg' in lista3:
                    lista3.remove('gtg')
                    lista3.append('V')
                    seq4 = ''
                if 'gtt' in lista3:
                    lista3.remove('gtt')
                    lista3.append('V')
                    seq4 = ''
                if 'gca' in lista3:
                    lista3.remove('gca')
                    lista3.append('A')
                    seq4 = ''
                if 'gcc' in lista3:
                    lista3.remove('gcc')
                    lista3.append('A')
                    seq4 = ''
                if 'gcg' in lista3:
                    lista3.remove('gcg')
                    lista3.append('A')
                    seq4 = ''
                if 'gct' in lista3:
                    lista3.remove('gct')
                    lista3.append('A')
                    seq4 = ''
                if 'gac' in lista3:
                    lista3.remove('gac')
                    lista3.append('D')
                    seq4 = ''
                if 'gat' in lista3:
                    lista3.remove('gat')
                    lista3.append('D')
                    seq4 = ''
                if 'gag' in lista3:
                    lista3.remove('gag')
                    lista3.append('E')
                    seq4 = ''
                if 'gga' in lista3:
                    lista3.remove('gga')
                    lista3.append('G')
                    seq4 = ''
                if 'gaa' in lista3:
                    lista3.remove('gaa')
                    lista3.append('E')
                    seq4 = ''
                if 'ggc' in lista3:
                    lista3.remove('ggc')
                    lista3.append('G')
                    seq4 = ''
                if 'ggg' in lista3:
                    lista3.remove('ggg')
                    lista3.append('G')
                    seq4 = ''
                if 'ggt' in lista3:
                    lista3.remove('ggt')
                    lista3.append('G')
                    seq4 = ''
                if 'tca' in lista3:
                    lista3.remove('tca')
                    lista3.append('S')
                    seq4 = ''
                if 'ttc' in lista3:
                    lista3.remove('ttc')
                    lista3.append('F')
                    seq4 = ''
                if 'tcg' in lista3:
                    lista3.remove('tcg')
                    lista3.append('S')
                    seq4 = ''
                if 'tct' in lista3:
                    lista3.remove('tct')
                    lista3.append('S')
                    seq4 = ''
                if 'ttc' in lista3:
                    lista3.remove('ttc')
                    lista3.append('F')
                    seq4 = ''
                if 'ttt' in lista3:
                    lista3.remove('ttt')
                    lista3.append('F')
                    seq4 = ''
                if 'tta' in lista3:
                    lista3.remove('tta')
                    lista3.append('L')
                    seq4 = ''
                if 'ttg' in lista3:
                    lista3.remove('ttg')
                    lista3.append('L')
                    seq4 = ''
                if 'tac' in lista3:
                    lista3.remove('tac')
                    lista3.append('Y')
                    seq4 = ''
                if 'tat' in lista3:
                    lista3.remove('tat')
                    lista3.append('Y')
                    seq4 = ''
                if 'taa' in lista3:
                    lista3.remove('taa')
                    lista3.append(('_'))
                    seq4 = ''
                if 'tag' in lista3:
                    lista3.remove('tag')
                    lista3.append(('_'))
                    seq4 = ''
                if 'tgc' in lista3:
                    lista3.remove('tgc')
                    lista3.append('C')
                    seq4 = ''
                if 'tgt' in lista3:
                    lista3.remove('tgt')
                    lista3.append('C')
                    seq4 = ''
                if 'tga' in lista3:
                    lista3.remove('tga')
                    lista3.append(('_'))
                    seq4 = ''
                if 'tgg' in lista3:
                    lista3.remove('tgg')
                    lista3.append('W')
                    seq4 = ''
                if 'tcc' in lista3:
                    lista3.remove('tcc')
                    lista3.append('S')
                    seq4 = ''
                if 'aac' in lista3:
                    lista3.remove('aac')
                    lista3.append('N')
                    seq4 = ''
                else:
                    seq4 = ''
        d = ''.join(lista3)
        d1 = d.find('M')
        print('Sua sequência traduzida em quadro de leitura -3 é:\n', d)
        print('A sequência a partir do start códon é:\n', d[d1:])
        print(50 * '-=-', '\n\n')
        tradução.write('\n\nSequência integral -3:\t')
        for aa in d:
            tradução.write(aa[d2::-3])
        tradução.write('\nSequência tratada -3:\t')
        for aa in d[d1:]:
            tradução.write(aa)
        tradução.write('\n\n')
    tradutor_3()

    tradução.write(40*'-=-=-=-=-=-=-=-\t')

    def tradutor1():
        lista = []
        seq1 = ''
        for i in seq:
            seq1 = seq1 + i
            if len(seq1) == 3:
                lista.append(seq1)
                seq1 = ''
                if 'ata' in lista:
                    lista.remove('ata')
                    lista.append('I')
                    seq1 = ''
                if 'aaa' in lista:
                    lista.remove('aaa')
                    lista.append('K')
                    seq1 = ''
                if 'atc' in lista:
                    lista.remove('atc')
                    lista.append('I')
                    seq1 = ''
                if 'att' in lista:
                    lista.remove('att')
                    lista.append('I')
                    seq1 = ''
                if 'aat' in lista:
                    lista.remove('aat')
                    lista.append('N')
                    seq1 = ''
                if 'atg' in lista:
                    lista.remove('atg')
                    lista.append('M')
                    seq1 = ''
                if 'aca' in lista:
                    lista.remove('aca')
                    lista.append('T')
                    seq1 = ''
                if 'acc' in lista:
                    lista.remove('acc')
                    lista.append('T')
                    seq1 = ''
                if 'aac' in lista:
                    lista.remove('aac')
                    lista.append('N')
                if 'acg' in lista:
                    lista.remove('acg')
                    lista.append('T')
                    seq1 = ''
                if 'act' in lista:
                    lista.remove('act')
                    lista.append('T')
                    seq1 = ''
                if 'acc' in lista:
                    lista.remove('acc')
                    lista.append('N')
                    seq1 = ''
                if 'aag' in lista:
                    lista.remove('aag')
                    lista.append('K')
                    seq1 = ''
                if 'agc' in lista:
                    lista.remove('agc')
                    lista.append('S')
                    seq1 = ''
                if 'agt' in lista:
                    lista.remove('agt')
                    lista.append('S')
                    seq1 = ''
                if 'aga' in lista:
                    lista.remove('aga')
                    lista.append('R')
                    seq1 = ''
                if 'agg' in lista:
                    lista.remove('agg')
                    lista.append('R')
                    seq1 = ''
                if 'cta' in lista:
                    lista.remove('cta')
                    lista.append('L')
                    seq1 = ''
                if 'ctc' in lista:
                    lista.remove('ctc')
                    lista.append('L')
                    seq1 = ''
                if 'ctg' in lista:
                    lista.remove('ctg')
                    lista.append('L')
                    seq1 = ''
                if 'ctt' in lista:
                    lista.remove('ctt')
                    lista.append('L')
                    seq1 = ''
                if 'cca' in lista:
                    lista.remove('cca')
                    lista.append('P')
                    seq1 = ''
                if 'ccc' in lista:
                    lista.remove('ccc')
                    lista.append('P')
                    seq1 = ''
                if 'ccg' in lista:
                    lista.remove('ccg')
                    lista.append('P')
                    seq1 = ''
                if 'cct' in lista:
                    lista.remove('cct')
                    lista.append('P')
                    seq1 = ''
                if 'cac'  in lista:
                    lista.remove('cac')
                    lista.append('H')
                    seq1 = ''
                if 'cat'  in lista:
                    lista.remove('cat')
                    lista.append('H')
                    seq1 = ''
                if 'caa'  in lista:
                    lista.remove('caa')
                    lista.append('Q')
                    seq1 = ''
                if 'cag'  in lista:
                    lista.remove('cag')
                    lista.append('Q')
                    seq1 = ''
                if 'cga'  in lista:
                    lista.remove('cga')
                    lista.append('R')
                    seq1 = ''
                if 'cgc'  in lista:
                    lista.remove('cgc')
                    lista.append('R')
                    seq1 = ''
                if 'cgg'  in lista:
                    lista.remove('cgg')
                    lista.append('R')
                    seq1 = ''
                if 'cgt'  in lista:
                    lista.remove('cgt')
                    lista.append('R')
                    seq1 = ''
                if 'gta'  in lista:
                    lista.remove('gta')
                    lista.append('V')
                    seq1 = ''
                if 'gtc'  in lista:
                    lista.remove('gtc')
                    lista.append('V')
                    seq1 = ''
                if 'gtg'  in lista:
                    lista.remove('gtg')
                    lista.append('V')
                    seq1 = ''
                if 'gtt'  in lista:
                    lista.remove('gtt')
                    lista.append('V')
                    seq1 = ''
                if 'gca'  in lista:
                    lista.remove('gca')
                    lista.append('A')
                    seq1 = ''
                if 'gcc'  in lista:
                    lista.remove('gcc')
                    lista.append('A')
                    seq1 = ''
                if 'gcg'  in lista:
                    lista.remove('gcg')
                    lista.append('A')
                    seq1 = ''
                if 'gct'  in lista:
                    lista.remove('gct')
                    lista.append('A')
                    seq1 = ''
                if 'gac'  in lista:
                    lista.remove('gac')
                    lista.append('D')
                    seq1 = ''
                if 'gat'  in lista:
                    lista.remove('gat')
                    lista.append('D')
                    seq1 = ''
                if 'gag'  in lista:
                    lista.remove('gag')
                    lista.append('E')
                    seq1 = ''
                if 'gga'  in lista:
                    lista.remove('gga')
                    lista.append('G')
                    seq1 = ''
                if 'gaa'  in lista:
                    lista.remove('gaa')
                    lista.append('E')
                    seq1 = ''
                if 'ggc'  in lista:
                    lista.remove('ggc')
                    lista.append('G')
                    seq1 = ''
                if 'ggg'  in lista:
                    lista.remove('ggg')
                    lista.append('G')
                    seq1 = ''
                if 'ggt'  in lista:
                    lista.remove('ggt')
                    lista.append('G')
                    seq1 = ''
                if 'tca'  in lista:
                    lista.remove('tca')
                    lista.append('S')
                    seq1 = ''
                if 'ttc'  in lista:
                    lista.remove('ttc')
                    lista.append('F')
                    seq1 = ''
                if 'tcg'  in lista:
                    lista.remove('tcg')
                    lista.append('S')
                    seq1 = ''
                if 'tct'  in lista:
                    lista.remove('tct')
                    lista.append('S')
                    seq1 = ''
                if 'ttc'  in lista:
                    lista.remove('ttc')
                    lista.append('F')
                    seq1 = ''
                if 'ttt'  in lista:
                    lista.remove('ttt')
                    lista.append('F')
                    seq1 = ''
                if 'tta' in lista:
                    lista.remove('tta')
                    lista.append('L')
                    seq1 = ''
                if 'ttg' in lista:
                    lista.remove('ttg')
                    lista.append('L')
                    seq1 = ''
                if 'tac' in lista:
                    lista.remove('tac')
                    lista.append('Y')
                    seq1 = ''
                if 'tat' in lista:
                    lista.remove('tat')
                    lista.append('Y')
                    seq1 = ''
                if 'taa' in lista:
                    lista.remove('taa')
                    lista.append(('_\t'))
                    seq1 = ''
                if 'tag' in lista:
                    lista.remove('tag')
                    lista.append(('_\t'))
                    seq1 = ''
                if 'tgc' in lista:
                    lista.remove('tgc')
                    lista.append('C')
                    seq1 = ''
                if 'tgt' in lista:
                    lista.remove('tgt')
                    lista.append('C')
                    seq1 = ''
                if 'tga' in lista:
                    lista.remove('tga')
                    lista.append(('_\t'))
                    seq1 = ''
                if 'tgg' in lista:
                    lista.remove('tgg')
                    lista.append('W')
                    seq1 = ''
                if 'tcc' in lista:
                    lista.remove('tcc')
                    lista.append('S')
                    seq1 = ''
                else:
                    seq1 = ''
        a = ''.join(lista)
        a1 = a.find('M')
        a2 = a.find('K''K''K''K''K''K')
        print('Sua sequência traduzida em quadro de leitura +1 é:\n', a)
        print('A sequência a partir do start códon é:\n', a[a1:a2])
        print(50*'-=-', '\n\n')
        tradução.write('\n\nSequência integral +1:\t')
        for aa in a:
            tradução.write(aa)
        tradução.write('\nSequência tratada +1:\t')
        for aa in a[a1:a2]:
            tradução.write(aa)
    tradutor1()
    def tradutor2():
        lista = []
        seq1 = ''
        for i in seq[1:]:
            seq1 = seq1 + i
            if len(seq1) == 3:
                lista.append(seq1)
                seq1 = ''
                if 'ata' in lista:
                    lista.remove('ata')
                    lista.append('I')
                    seq1 = ''
                if 'aaa' in lista:
                    lista.remove('aaa')
                    lista.append('K')
                    seq1 = ''
                if 'atc' in lista:
                    lista.remove('atc')
                    lista.append('I')
                    seq1 = ''
                if 'att' in lista:
                    lista.remove('att')
                    lista.append('I')
                    seq1 = ''
                if 'aat' in lista:
                    lista.remove('aat')
                    lista.append('N')
                    seq1 = ''
                if 'atg' in lista:
                    lista.remove('atg')
                    lista.append('M')
                    seq1 = ''
                if 'aca' in lista:
                    lista.remove('aca')
                    lista.append('T')
                    seq1 = ''
                if 'acc' in lista:
                    lista.remove('acc')
                    lista.append('T')
                    seq1 = ''
                if 'aac' in lista:
                    lista.remove('aac')
                    lista.append('N')
                if 'acg' in lista:
                    lista.remove('acg')
                    lista.append('T')
                    seq1 = ''
                if 'act' in lista:
                    lista.remove('act')
                    lista.append('T')
                    seq1 = ''
                if 'acc' in lista:
                    lista.remove('acc')
                    lista.append('N')
                    seq1 = ''
                if 'aag' in lista:
                    lista.remove('aag')
                    lista.append('K')
                    seq1 = ''
                if 'agc' in lista:
                    lista.remove('agc')
                    lista.append('S')
                    seq1 = ''
                if 'agt' in lista:
                    lista.remove('agt')
                    lista.append('S')
                    seq1 = ''
                if 'aga' in lista:
                    lista.remove('aga')
                    lista.append('R')
                    seq1 = ''
                if 'agg' in lista:
                    lista.remove('agg')
                    lista.append('R')
                    seq1 = ''
                if 'cta' in lista:
                    lista.remove('cta')
                    lista.append('L')
                    seq1 = ''
                if 'ctc' in lista:
                    lista.remove('ctc')
                    lista.append('L')
                    seq1 = ''
                if 'ctg' in lista:
                    lista.remove('ctg')
                    lista.append('L')
                    seq1 = ''
                if 'ctt' in lista:
                    lista.remove('ctt')
                    lista.append('L')
                    seq1 = ''
                if 'cca' in lista:
                    lista.remove('cca')
                    lista.append('P')
                    seq1 = ''
                if 'ccc' in lista:
                    lista.remove('ccc')
                    lista.append('P')
                    seq1 = ''
                if 'ccg' in lista:
                    lista.remove('ccg')
                    lista.append('P')
                    seq1 = ''
                if 'cct' in lista:
                    lista.remove('cct')
                    lista.append('P')
                    seq1 = ''
                if 'cac' in lista:
                    lista.remove('cac')
                    lista.append('H')
                    seq1 = ''
                if 'cat' in lista:
                    lista.remove('cat')
                    lista.append('H')
                    seq1 = ''
                if 'caa' in lista:
                    lista.remove('caa')
                    lista.append('Q')
                    seq1 = ''
                if 'cag' in lista:
                    lista.remove('cag')
                    lista.append('Q')
                    seq1 = ''
                if 'cga' in lista:
                    lista.remove('cga')
                    lista.append('R')
                    seq1 = ''
                if 'cgc' in lista:
                    lista.remove('cgc')
                    lista.append('R')
                    seq1 = ''
                if 'cgg' in lista:
                    lista.remove('cgg')
                    lista.append('R')
                    seq1 = ''
                if 'cgt' in lista:
                    lista.remove('cgt')
                    lista.append('R')
                    seq1 = ''
                if 'gta' in lista:
                    lista.remove('gta')
                    lista.append('V')
                    seq1 = ''
                if 'gtc' in lista:
                    lista.remove('gtc')
                    lista.append('V')
                    seq1 = ''
                if 'gtg' in lista:
                    lista.remove('gtg')
                    lista.append('V')
                    seq1 = ''
                if 'gtt' in lista:
                    lista.remove('gtt')
                    lista.append('V')
                    seq1 = ''
                if 'gca' in lista:
                    lista.remove('gca')
                    lista.append('A')
                    seq1 = ''
                if 'gcc' in lista:
                    lista.remove('gcc')
                    lista.append('A')
                    seq1 = ''
                if 'gcg' in lista:
                    lista.remove('gcg')
                    lista.append('A')
                    seq1 = ''
                if 'gct' in lista:
                    lista.remove('gct')
                    lista.append('A')
                    seq1 = ''
                if 'gac' in lista:
                    lista.remove('gac')
                    lista.append('D')
                    seq1 = ''
                if 'gat' in lista:
                    lista.remove('gat')
                    lista.append('D')
                    seq1 = ''
                if 'gag' in lista:
                    lista.remove('gag')
                    lista.append('E')
                    seq1 = ''
                if 'gga' in lista:
                    lista.remove('gga')
                    lista.append('G')
                    seq1 = ''
                if 'gaa' in lista:
                    lista.remove('gaa')
                    lista.append('E')
                    seq1 = ''
                if 'ggc' in lista:
                    lista.remove('ggc')
                    lista.append('G')
                    seq1 = ''
                if 'ggg' in lista:
                    lista.remove('ggg')
                    lista.append('G')
                    seq1 = ''
                if 'ggt' in lista:
                    lista.remove('ggt')
                    lista.append('G')
                    seq1 = ''
                if 'tca' in lista:
                    lista.remove('tca')
                    lista.append('S')
                    seq1 = ''
                if 'ttc' in lista:
                    lista.remove('ttc')
                    lista.append('F')
                    seq1 = ''
                if 'tcg' in lista:
                    lista.remove('tcg')
                    lista.append('S')
                    seq1 = ''
                if 'tct' in lista:
                    lista.remove('tct')
                    lista.append('S')
                    seq1 = ''
                if 'ttc' in lista:
                    lista.remove('ttc')
                    lista.append('F')
                    seq1 = ''
                if 'ttt' in lista:
                    lista.remove('ttt')
                    lista.append('F')
                    seq1 = ''
                if 'tta' in lista:
                    lista.remove('tta')
                    lista.append('L')
                    seq1 = ''
                if 'ttg' in lista:
                    lista.remove('ttg')
                    lista.append('L')
                    seq1 = ''
                if 'tac' in lista:
                    lista.remove('tac')
                    lista.append('Y')
                    seq1 = ''
                if 'tat' in lista:
                    lista.remove('tat')
                    lista.append('Y')
                    seq1 = ''
                if 'taa' in lista:
                    lista.remove('taa')
                    lista.append(('_\t'))
                    seq1 = ''
                if 'tag' in lista:
                    lista.remove('tag')
                    lista.append(('_\t'))
                    seq1 = ''
                if 'tgc' in lista:
                    lista.remove('tgc')
                    lista.append('C')
                    seq1 = ''
                if 'tgt' in lista:
                    lista.remove('tgt')
                    lista.append('C')
                    seq1 = ''
                if 'tga' in lista:
                    lista.remove('tga')
                    lista.append(('_\t'))
                    seq1 = ''
                if 'tgg' in lista:
                    lista.remove('tgg')
                    lista.append('W')
                    seq1 = ''
                if 'tcc' in lista:
                    lista.remove('tcc')
                    lista.append('S')
                    seq1 = ''
                else:
                    seq1 = ''
        a = ''.join(lista)
        a1 = a.find('M')
        a2 = a.find('K''K''K''K''K''K')
        print('Sua sequência traduzida em quadro de leitura +2 é:\n', a)
        print('A sequência a partir do start códon é:\n', a[a1:a2])
        print(50 * '-=-', '\n\n')
        tradução.write('\n\nSequência integral +2:\t')
        for aa in a:
            tradução.write(aa)
        tradução.write('\nSequência tratada +2:\t')
        for aa in a[a1:a2]:
            tradução.write(aa)
    tradutor2()
    def tradutor3():
        lista = []
        seq1 = ''
        for i in seq[2:]:
            seq1 = seq1 + i
            if len(seq1) == 3:
                lista.append(seq1)
                seq1 = ''
                if 'ata' in lista:
                    lista.remove('ata')
                    lista.append('I')
                    seq1 = ''
                if 'aaa' in lista:
                    lista.remove('aaa')
                    lista.append('K')
                    seq1 = ''
                if 'atc' in lista:
                    lista.remove('atc')
                    lista.append('I')
                    seq1 = ''
                if 'att' in lista:
                    lista.remove('att')
                    lista.append('I')
                    seq1 = ''
                if 'aat' in lista:
                    lista.remove('aat')
                    lista.append('N')
                    seq1 = ''
                if 'atg' in lista:
                    lista.remove('atg')
                    lista.append('M')
                    seq1 = ''
                if 'aca' in lista:
                    lista.remove('aca')
                    lista.append('T')
                    seq1 = ''
                if 'acc' in lista:
                    lista.remove('acc')
                    lista.append('T')
                    seq1 = ''
                if 'aac' in lista:
                    lista.remove('aac')
                    lista.append('N')
                if 'acg' in lista:
                    lista.remove('acg')
                    lista.append('T')
                    seq1 = ''
                if 'act' in lista:
                    lista.remove('act')
                    lista.append('T')
                    seq1 = ''
                if 'acc' in lista:
                    lista.remove('acc')
                    lista.append('N')
                    seq1 = ''
                if 'aag' in lista:
                    lista.remove('aag')
                    lista.append('K')
                    seq1 = ''
                if 'agc' in lista:
                    lista.remove('agc')
                    lista.append('S')
                    seq1 = ''
                if 'agt' in lista:
                    lista.remove('agt')
                    lista.append('S')
                    seq1 = ''
                if 'aga' in lista:
                    lista.remove('aga')
                    lista.append('R')
                    seq1 = ''
                if 'agg' in lista:
                    lista.remove('agg')
                    lista.append('R')
                    seq1 = ''
                if 'cta' in lista:
                    lista.remove('cta')
                    lista.append('L')
                    seq1 = ''
                if 'ctc' in lista:
                    lista.remove('ctc')
                    lista.append('L')
                    seq1 = ''
                if 'ctg' in lista:
                    lista.remove('ctg')
                    lista.append('L')
                    seq1 = ''
                if 'ctt' in lista:
                    lista.remove('ctt')
                    lista.append('L')
                    seq1 = ''
                if 'cca' in lista:
                    lista.remove('cca')
                    lista.append('P')
                    seq1 = ''
                if 'ccc' in lista:
                    lista.remove('ccc')
                    lista.append('P')
                    seq1 = ''
                if 'ccg' in lista:
                    lista.remove('ccg')
                    lista.append('P')
                    seq1 = ''
                if 'cct' in lista:
                    lista.remove('cct')
                    lista.append('P')
                    seq1 = ''
                if 'cac' in lista:
                    lista.remove('cac')
                    lista.append('H')
                    seq1 = ''
                if 'cat' in lista:
                    lista.remove('cat')
                    lista.append('H')
                    seq1 = ''
                if 'caa' in lista:
                    lista.remove('caa')
                    lista.append('Q')
                    seq1 = ''
                if 'cag' in lista:
                    lista.remove('cag')
                    lista.append('Q')
                    seq1 = ''
                if 'cga' in lista:
                    lista.remove('cga')
                    lista.append('R')
                    seq1 = ''
                if 'cgc' in lista:
                    lista.remove('cgc')
                    lista.append('R')
                    seq1 = ''
                if 'cgg' in lista:
                    lista.remove('cgg')
                    lista.append('R')
                    seq1 = ''
                if 'cgt' in lista:
                    lista.remove('cgt')
                    lista.append('R')
                    seq1 = ''
                if 'gta' in lista:
                    lista.remove('gta')
                    lista.append('V')
                    seq1 = ''
                if 'gtc' in lista:
                    lista.remove('gtc')
                    lista.append('V')
                    seq1 = ''
                if 'gtg' in lista:
                    lista.remove('gtg')
                    lista.append('V')
                    seq1 = ''
                if 'gtt' in lista:
                    lista.remove('gtt')
                    lista.append('V')
                    seq1 = ''
                if 'gca' in lista:
                    lista.remove('gca')
                    lista.append('A')
                    seq1 = ''
                if 'gcc' in lista:
                    lista.remove('gcc')
                    lista.append('A')
                    seq1 = ''
                if 'gcg' in lista:
                    lista.remove('gcg')
                    lista.append('A')
                    seq1 = ''
                if 'gct' in lista:
                    lista.remove('gct')
                    lista.append('A')
                    seq1 = ''
                if 'gac' in lista:
                    lista.remove('gac')
                    lista.append('D')
                    seq1 = ''
                if 'gat' in lista:
                    lista.remove('gat')
                    lista.append('D')
                    seq1 = ''
                if 'gag' in lista:
                    lista.remove('gag')
                    lista.append('E')
                    seq1 = ''
                if 'gga' in lista:
                    lista.remove('gga')
                    lista.append('G')
                    seq1 = ''
                if 'gaa' in lista:
                    lista.remove('gaa')
                    lista.append('E')
                    seq1 = ''
                if 'ggc' in lista:
                    lista.remove('ggc')
                    lista.append('G')
                    seq1 = ''
                if 'ggg' in lista:
                    lista.remove('ggg')
                    lista.append('G')
                    seq1 = ''
                if 'ggt' in lista:
                    lista.remove('ggt')
                    lista.append('G')
                    seq1 = ''
                if 'tca' in lista:
                    lista.remove('tca')
                    lista.append('S')
                    seq1 = ''
                if 'ttc' in lista:
                    lista.remove('ttc')
                    lista.append('F')
                    seq1 = ''
                if 'tcg' in lista:
                    lista.remove('tcg')
                    lista.append('S')
                    seq1 = ''
                if 'tct' in lista:
                    lista.remove('tct')
                    lista.append('S')
                    seq1 = ''
                if 'ttc' in lista:
                    lista.remove('ttc')
                    lista.append('F')
                    seq1 = ''
                if 'ttt' in lista:
                    lista.remove('ttt')
                    lista.append('F')
                    seq1 = ''
                if 'tta' in lista:
                    lista.remove('tta')
                    lista.append('L')
                    seq1 = ''
                if 'ttg' in lista:
                    lista.remove('ttg')
                    lista.append('L')
                    seq1 = ''
                if 'tac' in lista:
                    lista.remove('tac')
                    lista.append('Y')
                    seq1 = ''
                if 'tat' in lista:
                    lista.remove('tat')
                    lista.append('Y')
                    seq1 = ''
                if 'taa' in lista:
                    lista.remove('taa')
                    lista.append(('_\t'))
                    seq1 = ''
                if 'tag' in lista:
                    lista.remove('tag')
                    lista.append(('_\t'))
                    seq1 = ''
                if 'tgc' in lista:
                    lista.remove('tgc')
                    lista.append('C')
                    seq1 = ''
                if 'tgt' in lista:
                    lista.remove('tgt')
                    lista.append('C')
                    seq1 = ''
                if 'tga' in lista:
                    lista.remove('tga')
                    lista.append(('_\t'))
                    seq1 = ''
                if 'tgg' in lista:
                    lista.remove('tgg')
                    lista.append('W')
                    seq1 = ''
                if 'tcc' in lista:
                    lista.remove('tcc')
                    lista.append('S')
                    seq1 = ''
                else:
                    seq1 = ''
        a = ''.join(lista)
        a1 = a.find('M')
        a2 = a.find('K''K''K''K''K''K')
        print('Sua sequência traduzida em quadro de leitura +3 é:\n', a)
        print('A sequência a partir do start códon é:\n', a[a1:a2])
        print(50 * '-=-', '\n\n')
        tradução.write('\n\nSequência integral +3:\t')
        for aa in a:
            tradução.write(aa)
        tradução.write('\nSequência tratada +3:\t')
        for aa in a[a1:a2]:
            tradução.write(aa)
    tradutor3()
    def tradutor_1():
        lista3 = []
        seq4 = ''
        d2 = len(seq)
        for i in seq[d2::-1]:
            seq4 = seq4 + i
            if len(seq4) == 3:
                lista3.append(seq4)
                seq4 = ''
                if 'ata' in lista3:
                    lista3.remove('ata')
                    lista3.append('I')
                    seq4 = ''
                if 'aaa' in lista3:
                    lista3.remove('aaa')
                    lista3.append('K')
                    seq4 = ''
                if 'atc' in lista3:
                    lista3.remove('atc')
                    lista3.append('I')
                    seq4 = ''
                if 'att' in lista3:
                    lista3.remove('att')
                    lista3.append('I')
                    seq4 = ''
                if 'aat' in lista3:
                    lista3.remove('aat')
                    lista3.append('N')
                    seq4 = ''
                if 'atg' in lista3:
                    lista3.remove('atg')
                    lista3.append('M')
                    seq4 = ''
                if 'aca' in lista3:
                    lista3.remove('aca')
                    lista3.append('T')
                    seq4 = ''
                if 'acc' in lista3:
                    lista3.remove('acc')
                    lista3.append('T')
                    seq4 = ''
                if 'acg' in lista3:
                    lista3.remove('acg')
                    lista3.append('T')
                    seq4 = ''
                if 'act' in lista3:
                    lista3.remove('act')
                    lista3.append('T')
                    seq4 = ''
                if 'acc' in lista3:
                    lista3.remove('acc')
                    lista3.append('N')
                    seq4 = ''
                if 'aag' in lista3:
                    lista3.remove('aag')
                    lista3.append('K')
                    seq4 = ''
                if 'agc' in lista3:
                    lista3.remove('agc')
                    lista3.append('S')
                    seq4 = ''
                if 'agt' in lista3:
                    lista3.remove('agt')
                    lista3.append('S')
                    seq4 = ''
                if 'aga' in lista3:
                    lista3.remove('aga')
                    lista3.append('R')
                    seq4 = ''
                if 'agg' in lista3:
                    lista3.remove('agg')
                    lista3.append('R')
                    seq4 = ''
                if 'cta' in lista3:
                    lista3.remove('cta')
                    lista3.append('L')
                    seq4 = ''
                if 'ctc' in lista3:
                    lista3.remove('ctc')
                    lista3.append('L')
                    seq4 = ''
                if 'ctg' in lista3:
                    lista3.remove('ctg')
                    lista3.append('L')
                    seq4 = ''
                if 'ctt' in lista3:
                    lista3.remove('ctt')
                    lista3.append('L')
                    seq4 = ''
                if 'cca' in lista3:
                    lista3.remove('cca')
                    lista3.append('P')
                    seq4 = ''
                if 'ccc' in lista3:
                    lista3.remove('ccc')
                    lista3.append('P')
                    seq4 = ''
                if 'ccg' in lista3:
                    lista3.remove('ccg')
                    lista3.append('P')
                    seq4 = ''
                if 'cct' in lista3:
                    lista3.remove('cct')
                    lista3.append('P')
                    seq4 = ''
                if 'cac' in lista3:
                    lista3.remove('cac')
                    lista3.append('H')
                    seq4 = ''
                if 'cat' in lista3:
                    lista3.remove('cat')
                    lista3.append('H')
                    seq4 = ''
                if 'caa' in lista3:
                    lista3.remove('caa')
                    lista3.append('Q')
                    seq4 = ''
                if 'cag' in lista3:
                    lista3.remove('cag')
                    lista3.append('Q')
                    seq4 = ''
                if 'cga' in lista3:
                    lista3.remove('cga')
                    lista3.append('R')
                    seq4 = ''
                if 'cgc' in lista3:
                    lista3.remove('cgc')
                    lista3.append('R')
                    seq4 = ''
                if 'cgg' in lista3:
                    lista3.remove('cgg')
                    lista3.append('R')
                    seq4 = ''
                if 'cgt' in lista3:
                    lista3.remove('cgt')
                    lista3.append('R')
                    seq4 = ''
                if 'gta' in lista3:
                    lista3.remove('gta')
                    lista3.append('V')
                    seq4 = ''
                if 'gtc' in lista3:
                    lista3.remove('gtc')
                    lista3.append('V')
                    seq4 = ''
                if 'gtg' in lista3:
                    lista3.remove('gtg')
                    lista3.append('V')
                    seq4 = ''
                if 'gtt' in lista3:
                    lista3.remove('gtt')
                    lista3.append('V')
                    seq4 = ''
                if 'gca' in lista3:
                    lista3.remove('gca')
                    lista3.append('A')
                    seq4 = ''
                if 'gcc' in lista3:
                    lista3.remove('gcc')
                    lista3.append('A')
                    seq4 = ''
                if 'gcg' in lista3:
                    lista3.remove('gcg')
                    lista3.append('A')
                    seq4 = ''
                if 'gct' in lista3:
                    lista3.remove('gct')
                    lista3.append('A')
                    seq4 = ''
                if 'gac' in lista3:
                    lista3.remove('gac')
                    lista3.append('D')
                    seq4 = ''
                if 'gat' in lista3:
                    lista3.remove('gat')
                    lista3.append('D')
                    seq4 = ''
                if 'gag' in lista3:
                    lista3.remove('gag')
                    lista3.append('E')
                    seq4 = ''
                if 'gga' in lista3:
                    lista3.remove('gga')
                    lista3.append('G')
                    seq4 = ''
                if 'gaa' in lista3:
                    lista3.remove('gaa')
                    lista3.append('E')
                    seq4 = ''
                if 'ggc' in lista3:
                    lista3.remove('ggc')
                    lista3.append('G')
                    seq4 = ''
                if 'ggg' in lista3:
                    lista3.remove('ggg')
                    lista3.append('G')
                    seq4 = ''
                if 'ggt' in lista3:
                    lista3.remove('ggt')
                    lista3.append('G')
                    seq4 = ''
                if 'tca' in lista3:
                    lista3.remove('tca')
                    lista3.append('S')
                    seq4 = ''
                if 'ttc' in lista3:
                    lista3.remove('ttc')
                    lista3.append('F')
                    seq4 = ''
                if 'tcg' in lista3:
                    lista3.remove('tcg')
                    lista3.append('S')
                    seq4 = ''
                if 'tct' in lista3:
                    lista3.remove('tct')
                    lista3.append('S')
                    seq4 = ''
                if 'ttc' in lista3:
                    lista3.remove('ttc')
                    lista3.append('F')
                    seq4 = ''
                if 'ttt' in lista3:
                    lista3.remove('ttt')
                    lista3.append('F')
                    seq4 = ''
                if 'tta' in lista3:
                    lista3.remove('tta')
                    lista3.append('L')
                    seq4 = ''
                if 'ttg' in lista3:
                    lista3.remove('ttg')
                    lista3.append('L')
                    seq4 = ''
                if 'tac' in lista3:
                    lista3.remove('tac')
                    lista3.append('Y')
                    seq4 = ''
                if 'tat' in lista3:
                    lista3.remove('tat')
                    lista3.append('Y')
                    seq4 = ''
                if 'taa' in lista3:
                    lista3.remove('taa')
                    lista3.append(('_\t_\t'))
                    seq4 = ''
                if 'tag' in lista3:
                    lista3.remove('tag')
                    lista3.append(('_\t'))
                    seq4 = ''
                if 'tgc' in lista3:
                    lista3.remove('tgc')
                    lista3.append('C')
                    seq4 = ''
                if 'tgt' in lista3:
                    lista3.remove('tgt')
                    lista3.append('C')
                    seq4 = ''
                if 'tga' in lista3:
                    lista3.remove('tga')
                    lista3.append(('_\t_\t'))
                    seq4 = ''
                if 'tgg' in lista3:
                    lista3.remove('tgg')
                    lista3.append('W')
                    seq4 = ''
                if 'tcc' in lista3:
                    lista3.remove('tcc')
                    lista3.append('S')
                    seq4 = ''
                if 'aac' in lista3:
                    lista3.remove('aac')
                    lista3.append('N')
                    seq4 = ''
                else:
                    seq4 = ''
        d = ''.join(lista3)
        d1 = d.find('M')
        print('Sua sequência traduzida em quadro de leitura -1 é:\n', d)
        print('A sequência a partir do start códon é:\n', d[d1:])
        print(50 * '-=-', '\n\n')
        tradução.write('\n\nSequência integral -1:\t')
        d2 = len(seq)
        for aa in d:
            tradução.write(aa[d2::-1])
        tradução.write('\nSequência tratada -1:\t')
        for aa in d[d1:]:
            tradução.write(aa)
    tradutor_1()
    def tradutor_2():
        lista3 = []
        seq4 = ''
        d2 = len(seq)
        for i in seq[d2::-2]:
            seq4 = seq4 + i
            if len(seq4) == 3:
                lista3.append(seq4)
                seq4 = ''
                if 'ata' in lista3:
                    lista3.remove('ata')
                    lista3.append('I')
                    seq4 = ''
                if 'aaa' in lista3:
                    lista3.remove('aaa')
                    lista3.append('K')
                    seq4 = ''
                if 'atc' in lista3:
                    lista3.remove('atc')
                    lista3.append('I')
                    seq4 = ''
                if 'att' in lista3:
                    lista3.remove('att')
                    lista3.append('I')
                    seq4 = ''
                if 'aat' in lista3:
                    lista3.remove('aat')
                    lista3.append('N')
                    seq4 = ''
                if 'atg' in lista3:
                    lista3.remove('atg')
                    lista3.append('M')
                    seq4 = ''
                if 'aca' in lista3:
                    lista3.remove('aca')
                    lista3.append('T')
                    seq4 = ''
                if 'acc' in lista3:
                    lista3.remove('acc')
                    lista3.append('T')
                    seq4 = ''
                if 'acg' in lista3:
                    lista3.remove('acg')
                    lista3.append('T')
                    seq4 = ''
                if 'act' in lista3:
                    lista3.remove('act')
                    lista3.append('T')
                    seq4 = ''
                if 'acc' in lista3:
                    lista3.remove('acc')
                    lista3.append('N')
                    seq4 = ''
                if 'aag' in lista3:
                    lista3.remove('aag')
                    lista3.append('K')
                    seq4 = ''
                if 'agc' in lista3:
                    lista3.remove('agc')
                    lista3.append('S')
                    seq4 = ''
                if 'agt' in lista3:
                    lista3.remove('agt')
                    lista3.append('S')
                    seq4 = ''
                if 'aga' in lista3:
                    lista3.remove('aga')
                    lista3.append('R')
                    seq4 = ''
                if 'agg' in lista3:
                    lista3.remove('agg')
                    lista3.append('R')
                    seq4 = ''
                if 'cta' in lista3:
                    lista3.remove('cta')
                    lista3.append('L')
                    seq4 = ''
                if 'ctc' in lista3:
                    lista3.remove('ctc')
                    lista3.append('L')
                    seq4 = ''
                if 'ctg' in lista3:
                    lista3.remove('ctg')
                    lista3.append('L')
                    seq4 = ''
                if 'ctt' in lista3:
                    lista3.remove('ctt')
                    lista3.append('L')
                    seq4 = ''
                if 'cca' in lista3:
                    lista3.remove('cca')
                    lista3.append('P')
                    seq4 = ''
                if 'ccc' in lista3:
                    lista3.remove('ccc')
                    lista3.append('P')
                    seq4 = ''
                if 'ccg' in lista3:
                    lista3.remove('ccg')
                    lista3.append('P')
                    seq4 = ''
                if 'cct' in lista3:
                    lista3.remove('cct')
                    lista3.append('P')
                    seq4 = ''
                if 'cac' in lista3:
                    lista3.remove('cac')
                    lista3.append('H')
                    seq4 = ''
                if 'cat' in lista3:
                    lista3.remove('cat')
                    lista3.append('H')
                    seq4 = ''
                if 'caa' in lista3:
                    lista3.remove('caa')
                    lista3.append('Q')
                    seq4 = ''
                if 'cag' in lista3:
                    lista3.remove('cag')
                    lista3.append('Q')
                    seq4 = ''
                if 'cga' in lista3:
                    lista3.remove('cga')
                    lista3.append('R')
                    seq4 = ''
                if 'cgc' in lista3:
                    lista3.remove('cgc')
                    lista3.append('R')
                    seq4 = ''
                if 'cgg' in lista3:
                    lista3.remove('cgg')
                    lista3.append('R')
                    seq4 = ''
                if 'cgt' in lista3:
                    lista3.remove('cgt')
                    lista3.append('R')
                    seq4 = ''
                if 'gta' in lista3:
                    lista3.remove('gta')
                    lista3.append('V')
                    seq4 = ''
                if 'gtc' in lista3:
                    lista3.remove('gtc')
                    lista3.append('V')
                    seq4 = ''
                if 'gtg' in lista3:
                    lista3.remove('gtg')
                    lista3.append('V')
                    seq4 = ''
                if 'gtt' in lista3:
                    lista3.remove('gtt')
                    lista3.append('V')
                    seq4 = ''
                if 'gca' in lista3:
                    lista3.remove('gca')
                    lista3.append('A')
                    seq4 = ''
                if 'gcc' in lista3:
                    lista3.remove('gcc')
                    lista3.append('A')
                    seq4 = ''
                if 'gcg' in lista3:
                    lista3.remove('gcg')
                    lista3.append('A')
                    seq4 = ''
                if 'gct' in lista3:
                    lista3.remove('gct')
                    lista3.append('A')
                    seq4 = ''
                if 'gac' in lista3:
                    lista3.remove('gac')
                    lista3.append('D')
                    seq4 = ''
                if 'gat' in lista3:
                    lista3.remove('gat')
                    lista3.append('D')
                    seq4 = ''
                if 'gag' in lista3:
                    lista3.remove('gag')
                    lista3.append('E')
                    seq4 = ''
                if 'gga' in lista3:
                    lista3.remove('gga')
                    lista3.append('G')
                    seq4 = ''
                if 'gaa' in lista3:
                    lista3.remove('gaa')
                    lista3.append('E')
                    seq4 = ''
                if 'ggc' in lista3:
                    lista3.remove('ggc')
                    lista3.append('G')
                    seq4 = ''
                if 'ggg' in lista3:
                    lista3.remove('ggg')
                    lista3.append('G')
                    seq4 = ''
                if 'ggt' in lista3:
                    lista3.remove('ggt')
                    lista3.append('G')
                    seq4 = ''
                if 'tca' in lista3:
                    lista3.remove('tca')
                    lista3.append('S')
                    seq4 = ''
                if 'ttc' in lista3:
                    lista3.remove('ttc')
                    lista3.append('F')
                    seq4 = ''
                if 'tcg' in lista3:
                    lista3.remove('tcg')
                    lista3.append('S')
                    seq4 = ''
                if 'tct' in lista3:
                    lista3.remove('tct')
                    lista3.append('S')
                    seq4 = ''
                if 'ttc' in lista3:
                    lista3.remove('ttc')
                    lista3.append('F')
                    seq4 = ''
                if 'ttt' in lista3:
                    lista3.remove('ttt')
                    lista3.append('F')
                    seq4 = ''
                if 'tta' in lista3:
                    lista3.remove('tta')
                    lista3.append('L')
                    seq4 = ''
                if 'ttg' in lista3:
                    lista3.remove('ttg')
                    lista3.append('L')
                    seq4 = ''
                if 'tac' in lista3:
                    lista3.remove('tac')
                    lista3.append('Y')
                    seq4 = ''
                if 'tat' in lista3:
                    lista3.remove('tat')
                    lista3.append('Y')
                    seq4 = ''
                if 'taa' in lista3:
                    lista3.remove('taa')
                    lista3.append(('_\t'))
                    seq4 = ''
                if 'tag' in lista3:
                    lista3.remove('tag')
                    lista3.append(('_\t'))
                    seq4 = ''
                if 'tgc' in lista3:
                    lista3.remove('tgc')
                    lista3.append('C')
                    seq4 = ''
                if 'tgt' in lista3:
                    lista3.remove('tgt')
                    lista3.append('C')
                    seq4 = ''
                if 'tga' in lista3:
                    lista3.remove('tga')
                    lista3.append(('_\t'))
                    seq4 = ''
                if 'tgg' in lista3:
                    lista3.remove('tgg')
                    lista3.append('W')
                    seq4 = ''
                if 'tcc' in lista3:
                    lista3.remove('tcc')
                    lista3.append('S')
                    seq4 = ''
                if 'aac' in lista3:
                    lista3.remove('aac')
                    lista3.append('N')
                    seq4 = ''
                else:
                    seq4 = ''
        d = ''.join(lista3)
        d1 = d.find('M')
        print('Sua sequência traduzida em quadro de leitura -2 é:\n', d)
        print('A sequência a partir do start códon é:\n', d[d1:])
        print(50 * '-=-', '\n\n')
        tradução.write('\n\nSequência integral -2:\t')
        for aa in d:
            tradução.write(aa[d2::-2])
        tradução.write('\nSequência tratada -2:\t')
        for aa in d[d1:]:
            tradução.write(aa)
    tradutor_2()
    def tradutor_3():
        lista3 = []
        seq4 = ''
        d2 = len(seq)
        for i in seq[d2::-3]:
            seq4 = seq4 + i
            if len(seq4) == 3:
                lista3.append(seq4)
                seq4 = ''
                if 'ata' in lista3:
                    lista3.remove('ata')
                    lista3.append('I')
                    seq4 = ''
                if 'aaa' in lista3:
                    lista3.remove('aaa')
                    lista3.append('K')
                    seq4 = ''
                if 'atc' in lista3:
                    lista3.remove('atc')
                    lista3.append('I')
                    seq4 = ''
                if 'att' in lista3:
                    lista3.remove('att')
                    lista3.append('I')
                    seq4 = ''
                if 'aat' in lista3:
                    lista3.remove('aat')
                    lista3.append('N')
                    seq4 = ''
                if 'atg' in lista3:
                    lista3.remove('atg')
                    lista3.append('M')
                    seq4 = ''
                if 'aca' in lista3:
                    lista3.remove('aca')
                    lista3.append('T')
                    seq4 = ''
                if 'acc' in lista3:
                    lista3.remove('acc')
                    lista3.append('T')
                    seq4 = ''
                if 'acg' in lista3:
                    lista3.remove('acg')
                    lista3.append('T')
                    seq4 = ''
                if 'act' in lista3:
                    lista3.remove('act')
                    lista3.append('T')
                    seq4 = ''
                if 'acc' in lista3:
                    lista3.remove('acc')
                    lista3.append('N')
                    seq4 = ''
                if 'aag' in lista3:
                    lista3.remove('aag')
                    lista3.append('K')
                    seq4 = ''
                if 'agc' in lista3:
                    lista3.remove('agc')
                    lista3.append('S')
                    seq4 = ''
                if 'agt' in lista3:
                    lista3.remove('agt')
                    lista3.append('S')
                    seq4 = ''
                if 'aga' in lista3:
                    lista3.remove('aga')
                    lista3.append('R')
                    seq4 = ''
                if 'agg' in lista3:
                    lista3.remove('agg')
                    lista3.append('R')
                    seq4 = ''
                if 'cta' in lista3:
                    lista3.remove('cta')
                    lista3.append('L')
                    seq4 = ''
                if 'ctc' in lista3:
                    lista3.remove('ctc')
                    lista3.append('L')
                    seq4 = ''
                if 'ctg' in lista3:
                    lista3.remove('ctg')
                    lista3.append('L')
                    seq4 = ''
                if 'ctt' in lista3:
                    lista3.remove('ctt')
                    lista3.append('L')
                    seq4 = ''
                if 'cca' in lista3:
                    lista3.remove('cca')
                    lista3.append('P')
                    seq4 = ''
                if 'ccc' in lista3:
                    lista3.remove('ccc')
                    lista3.append('P')
                    seq4 = ''
                if 'ccg' in lista3:
                    lista3.remove('ccg')
                    lista3.append('P')
                    seq4 = ''
                if 'cct' in lista3:
                    lista3.remove('cct')
                    lista3.append('P')
                    seq4 = ''
                if 'cac' in lista3:
                    lista3.remove('cac')
                    lista3.append('H')
                    seq4 = ''
                if 'cat' in lista3:
                    lista3.remove('cat')
                    lista3.append('H')
                    seq4 = ''
                if 'caa' in lista3:
                    lista3.remove('caa')
                    lista3.append('Q')
                    seq4 = ''
                if 'cag' in lista3:
                    lista3.remove('cag')
                    lista3.append('Q')
                    seq4 = ''
                if 'cga' in lista3:
                    lista3.remove('cga')
                    lista3.append('R')
                    seq4 = ''
                if 'cgc' in lista3:
                    lista3.remove('cgc')
                    lista3.append('R')
                    seq4 = ''
                if 'cgg' in lista3:
                    lista3.remove('cgg')
                    lista3.append('R')
                    seq4 = ''
                if 'cgt' in lista3:
                    lista3.remove('cgt')
                    lista3.append('R')
                    seq4 = ''
                if 'gta' in lista3:
                    lista3.remove('gta')
                    lista3.append('V')
                    seq4 = ''
                if 'gtc' in lista3:
                    lista3.remove('gtc')
                    lista3.append('V')
                    seq4 = ''
                if 'gtg' in lista3:
                    lista3.remove('gtg')
                    lista3.append('V')
                    seq4 = ''
                if 'gtt' in lista3:
                    lista3.remove('gtt')
                    lista3.append('V')
                    seq4 = ''
                if 'gca' in lista3:
                    lista3.remove('gca')
                    lista3.append('A')
                    seq4 = ''
                if 'gcc' in lista3:
                    lista3.remove('gcc')
                    lista3.append('A')
                    seq4 = ''
                if 'gcg' in lista3:
                    lista3.remove('gcg')
                    lista3.append('A')
                    seq4 = ''
                if 'gct' in lista3:
                    lista3.remove('gct')
                    lista3.append('A')
                    seq4 = ''
                if 'gac' in lista3:
                    lista3.remove('gac')
                    lista3.append('D')
                    seq4 = ''
                if 'gat' in lista3:
                    lista3.remove('gat')
                    lista3.append('D')
                    seq4 = ''
                if 'gag' in lista3:
                    lista3.remove('gag')
                    lista3.append('E')
                    seq4 = ''
                if 'gga' in lista3:
                    lista3.remove('gga')
                    lista3.append('G')
                    seq4 = ''
                if 'gaa' in lista3:
                    lista3.remove('gaa')
                    lista3.append('E')
                    seq4 = ''
                if 'ggc' in lista3:
                    lista3.remove('ggc')
                    lista3.append('G')
                    seq4 = ''
                if 'ggg' in lista3:
                    lista3.remove('ggg')
                    lista3.append('G')
                    seq4 = ''
                if 'ggt' in lista3:
                    lista3.remove('ggt')
                    lista3.append('G')
                    seq4 = ''
                if 'tca' in lista3:
                    lista3.remove('tca')
                    lista3.append('S')
                    seq4 = ''
                if 'ttc' in lista3:
                    lista3.remove('ttc')
                    lista3.append('F')
                    seq4 = ''
                if 'tcg' in lista3:
                    lista3.remove('tcg')
                    lista3.append('S')
                    seq4 = ''
                if 'tct' in lista3:
                    lista3.remove('tct')
                    lista3.append('S')
                    seq4 = ''
                if 'ttc' in lista3:
                    lista3.remove('ttc')
                    lista3.append('F')
                    seq4 = ''
                if 'ttt' in lista3:
                    lista3.remove('ttt')
                    lista3.append('F')
                    seq4 = ''
                if 'tta' in lista3:
                    lista3.remove('tta')
                    lista3.append('L')
                    seq4 = ''
                if 'ttg' in lista3:
                    lista3.remove('ttg')
                    lista3.append('L')
                    seq4 = ''
                if 'tac' in lista3:
                    lista3.remove('tac')
                    lista3.append('Y')
                    seq4 = ''
                if 'tat' in lista3:
                    lista3.remove('tat')
                    lista3.append('Y')
                    seq4 = ''
                if 'taa' in lista3:
                    lista3.remove('taa')
                    lista3.append(('_\t'))
                    seq4 = ''
                if 'tag' in lista3:
                    lista3.remove('tag')
                    lista3.append(('_\t'))
                    seq4 = ''
                if 'tgc' in lista3:
                    lista3.remove('tgc')
                    lista3.append('C')
                    seq4 = ''
                if 'tgt' in lista3:
                    lista3.remove('tgt')
                    lista3.append('C')
                    seq4 = ''
                if 'tga' in lista3:
                    lista3.remove('tga')
                    lista3.append(('_\t'))
                    seq4 = ''
                if 'tgg' in lista3:
                    lista3.remove('tgg')
                    lista3.append('W')
                    seq4 = ''
                if 'tcc' in lista3:
                    lista3.remove('tcc')
                    lista3.append('S')
                    seq4 = ''
                if 'aac' in lista3:
                    lista3.remove('aac')
                    lista3.append('N')
                    seq4 = ''
                else:
                    seq4 = ''
        d = ''.join(lista3)
        d1 = d.find('M')
        print('Sua sequência traduzida em quadro de leitura -3 é:\n', d)
        print('A sequência a partir do start códon é:\n', d[d1:])
        print(50 * '-=-', '\n\n')
        tradução.write('\n\nSequência integral -3:\t')
        for aa in d:
            tradução.write(aa[d2::-3])
        tradução.write('\nSequência tratada -3:\t')
        for aa in d[d1:]:
            tradução.write(aa)
    tradutor_3()

