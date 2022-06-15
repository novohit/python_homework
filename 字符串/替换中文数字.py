def char_to_num(num):
    new_str=""
    num_dict={"零":u"0","一":u"1","二":u"2","三":u"3","四":u"4","五":u"5","六":u"6","七":u"7","八":u"8","九":u"9"}
    listnum=list(num)
    shu=[]
    for i in listnum:
        if i in num_dict:
            shu.append(num_dict[i])
        else:
            shu.append(i)
    new_str="".join(shu)
    return new_str

print(char_to_num(input()))
