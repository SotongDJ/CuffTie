import json, pprint

"""--- README of exp06-fsp ---
Title:
    Polymerise Summary of FastQC
    (f.s.p. stand for fastqc summary polymerise)

Required files:
    ./data/config.json

--- README ---"""

configsi = 'data/config.json'

configfa = open(configsi,'r')

configso = json.load(configfa)
configdi = configso.get('var',{})
pafwasi = configdi.get('path',{}).get('fastqc-comb',"")
grupoli = configdi.get('group',[])
tribeli = configdi.get('tribe',[])
prefisdi = configdi.get('prefix',{})
blanksi = configdi.get('blank-prefix',{})

pngconfi = configdi.get('png',0)
pnglibfa = open('exp06-fsp-pngtemplate.json','r')
pnglibdi = json.load(pnglibfa)

faslidi = configso.get('fastqc-list',{})
rowlist = faslidi.get("row",{})
rowlitu = tuple(rowlist)
colspan = faslidi.get("colspan",1)

inputsi = pafwasi + '/result.json'
inputfa = open(inputsi,'r')
inputso = json.load(inputfa)

faledi = inputso.get('fale',{})
catedi = inputso.get('cate',{})

resutdi = {}
resutsi = pafwasi + '/result.html'
resutfa = open(resutsi,'w')

"""
resutdi={
    group:{ # primadi
        tribe:[ # seconli / blankli
            fale,
            fale
        ]
    },
    group:{
        tribe:[
            fale,
            fale
        ]
    }
}
"""

for grupo in grupoli:
    primadi = {}
    primadi = resutdi.get(grupo,{})

    for tribe in tribeli:
        seconli = {}
        seconli = primadi.get(tribe,[])

        blankli = {}
        blankli = primadi.get(blanksi,[])

        for fale in faledi:
            if grupo in fale:

                prefis = prefisdi.get(tribe,"")
                if prefis != "":
                    if prefis in fale:
                        seconli.append(fale)
                    else:
                        blankli.append(fale)

        primadi.update({ tribe : seconli })
        primadi.update({ blanksi : blankli })

    resutdi.update({ grupo : primadi })

# pprint.pprint(resutdi)

headsi = """<!DOCTYPE html>
<html>
<head>
<style>
h2 {
    text-align: center
}
table, th, td {
    border: 2px solid black;
    border-collapse: collapse;
    background-color: #EDF7F9;
    margin: auto;
    text-align: center;
}
th, td {
    padding: 15px;
}
</style>
</head>
<body>
"""
resutfa.write(headsi)

for grupo in list(resutdi.keys()):

    metasi = ""
    metasi = "<table>\n    <caption><h2>" + grupo + "</h2></caption>\n"
    resutfa.write(metasi)

    primadi = {}
    primadi = resutdi.get(grupo,{})

    tribetu = ()
    tribetu = tuple(primadi.keys())
    faletu = ()

    metasi = "    <tr>\n        <th>Types</th>\n"
    resutfa.write(metasi)

    for n in range(len(tribetu)):
        tribe = ""
        tribe = tribetu[n]
        if colspan > 1:
            metasi = "        <th colspan=\"" + str(colspan) + "\">" + tribe + "</th>\n"
        else:
            metasi = "        <th>" + tribe + "</th>\n"
        resutfa.write(metasi)

        seconli = primadi.get(tribe,[])
        faletu = faletu + tuple(sorted(seconli))

    metasi = "    </tr>\n"
    resutfa.write(metasi)

    metasi = "    <tr>\n        <th>Files</th>\n"
    resutfa.write(metasi)

    for n in range(len(faletu)):
        fale = ""
        fale = faletu[n]
        metasi = "        <th>" + fale + "</th>\n"
        resutfa.write(metasi)

    metasi = "    </tr>\n"
    resutfa.write(metasi)

    for nume in range(len(rowlitu)):
        rowlisi=""
        rowlisi = rowlitu[nume]
        metasi = "    <tr>\n        <th>" + rowlisi + "</th>\n"
        resutfa.write(metasi)

        for n in range(len(faletu)):
            fale = ""
            fale = faletu[n]
            valusi = catedi.get(rowlisi,{}).get(fale,'')
            if pngconfi == 1:
                metasi = "        <td>" + pnglibdi.get(valusi,"") + "</td>\n"
            else:
                metasi = "        <td>" + valusi + "</td>\n"
            resutfa.write(metasi)


        metasi = "    </tr>\n"
        resutfa.write(metasi)

    metasi = "</table>\n<br>"
    resutfa.write(metasi)


endsi = """</body>
</html>
"""
resutfa.write(endsi)

resutfa.close()
