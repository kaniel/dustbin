# -*- coding:utf-8 -*-
__author__ = 'keniel'

# 计算积水量计算积水量


def water(l):
    if len(l) <= 1:
        return
    len_l = len(l)
    print "len(L):", len_l
    k = 0
    water_num = 0
    for item in xrange(len_l):
        if k == len_l - 1:
            break
        if l[k] == 0:
            k += 1
            continue
        start = k
        end = k + 1
        print "start:%d, value:%d, end:%d, value:%d" % (start, l[start], end, l[end])
        temp = end
        for x in l[end:]:
            # print "===>", l[start], l[end], x
            if l[start] <= l[start + 1]:
                break
            if l[end] < x:
                end = temp
                if l[start] <= x:
                    break
            if temp == len_l - 1:
                break
            temp += 1
        print "start:", start, end
        if start + 1 == end:
            k += 1
            continue
        else:
            print "--->start:%d, value:%d, end:%d, value:%d" % (start, l[start], end, l[end])
            for item in range(start, end):
                if l[start] <= l[end]:
                    print "abs start:", start
                    water_num += abs(l[start] - l[item])
                elif l[start] > l[end]:
                    print "abs end:", end
                    water_num += abs(l[end] - l[item + 1])
            print "water:", water_num
            k = end
    return water_num


if __name__ == "__main__":
    # l = [1, 0, 2, 1, 0, 1, 2, 3, 2, 1, 2]
    l = [2, 3, 0, 1, 2, 0, 1, 0, 1, 2, 0, 3, 0, 2, 0, 1, 2, 1, 0]
    print "L:", l
    res = water(l)
    print "res:", res