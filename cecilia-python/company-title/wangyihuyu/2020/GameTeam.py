#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   GameTeam.py    
@Contact :   70904372cecilia@gmail.com
@License :   (C)Copyright 2019-2020

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/4/19 18:25   cecilia      1.0        游戏组队

问题描述：小易新开发了一个游戏，游戏里有N个职业，如肉盾、医生、召唤、物理近战、物理远程、法术近战、法术远程等。
现在每个职业都有M个不同的玩家，因此共有N*M个玩家。每个玩家都有一个唯一的名字，这个名字是一个大小写敏感的字母，
这些玩家想要组成M支队伍。每支队伍里都要包含N个职业，每个职业有且仅有一名玩家。
这些玩家对和自己组队的其他职业玩家有要求，有的要求是“必须不和某人组队”，有的要求是“必须要和某人组队”。
现在收到了所有玩家的要求，要怎么样组队才能满足所有人的要求？

输入描述：第一行包含两个正整数N和M，表示总共有N个职业，每个职业有M个玩家，1<N<7,1<M<7。
接下来有N行，每行包含M个字符的字符串，其中第i行（1<i<N）表示第i个职业的M个玩家的名字。
剩下的若干行，每行是玩家的要求，每个要求的格式是i j X P q，1<=i,p<=N, 1<=j,q<=M,X可能是字符Y或者字符N。
如果X是字符Y，表示第i个职业的第j个玩家要求必须和第p个职业的第q个玩家组队；
如果X是字符N，表示第i个职业的dij个玩家要求必须不和dip个职业的第q个玩家组队。
输入以0 0 N 0 0为代表输入结束。

示例：
输入：
3 4
ABCD
efgh
IJKL
1 1 Y 3 2
1 2 N 2 2
2 2 Y 3 4
1 3 Y 2 3
1 1 N 2 4
3 1 Y 1 3
0 0 N 0 0

输出：
AeJ
BhK
CgI
DfL

解释：
第一个职业有ABCD个玩家；第二个职业有efgh四名玩家；第三个职业有IJKL四名玩家；
A要求和J组队，B不要和f组队，f要和L组队，C要和g组队，A不要和ｈ组队，Ｉ要和Ｃ组队。

输入保证不存在矛盾，且存在唯一解。

"""
