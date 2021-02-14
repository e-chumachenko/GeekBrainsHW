with open('curriculum.txt', encoding='utf-8') as c_file:
    data = c_file.readlines()
    curriculum = {}
    for line in data:
        subject = line.split()[0][0:-1]
        hours, hours_l, hours_pr, hours_lab = (0, 0, 0, 0)
        if line.split()[1] != '—':
            hours_l = float(line.split()[1][0:-3])
        if line.split()[2] != '—':
            hours_pr = float(line.split()[2][0:-4])
        if line.split()[3] != '—':
            hours_lab = float(line.split()[3][0:-5])
        hours = hours_l + hours_pr + hours_lab
        curriculum[subject] = hours
    print(curriculum)
