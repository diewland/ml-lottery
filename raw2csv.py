import re

months = {
    'มกราคม': 1,
    'กุมภาพันธ์': 2,
    'มีนาคม': 3,
    'เมษายน': 4,
    'พฤษภาคม': 5,
    'มิถุนายน': 6,
    'กรกฎาคม': 7,
    'สิงหาคม': 8,
    'กันยายน': 9,
    'ตุลาคม': 10,
    'พฤศจิกายน': 11,
    'ธันวาคม': 12,
}

rows = []

# parse raw data to rows
infile = open('lottery.txt', encoding='utf-8')
for line in infile:
    l = line.strip()
    if l:
        m = re.match("(\d+ .+ 25..) (.+)", l)
        dmy = m.group(1).split()
        raw = m.group(2).replace(' ', '')
        raw_x = raw[:]

        # dmy
        day = dmy[0]
        month = months[dmy[1]]
        year = int(dmy[2]) - 543

        # collect other fields
        no1 = None
        top2 = None
        top3 = None
        bottom2 = None
        front3_1 = None
        front3_2 = None
        bottom3_1 = None
        bottom3_2 = None

        # no 1
        if year < 1995:
            no1 = raw[:7]
        else:
            no1 = raw[:6]
        raw = raw.replace(no1, '', 1)

        # top2
        top2 = raw[:2]
        raw = raw.replace(top2, '', 1)

        # top3
        top3 = raw[:3]
        raw = raw.replace(top3, '', 1)

        # bottom2
        bottom2 = raw[:2]
        raw = raw.replace(bottom2, '', 1)

        # front3_1
        front3_1 = raw[:3]
        raw = raw.replace(front3_1, '', 1)

        # front3_2
        front3_2 = raw[:3]
        raw = raw.replace(front3_2, '', 1)

        # bottom3_1
        bottom3_1 = raw[:3]
        raw = raw.replace(bottom3_1, '', 1)

        # bottom3_2
        bottom3_2 = raw[:3]
        raw = raw.replace(bottom3_2, '', 1)

        # cross check
        xcheck = [
            no1,
            top2,
            top3,
            bottom2,
            front3_1,
            front3_2,
            bottom3_1,
            bottom3_2,
        ]
        if raw_x != "".join(xcheck):
            print(raw_x)
            print("".join(xcheck))
            raise ValueError("Data not match")

        # sum
        row = [
            day,
            month,
            year,
            no1,
            top2,
            top3,
            bottom2,
            front3_1,
            front3_2,
            bottom3_1,
            bottom3_2,
        ]

        rows.append(row)

# print csv
print("day,month,year,no1,top2,top3,bottom2,front3_1,front3_2,bottom3_1,bottom3_2")
for row in rows:
    print(",".join([ str(v) for v in row ]))
    #print("'%s'" % "','".join([ str(v) for v in row ]))
